# Gerenciador de Contatos - Flask App
## Uma imagem vale mais que mil palavras...
| ![Imagem 1](https://github.com/user-attachments/assets/fca18e37-1eaf-4f85-9657-adec11c011ad) | ![Imagem 2](https://github.com/user-attachments/assets/f8a53efc-8832-4798-94cc-66552e801fad) |
|---------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| Tela Inicial                                                                          | Modal para adição de novo contato                                                                           |

## Vídeo sobre a Publicação

Você pode assistir à publicação incorporada no LinkedIn [clicando aqui](https://www.linkedin.com/embed/feed/update/urn:li:ugcPost:7025985433931034624).

Este projeto é uma aplicação web simples para gerenciamento de contatos, construída com Flask, SQLAlchemy e Materialize CSS para o frontend.

## Funcionalidades

- **Adicionar Contatos:** Crie novos contatos com nome, e-mail, celular, tags e links.
- **Listar Contatos:** Exibe todos os contatos cadastrados.
- **Deletar Contatos:** Permite remover contatos da lista.

## Tecnologias Utilizadas

- **Python**: Linguagem principal para o backend.
- **Flask**: Framework web para construir a aplicação.
- **SQLAlchemy**: ORM (Object Relational Mapper) usado para manipulação de dados com SQLite.
- **SQLite**: Banco de dados utilizado para armazenar os contatos.
- **Materialize CSS**: Framework CSS utilizado para estilização da interface.

## Como Executar o Projeto

### Pré-requisitos

- Python 3.x instalado.
- Pip (gerenciador de pacotes do Python) instalado.

### Passos para Execução

1. Clone este repositório em sua máquina (ou navegue até o diretório onde o projeto está localizado):

   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
2. Acesse o diretório do projeto:
    ```bash
    cd seu-repositorio

3. Crie um ambiente virtual (opcional, mas recomendado):
    ```bash
    python -m venv venv

4. Ative o ambiente virtual:
   
   - No Windows:
     ```bash
     venv\Scripts\activate

   - No Linux/Mac:
     ```bash
     source venv/bin/activate

5. Instale as dependências:
    ```bash
    pip install flask sqlalchemy

6. Execute a aplicação:
    ```bash
    python main.py

7. Acesse a aplicação no navegador:
    ```bash
    http://127.0.0.1:5000/
    
### Arquivo `main.py`

O arquivo `main.py` contém as rotas e a lógica de manipulação dos contatos. Ele inclui:

- **Modelo Contato:** Definição da tabela `contatos` com SQLAlchemy.
- **Funções para criar, deletar e buscar contatos:** Integração com o banco de dados SQLite usando SQLAlchemy.
- **Rotas:**
  - `/`: Rota principal que lista os contatos.
  - `/salvar_contato`: Rota para salvar novos contatos (usando método POST).
  - `/deletar_contato`: Rota para deletar contatos (usando método POST).

### Frontend

O frontend foi construído usando Materialize CSS para proporcionar uma interface amigável e responsiva.

### Melhorias Futuras

- Adicionar funcionalidade de edição de contatos.
- Melhorar a validação de dados no frontend.
- Adicionar filtros de busca e paginação.

### Contribuições

Sinta-se à vontade para fazer um fork deste projeto e abrir pull requests com melhorias ou novas funcionalidades.

### Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
