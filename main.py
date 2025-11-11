# https://docs.google.com/presentation/d/1lo89ViUnysgyNwuzQWl-AGnRaN_UDXWcfgv2GKNnsNQ/edit?slide=id.g2d0e52ba0ec_0_0#slide=id.g2d0e52ba0ec_0_0
# https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbk5iWmRCVHFQNmMzNjJ2SlloempXX3NPTGMyd3xBQ3Jtc0ttM1R3eGFiNmlPV3FYWjl0aXVyVXp5RXF1TnFMNEY4SncyRHh6VUFzbWdKcE05MWQ0WkpIUGdLTzhLSnhuS3NFeDdhRmcxTFJJald2NC1NeTZDN2JveGF3UUdocVk5NXVjaGpCWTkyQ0JQTkpvY0k5RQ&q=https%3A%2F%2Fdocs.google.com%2Fspreadsheets%2Fd%2F1-t9KenqGfLNrd8UJ79xS7eaq42ed95E7jf0VnavGuoA%2Fedit%3Fgid%3D720500922%23gid%3D720500922&v=LkcsMjC5QOo
# https://www.youtube.com/watch?v=LkcsMjC5QOo&t=1070s

import streamlit as st
import pandas as pd

def calc_general_stats(df:pd.DataFrame):
     df_data = df.groupby(by = "Data")[["Valor"]].sum()
     df_data["lag_1"] = df_data["Valor"].shift(1)
     df_data["Diferença Mensal Abs."] = df_data["Valor"] - df_data["lag_1"]
     df_data["Média 6M Diferença Mensal Abs."] = df_data["Diferença Mensal Abs."].rolling(6).mean()
     df_data["Média 12M Diferença Mensal Abs."] = df_data["Diferença Mensal Abs."].rolling(12).mean()
     df_data["Média 24M Diferença Mensal Abs."] = df_data["Diferença Mensal Abs."].rolling(24).mean()
     df_data["Diferença Mensal Rel."] = df_data["Valor"] / df_data["lag_1"] - 1
     df_data["Evolução 6M Total"] = df_data["Valor"].rolling(6).apply(lambda x: x[-1] - x[0])
     df_data["Evolução 12M Total"] = df_data["Valor"].rolling(12).apply(lambda x: x[-1] - x[0])
     df_data["Evolução 24M Total"] = df_data["Valor"].rolling(24).apply(lambda x: x[-1] - x[0])
     df_data["Evolução 6M Relativa"] = df_data["Valor"].rolling(6).apply(lambda x: x[-1] / x[0] - 1)
     df_data["Evolução 12M Relativa"] = df_data["Valor"].rolling(12).apply(lambda x: x[-1] / x[0] - 1)
     df_data["Evolução 24M Relativa"] = df_data["Valor"].rolling(24).apply(lambda x: x[-1] / x[0] - 1)

     df_data = df_data.drop("lag_1", axis = 1)

     return df_data

st.set_page_config(page_title="Finanças", page_icon="💰")

st.markdown(
"""
# Boas vindas!

## Nosso APP Financeiro!

Espero que você curta a experiência da nossa solução para organização financeira.

"""
)
# Widget de upload de dados
file_upload = st.file_uploader(label="Faça upload dos dados aqui", type=["csv"])

# Verifica se foi feito upload de algum arquivo
if file_upload:

     # Leitura dos dados
     df = pd.read_csv(file_upload)
     df["Data"] = pd.to_datetime(df["Data"], format = "%d/%m/%Y").dt.date

     # Exibição dos dados do app
     exp1 = st.expander("Dados Brutos")
     columns_fmt = {"Valor" : st.column_config.NumberColumn("Valor", format="R$ %f")}
     exp1.dataframe(df, hide_index= True, column_config= columns_fmt)

     # Visão Instituição
     exp2 = st.expander("Instituições")
     df_instituicao = df.pivot_table(index = "Data", columns = "Instituição", values = "Valor")

     tab_data, tab_history, tab_share = exp2.tabs(["Dados", "Histórico", "Distribuição"])

     with tab_data:
          st.dataframe(df_instituicao)
     
     with tab_history:
          st.line_chart(df_instituicao)

     with tab_share:
          
          date = st.selectbox("Filtro Data", options = df_instituicao.index)
          # Input de data
          # date = st.date_input("Data para Distribuição",
          #                      min_value=df_instituicao.index.min(),
          #                      max_value=df_instituicao.index.max()
          #                      )
          # Condição caso seja inputada data inválida
          # if date not in df_instituicao.index:
          #      st.warning("Entre com uma data válida")
          # else:
               # Obtém a última data de dados
               # last_dt = df_instituicao.sort_index().iloc[-1]  
          st.bar_chart(df_instituicao.loc[date])

     exp3 = st.expander("Estatísticas Gerais")

     df_stats = calc_general_stats(df)
     columns_config = {
          "Valor": st.column_config.NumberColumn("Valor", format = "R$ %.2f"),
          "Diferença Mensal Abs.": st.column_config.NumberColumn("Diferença Mensal Abs.", format = "R$ %.2f"),
          "Média 6M Diferença Mensal Abs.": st.column_config.NumberColumn("Média 6M Diferença Mensal Abs.", format = "R$ %.2f"),
          "Média 12M Diferença Mensal Abs.": st.column_config.NumberColumn("Média 12M Diferença Mensal Abs.", format = "R$ %.2f"),
          "Média 24M Diferença Mensal Abs.": st.column_config.NumberColumn("Média 24M Diferença Mensal Abs.", format = "R$ %.2f"),
          "Evolução 6M Total": st.column_config.NumberColumn("Evolução 6M Total", format = "R$ %.2f"),
          "Evolução 12M Total":  st.column_config.NumberColumn("Evolução 12M Total", format = "R$ %.2f"),
          "Evolução 24M Total": st.column_config.NumberColumn("Evolução 24M Total", format = "R$ %.2f"),
          "Diferença Mensal Rel.": st.column_config.NumberColumn("Diferença Mensal Rel.", format = "percent"),
          "Evolução 6M Relativa": st.column_config.NumberColumn("Evolução 6M Relativa", format = "percent"),
          "Evolução 12M Relativa":st.column_config.NumberColumn("Evolução 12M Relativa", format = "percent"),
          "Evolução 24M Relativa": st.column_config.NumberColumn("Evolução 24M Relativa", format = "percent")
     }

     tab_stats, tab_abs, tab_rel = exp3.tabs(tabs = ["Dados", "Histórico de Evolução", "Crescimento Relativo"])

     with tab_stats:
          st.dataframe(df_stats, column_config = columns_config )

     with tab_abs:
          abs_cols = [
               "Diferença Mensal Abs.",
               "Média 6M Diferença Mensal Abs.",
               "Média 12M Diferença Mensal Abs.",
               "Média 24M Diferença Mensal Abs."
          ]
          st.line_chart(df_stats[abs_cols])

     with tab_rel:
          rel_cols = [
               "Diferença Mensal Rel.",
               "Evolução 6M Relativa",
               "Evolução 12M Relativa",
               "Evolução 24M Relativa"
          ]
          st.line_chart(df_stats[rel_cols    ])

# Não tem arquivos...
