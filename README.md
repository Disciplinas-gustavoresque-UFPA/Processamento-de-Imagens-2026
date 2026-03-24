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

Recomendamos fortemente o uso de um **Ambiente Virtual (venv)** para instalar o projeto. Isso evita conflitos com outras bibliotecas do seu computador e previne erros de permissão (especialmente no Windows).

### Passo 1 — Criar o ambiente virtual
Abra o terminal na pasta raiz do projeto e rode:

```bash
python -m venv venv
```

### Passo 2 — Ativar o ambiente virtual

**No Windows (Command Prompt ou PowerShell):**
```bash
.\venv\Scripts\activate
```
> ⚠️ **Aviso (Erro no PowerShell):** Se você receber um erro vermelho dizendo que *"a execução de scripts foi desabilitada"*, significa que o seu Windows está bloqueando o terminal por segurança. Para resolver, rode o comando abaixo uma única vez, digite `S` para confirmar e tente ativar o ambiente de novo:
> `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`

**No Linux ou Mac:**
```bash
source venv/bin/activate
```

*(Você saberá que deu certo quando o nome `(venv)` aparecer em verde no início da linha do seu terminal).*

### Passo 3 — Instalar as dependências
Com o ambiente ativado, instale as bibliotecas necessárias para o projeto rodar:

```bash
pip install -r requirements.txt
```

### Passo 4 — Iniciar a aplicação
Por fim, suba o servidor local do Streamlit:

```bash
streamlit run app.py
```

## 📌 Fluxo de Trabalho (Issues e Pull Requests)

Para manter o repositório organizado e evitar que duas pessoas façam o mesmo trabalho, siga um dos fluxos abaixo:

## 📌 Fluxo de Trabalho (Issues e PRs)

Para manter o repositório organizado e evitar que duas pessoas façam o mesmo trabalho, siga um dos fluxos abaixo:

### Fluxo 1: Resolvendo uma Tarefa do Professor
1. **Escolha uma Issue e assuma a tarefa:** Vá na aba *Issues* do repositório, escolha uma tarefa aberta pelo professor e **deixe um comentário com o seu usuário (ex: "Vou desenvolver este plugin - @seu-nick")** para avisar à turma que você pegou a tarefa.
2. **Crie a Branch:** Crie uma branch diretamente associada a essa Issue (ex: `seu-nick/feature/filtro-xyz`).
3. **Faça Commits Atômicos:** Recomendamos fortemente a prática de commits atômicos. Cada commit deve ter um objetivo único e bem definido (fazer apenas uma coisa por vez), acompanhado de uma mensagem clara que explique exatamente o que foi alterado.
4. **Abra um Draft PR:** Com o seu primeiro commit feito, abra um Pull Request em modo **Draft** (Rascunho). Isso reforça aos colegas que você já está ativamente trabalhando nela.
5. **Desenvolva:** Continue fazendo seus commits atômicos normalmente na sua branch.
6. **Revisão e Merge:** Quando terminar, tire o PR do modo Draft e solicite a revisão (Review) do professor (`@gustavoresque`) para que o código seja integrado.

### Fluxo 2: Propondo uma Nova Ideia ou Correção
1. **Crie uma Issue:** Teve uma ideia legal para um plugin novo ou encontrou um bug? Abra uma nova Issue descrevendo a sua proposta. **Não esqueça de colocar o seu usuário (`@seu-nick`) na descrição** para registrar a autoria da ideia.
2. **Chame o Professor:** Mencione o professor (`@gustavoresque`) na descrição da Issue para avaliação.
3. **Aprovação:** O professor vai avaliar, refinar o objetivo se necessário, e aprovar a ideia.
4. **Mão na Massa:** Com a Issue aprovada, siga exatamente os mesmos passos do Fluxo 1 (crie a branch, faça commits atômicos, abra o Draft PR, desenvolva e peça revisão).

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
