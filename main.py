# https://docs.google.com/presentation/d/1lo89ViUnysgyNwuzQWl-AGnRaN_UDXWcfgv2GKNnsNQ/edit?slide=id.g2d0e52ba0ec_0_0#slide=id.g2d0e52ba0ec_0_0
# https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbk5iWmRCVHFQNmMzNjJ2SlloempXX3NPTGMyd3xBQ3Jtc0ttM1R3eGFiNmlPV3FYWjl0aXVyVXp5RXF1TnFMNEY4SncyRHh6VUFzbWdKcE05MWQ0WkpIUGdLTzhLSnhuS3NFeDdhRmcxTFJJald2NC1NeTZDN2JveGF3UUdocVk5NXVjaGpCWTkyQ0JQTkpvY0k5RQ&q=https%3A%2F%2Fdocs.google.com%2Fspreadsheets%2Fd%2F1-t9KenqGfLNrd8UJ79xS7eaq42ed95E7jf0VnavGuoA%2Fedit%3Fgid%3D720500922%23gid%3D720500922&v=LkcsMjC5QOo
# https://www.youtube.com/watch?v=LkcsMjC5QOo&t=1070s

import streamlit as st
import pandas as pd

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

     # Exibição dos dados do app
     columns_fmt = {"Valor" : st.column_config.NumberColumn("Valor", format="R$ %f")}
     st.dataframe(df, hide_index= True, column_config= columns_fmt)