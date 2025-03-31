import streamlit as st
import requests
import config


def upload():
    st.title("Upload dos arquivos relacionados a NF")

    # Entrada para o usuário digitar informações
    nf = st.text_input("Digite o número da nf:")

    # Upload de arquivo
    uploaded_file = st.file_uploader(
        "Escolha um arquivo", type=["png", "jpg", "pdf"])

    # Botão de envio
    if st.button("Enviar"):
        if uploaded_file and nf:
            # Criando o payload multipart
            files = {
                "file": (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type)
            }

            data = {
                "os": nf,
                "latitude": 0,
                "longitude": 0,
                "uid": 1
            }
            headers = {
                # Enviando a API Key no cabeçalho
                "access_token": config.API_KEY
            }

            # Fazendo a requisição POST
            response = requests.post(config.API_URL, files=files,
                                     data=data, headers=headers)

            # Exibindo resposta
            if response.status_code == 200:
                st.success(
                    f"Upload realizado com sucesso!")
            else:
                st.error(
                    f"Erro no upload! Código: {response.status_code} - {response.text}")
        else:
            st.warning("Por favor, insira um nf e selecione um arquivo.")
