<h1 align="center">NLW Expert trilha de Python da Rocketseat</h1>

<p align="center">
  <a href="#-tecnologias">Tecnologias</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-projeto">Projeto</a>&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;
  <a href="#-principais-bibliotecas">Principais Bibliotecas</a>
  <a href="#-Para-executar-o-projeto">Para executar o projeto</a>
</p>

<br>

<p align="center">
  <img alt="perfilSiteMinimalistico" src=".github/7890129310232.png" width="40%">
</p>

## 🚀 Tecnologias

Esse projeto foi desenvolvido com as seguintes tecnologias:

- Python
- Flask

## 📚 Principais Bibliotecas

- Pylint
- python-barcode
- Cerberus
- pre-commit
- Virtualenv
- Pytest


## 💻 Projeto

Desenvolvimento de uma aplicação back-end em Python, utilizando Flask como framework, preparação de
ambiente e boas práticas de projeto com Virtualenv, Pylint e versionamento de código usando pre-commit, criação de
código de barras com python-barcode e testes com Pytest.

## 👨‍💻 Para executar o projeto

1. Clone o repositório: `git clone https://github.com/davioliveiraes/nlw-python-expert.git`
2. Entre na pasta do projeto: `cd nlw-python-expert`
3. Ative o ambiente virtual: `.venv\Scripts\activate` (windows) 
4. Instale as dependências com: `pip install -r requirements.txt`
5. Execute o programa: `python run.py`
6. Pode baixar o `Postman`, método `POST`, link `http://localhost:3000/create_tag`
7. No body -> raw: `{"product_code": "7891230910285"}` -> Send
8. O projeto vai/deve funcionar: `{
  "data": {
    "count": 1,
    "path": "7890129310232.png",
    "type": "Tag Image"
  }
} `
9. Condição de erro - Exemplo: `{"product_code": 7891230910285}` Saída: `{
    "errors": [
        {
            "detail": {
                "product_code": [
                    "must be of string type"
                ]
            },
            "title": "UnprocessableEntity"
        }
    ]
}`
