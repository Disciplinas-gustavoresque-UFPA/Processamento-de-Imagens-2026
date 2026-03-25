import streamlit as st
import numpy as np
from PIL import Image
import importlib
import pkgutil
import os

# Adiciona função de resetar/limpar as imagens no app
def limpar_tela():
    """Limpa as imagens da sessão e reseta o file uploader."""
    st.session_state.imagem_original = None
    st.session_state.imagem_atual = None
    # Deleta a chave do uploader para forçar o componente a esvaziar
    if "imagem_carregada" in st.session_state:
        del st.session_state["imagem_carregada"]

# Configuração da página
st.set_page_config(
    page_title="Studio de Processamento de Imagens",
    page_icon="🖼️",
    layout="wide",
)

# Inicialização do estado da sessão
if "imagem_original" not in st.session_state:
    st.session_state.imagem_original = None

if "imagem_atual" not in st.session_state:
    st.session_state.imagem_atual = None

# Barra lateral: upload de imagem
st.sidebar.title("🖼️ Studio de Processamento de Imagens")
st.sidebar.markdown("---")

arquivo_enviado = st.sidebar.file_uploader(
    "Carregar imagem",
    type=["jpg", "jpeg", "png"],
    help="Selecione uma imagem nos formatos JPG ou PNG.",
    # Adiciona uma chave para realizar a lógica de resetar imagem
    key="imagem_carregada"
)

if arquivo_enviado is not None:
    imagem_pil = Image.open(arquivo_enviado).convert("RGB")
    imagem_numpy = np.array(imagem_pil)
    st.session_state.imagem_original = imagem_numpy
    st.session_state.imagem_atual = imagem_numpy

# Botão de resetar a imagem
# O botão só é mostrado caso haja uma imagem carregada
if st.session_state.imagem_original is not None:
    st.sidebar.button("Remover imagem", on_click=limpar_tela, use_container_width=True)

# Descoberta dinâmica de plugins
pasta_plugins = os.path.join(os.path.dirname(os.path.abspath(__file__)), "plugins")

nomes_plugins = []
for info_modulo in pkgutil.iter_modules([pasta_plugins]):
    if not info_modulo.name.startswith("_"):
        nomes_plugins.append(info_modulo.name)

st.sidebar.markdown("---")

if nomes_plugins:
    plugin_selecionado = st.sidebar.selectbox(
        "Selecionar plugin",
        options=nomes_plugins,
        format_func=lambda nome: nome.replace("_", " ").title(),
    )
else:
    plugin_selecionado = None
    st.sidebar.info("Nenhum plugin encontrado na pasta plugins/.")

# Área principal
st.title("Studio de Processamento de Imagens")

if st.session_state.imagem_original is None:
    st.info("👈 Faça o upload de uma imagem na barra lateral para começar.")
else:
    coluna_original, coluna_resultado = st.columns(2)

    with coluna_original:
        st.subheader("Imagem Original")
        st.image(st.session_state.imagem_original, use_container_width=True)

    with coluna_resultado:
        st.subheader("Resultado do Plugin")

        if plugin_selecionado is not None:
            try:
                modulo_plugin = importlib.import_module(f"plugins.{plugin_selecionado}")
                if hasattr(modulo_plugin, "run"):
                    imagem_resultado = modulo_plugin.run(st.session_state.imagem_original.copy())
                    if imagem_resultado is not None:
                        st.session_state.imagem_atual = imagem_resultado
                        st.image(imagem_resultado, use_container_width=True)
                    else:
                        st.warning("O plugin não retornou nenhuma imagem.")
                else:
                    st.error(
                        f"O plugin '{plugin_selecionado}' não possui uma função `run(imagem_numpy)`. "
                        "Verifique a implementação."
                    )
            except Exception as erro:
                st.error(
                    f"Erro ao executar o plugin '{plugin_selecionado}': {erro}\n\n"
                    "Verifique o código do plugin e tente novamente."
                )
        else:
            st.image(st.session_state.imagem_original, use_container_width=True)
