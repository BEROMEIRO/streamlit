import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from views import upload

# Configuração do Streamlit
st.set_page_config(page_title="Dashboard de Exemplos", layout="wide")

# Sidebar com menu e filtros
st.sidebar.title("Menu")
pagina = st.sidebar.selectbox("Escolha a página", ["Home", "Dashboard", "Upload", "Sobre"])

if pagina == "Home":
    st.title("Bem-vindo à Página Inicial")
    st.write("Esta é a página principal do app.")

elif pagina == "Dashboard":
    st.title("📊 Dashboard Interativo com Streamlit")

    # Criando dados fictícios para os gráficos
    def generate_data():
        np.random.seed(42)
        data = pd.DataFrame({
            'Categoria': np.random.choice(['A', 'B', 'C', 'D'], size=200),
            'Valor': np.random.randint(10, 100, size=200),
            'Data': pd.date_range(start='2023-01-01', periods=200, freq='D'),
        })
        return data

    df = generate_data()

    # Filtros
    st.sidebar.header("Filtros")
    categorias = st.sidebar.multiselect("Selecione Categorias", df['Categoria'].unique(), df['Categoria'].unique())
    data_inicio = st.sidebar.date_input("Data Início", df['Data'].min())
    data_fim = st.sidebar.date_input("Data Fim", df['Data'].max())

    # Filtrando os dados
    filtered_df = df[
    (df['Categoria'].isin(categorias)) &
    (df['Data'].between(pd.to_datetime(data_inicio), pd.to_datetime(data_fim)))
]

    # Gráficos
    col1, col2 = st.columns(2)

    # Gráfico de barras
    with col1:
        st.subheader("📊 Gráfico de Barras")
        fig, ax = plt.subplots()
        sns.barplot(data=filtered_df, x='Categoria', y='Valor', estimator=np.sum, ci=None, ax=ax)
        st.pyplot(fig)

    # Gráfico de linha
    with col2:
        st.subheader("📈 Gráfico de Linha")
        fig, ax = plt.subplots()
        df_line = filtered_df.groupby('Data').sum()
        ax.plot(df_line.index, df_line['Valor'], marker='o')
        ax.set_xlabel("Data")
        ax.set_ylabel("Valor")
        st.pyplot(fig)

    # Exibir a tabela dos dados filtrados
    st.subheader("📋 Dados Filtrados")
    st.dataframe(filtered_df)

elif pagina == "Upload":
    upload.upload()

elif pagina == "Sobre":
    st.title("Sobre o App")
    st.write("Este é um exemplo de app com múltiplas páginas usando Streamlit.")
