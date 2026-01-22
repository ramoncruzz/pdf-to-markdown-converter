# Prompts para Reprodução e Evolução do Projeto

Este arquivo contém dois prompts detalhados. O primeiro serve para gerar o projeto no estado atual (CLI com OCR). O segundo instrui a transformação deste projeto em uma API Web.

---

## 1. Prompt para Gerar o Projeto Atual (CLI + OCR)

**Copie e cole este prompt para recriar o projeto atual:**

> "Atue como um Engenheiro de Software Sênior especialista em Python. Crie um projeto CLI profissional para converter arquivos PDF em Markdown.
>
> **Requisitos do Projeto:**
> 1.  **Core**: Utilize a biblioteca `PyMuPDF` (fitz) para a extração principal de texto.
> 2.  **Estrutura**: Organize o código como um pacote Python (diretório `src`, `main.py`, etc.), pronto para expansão.
> 3.  **OCR**: Implemente suporte a OCR (Optical Character Recognition) usando `pytesseract` e `Pillow`. O sistema deve detectar blocos de imagem dentro do PDF, extraí-los, melhorar a resolução (300 DPI) e aplicar OCR para extrair o texto contido. Implemente fallback de linguagem (tente 'por+eng', se falhar use 'eng').
> 4.  **CLI**: Use `argparse` para receber o arquivo de entrada, opcionalmente o arquivo de saída, e um argumento `--type` (opções: `txt`, `img`). Se `type` não for informado, o padrão deve ser `txt`.
>     -   **Lógica**: Se `type=img`, force a conversão via OCR (renderizar página como imagem -> OCR). Se `type=txt`, use a extração direta de texto do PyMuPDF.
> 5.  **Empacotamento**: Crie um arquivo `pyproject.toml` configurado para que o projeto possa ser instalado globalmente via `pip` (ex: `pip install .`) e executado com um comando próprio (ex: `pdf2md`).
> 6.  **Documentação**: Gere um `README.md` com instruções detalhadas de instalação (global e local), uso e dependências (como instalar o Tesseract no sistema)."

---

## 2. Prompt para Evolução Web (Backend RESTful + Docker)

**Copie e cole este prompt para criar a versão Web do projeto:**

> "Atue como um Engenheiro de Software Sênior. Baseado no projeto de conversão de PDF para Markdown existente (que usa PyMuPDF e Tesseract), crie um novo projeto **Backend RESTful** em Python (sugiro FastAPI ou Flask) que funcione como uma API, sem frontend.
>
> **Requisitos Funcionais da API:**
> 1.  **Rota 1 (Upload)**:
>     -   Método: `POST /convert/upload`
>     -   Entrada: Arquivo binário (multipart/form-data) e um campo opcional `type` (valores: `txt` ou `img`, padrão `txt`).
>     -   Ação: Processar o PDF recebido utilizando a lógica de conversão. Se `type=img`, usar OCR. Se `type=txt`, usar extração de texto.
>     -   Saída: Retornar o conteúdo convertido em texto/Markdown diretamente no corpo da resposta (Content-Type: text/markdown ou text/plain).
>
> 2.  **Rota 2 (Link)**:
>     -   Método: `POST /convert/link`
>     -   Entrada: JSON contendo uma URL e opcionalmente o tipo (ex: `{"url": "http://exemplo.com/arquivo.pdf", "type": "txt"}`). Se `type` não enviado, assumir `txt`.
>     -   Ação: Baixar o arquivo temporariamente, processá-lo conforme o `type` informado e converter.
>     -   Saída: Retornar o conteúdo convertido em texto/Markdown.
>
> **Requisitos de Infraestrutura e Documentação:**
> -   **Docker**: Crie um `Dockerfile` otimizado para a aplicação (incluindo dependências do sistema como `tesseract-ocr`).
> -   **Docker Compose**: Crie um arquivo `docker-compose.yml` para facilitar a subida do serviço.
> -   **README.md**: Gere um arquivo README completo contendo:
>     -   Como executar a aplicação localmente (com `venv`).
>     -   Como construir a imagem Docker.
>     -   Como executar usando Docker e Docker Compose.
>     -   Exemplos de chamadas cURL para testar as rotas.
>
> **Requisitos Técnicos:**
> -   Reaproveite a lógica de conversão (PyMuPDF + Tesseract).
> -   Trate erros adequadamente (ex: download falhou, arquivo inválido).
> -   Não mantenha estado; processe em memória ou use arquivos temporários que são limpos após o uso."
