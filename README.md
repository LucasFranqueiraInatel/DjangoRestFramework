# DjangoRestFramework

Este projeto é uma aplicação desenvolvida com Django e Django REST Framework, destinada a [descreva brevemente o propósito ou funcionalidade principal do seu projeto].

## Tecnologias Utilizadas

- **Django**: Framework web de alto nível que incentiva o desenvolvimento rápido e um design limpo e pragmático.&#8203;:contentReference[oaicite:3]{index=3}
- **Django REST Framework**: :contentReference[oaicite:4]{index=4}&#8203;:contentReference[oaicite:5]{index=5}

## Instalação

Siga os passos abaixo para configurar e executar o projeto localmente:

1. **Clone este repositório**:

    ```bash
    git clone https://github.com/LucasFranqueiraInatel/DjangoRestFramework.git
    ```

2. **Navegue até o diretório do projeto**:

    ```bash
    cd DjangoRestFramework
    ```

3. **Crie um ambiente virtual** (recomendado):

    ```bash
    python -m venv venv
    venv/bin/activate
    ```

4. **Instale as dependências**:

    ```bash
    pip install -r requirements.txt
    ```

5. **Execute as migrações do banco de dados**:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```
6. **Populando o banco de dados**:

    ```bash
    python manage.py populate
    ```

7. **Inicie o servidor de desenvolvimento**:

    ```bash
    python manage.py runserver
    ```