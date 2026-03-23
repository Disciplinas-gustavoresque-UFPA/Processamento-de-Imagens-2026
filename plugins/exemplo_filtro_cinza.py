import cv2
import streamlit as st


def run(imagem_numpy):
    """
    Converte a imagem para tons de cinza.

    Parâmetros:
        imagem_numpy: imagem de entrada no formato NumPy (RGB).

    Retorna:
        imagem_resultado: imagem em tons de cinza no formato NumPy (RGB).
    """
    # Slider na sidebar — exemplo de como adicionar controles interativos
    intensidade = st.sidebar.slider(
        "Intensidade do cinza",
        min_value=0,
        max_value=100,
        value=100,
        step=1,
        help="Controla a intensidade da conversão para tons de cinza (0 = original, 100 = cinza total).",
    )

    # Conversão para tons de cinza usando OpenCV
    imagem_cinza = cv2.cvtColor(imagem_numpy, cv2.COLOR_RGB2GRAY)

    # Converte de volta para 3 canais (RGB) para exibição padronizada
    imagem_cinza_rgb = cv2.cvtColor(imagem_cinza, cv2.COLOR_GRAY2RGB)

    # Aplica a intensidade: mistura a imagem original com a versão em cinza
    fator = intensidade / 100.0
    imagem_resultado = cv2.addWeighted(imagem_numpy, 1 - fator, imagem_cinza_rgb, fator, 0)

    return imagem_resultado
