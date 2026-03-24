# Studio de Processamento de Imagens 2026

Repositório colaborativo da disciplina de Processamento de Imagens — UFPA 2026.

## Visão Geral

Este projeto é um **Studio de Processamento de Imagens** interativo construído com Python e Streamlit. A arquitetura é baseada em **plugins**, permitindo que dezenas de alunos contribuam simultaneamente sem causar conflitos de merge.

## 🎮 Gamificação e Recompensas

Para tornar o nosso desenvolvimento mais dinâmico e simular um ambiente de engenharia de software de alto nível, este repositório conta com um sistema de gamificação. 

As suas contribuições e Pull Requests (PRs) não valem apenas nota, mas também **Badges (Medalhas)** de prestígio. 

**Como funciona?**
1. Você abre um Pull Request com o seu plugin ou melhoria.
2. O professor faz o *Code Review*. Se o seu trabalho se destacar em alguma área específica, o professor concederá uma badge diretamente nos comentários da sua PR.
3. Todo domingo à noite, nosso robô invisível (GitHub Actions) varre o repositório, contabiliza as badges e atualiza o **Hall da Fama** abaixo.

**As Badges que você pode conquistar:**
* 🤝 **O Salvador da Pátria:** Ajudou os colegas em discussões, revisões ou resolveu bloqueios da turma.
* 🐛 **Bug Catcher:** Encontrou e corrigiu um erro crítico no software.
* ⭐ **Código de Ouro:** Escreveu um código limpo, elegante, bem documentado e otimizado.
* 🧠 **Lógica Brilhante:** Implementou um algoritmo complexo de forma excepcional.
* 🎨 **UI/UX Master:** Criou uma interface ou controle no Streamlit absurdamente fácil e bonito de usar.
* 💻 **Enter the Matrix:** Dominou a manipulação de matrizes, tensores e álgebra linear usando NumPy/OpenCV.

---

## 🏆 Hall da Fama - Placar Semanal da Turma

> 🤖 *O robô está aquecendo os motores... O primeiro placar oficial será atualizado neste domingo à noite!*

### ⌨️ Jack Bauer do Código
*Quem mais codificou na semana (Volume total de linhas mescladas)*

![Jack Bauer](/.github/images/memes/image_5.png)

🥇 **Ainda não há registros. Faça o primeiro PR!** (0 linhas mescladas)

---

### 🤝 John Coffey do grupo
*Quem mais ganhou a badge 🤝 O Salvador da Pátria*

![John Coffey](/.github/images/memes/image_6.png)

🥇 **Ainda não há registros. Ajude um colega!** (0 badges acumuladas)

---

### 🐛 Pokemon Bug Catcher
*Quem mais ganhou a badge 🐛 Bug Catcher*

![Bug Catcher](/.github/images/memes/image_7.png)

🥇 **Ainda não há registros. Encontre um erro!** (0 badges acumuladas)

---

### ⭐ Patrick Bateman da turma
*Quem mais ganhou a badge ⭐ Código de Ouro*

![Patrick Bateman](/.github/images/memes/image_8.png)

🥇 **Ainda não há registros. Escreva um código impecável!** (0 badges acumuladas)

---

### 🧠 John Nash da turma
*Quem mais ganhou a badge 🧠 Lógica Brilhante*

![John Nash](/.github/images/memes/image_9.png)

🥇 **Ainda não há registros. Mostre sua genialidade!** (0 badges acumuladas)

---

### 🎨 Da Vinci do Front-end
*Quem mais ganhou a badge 🎨 UI/UX Master*

![Da Vinci](/.github/images/memes/image_10.png)

🥇 **Ainda não há registros. Capriche na interface!** (0 badges acumuladas)

---

### 💻 Neo da turma
*Quem dominou o uso de matrizes e álgebra linear (Badge 💻 Enter the Matrix)*

![Neo](/.github/images/memes/image_11.png)

🥇 **Ainda não há registros. Manipule a matriz!** (0 badges acumuladas)

---

## Arquitetura de Plugins

```
.
├── app.py                        # Ponto de entrada da aplicação
├── requirements.txt              # Dependências do projeto
├── core/
│   └── __init__.py               # Módulo central (lógicas compartilhadas)
└── plugins/
    ├── __init__.py               # Torna plugins/ um módulo Python
    └── exemplo_filtro_cinza.py   # Plugin de exemplo
```

O `app.py` carrega dinamicamente todos os arquivos `.py` dentro da pasta `plugins/` e os exibe como opções no menu lateral. Cada plugin deve exportar uma função `run(imagem_numpy)` que recebe e retorna uma imagem no formato NumPy (RGB).

## Como Executar

1. Instale as dependências:

```bash
pip install -r requirements.txt
```

2. Inicie a aplicação:

```bash
streamlit run app.py
```

## Como Criar um Plugin

Siga os passos abaixo para criar seu plugin e fazê-lo aparecer automaticamente na interface:

### Passo 1 — Crie seu arquivo na pasta `plugins/`

Crie um arquivo com um nome descritivo, por exemplo:

```
plugins/seu_nome_filtro_exemplo.py
```

> ⚠️ **Atenção:** use apenas letras minúsculas, números e underscores (`_`). Não use espaços ou caracteres especiais.

### Passo 2 — Implemente a função `run`

Seu arquivo **obrigatoriamente** deve conter uma função chamada `run(imagem_numpy)`:

```python
import cv2
import streamlit as st

def run(imagem_numpy):
    """
    Descrição do que seu plugin faz.

    Parâmetros:
        imagem_numpy: imagem de entrada no formato NumPy (RGB).

    Retorna:
        imagem_resultado: imagem processada no formato NumPy (RGB).
    """
    # Exemplo: adicionar um slider na barra lateral
    valor = st.sidebar.slider("Meu parâmetro", 0, 100, 50)

    # Processar a imagem (exemplo: inverter as cores)
    imagem_resultado = cv2.bitwise_not(imagem_numpy)

    return imagem_resultado
```

### Passo 3 — Teste seu plugin

Execute a aplicação e selecione seu plugin no menu lateral. Se houver algum erro no seu código, a interface exibirá uma mensagem de erro amigável sem derrubar a aplicação.

### Passo 4 — Abra um Pull Request

Envie apenas o seu arquivo `plugins/seu_nome_filtro_exemplo.py`. Não modifique `app.py`, `requirements.txt` ou outros arquivos de configuração.

## Regras e Boas Práticas

- Trabalhe **apenas** dentro da pasta `plugins/`.
- A função `run` deve sempre retornar uma imagem NumPy no formato RGB.
- Use `st.sidebar.*` para adicionar controles interativos (sliders, checkboxes, etc.).
- Escreva comentários e nomes de variáveis em **Português do Brasil (pt-BR)**.
- Não adicione dependências externas sem aprovação do professor.

## Dependências

| Biblioteca              | Uso                              |
|-------------------------|----------------------------------|
| streamlit               | Interface web interativa         |
| opencv-python-headless  | Processamento de imagens         |
| numpy                   | Manipulação de arrays            |
| Pillow                  | Leitura e conversão de imagens   |
