# Bootcamp de Engenharia de Dados - Nova Drive Motors

Este repositório contém o desenvolvimento do projeto de bootcamp para a **Nova Drive Motors**, focado na construção de um Data Warehouse (DW) para a área de Vendas.

O objetivo é criar um pipeline de dados completo, desde a extração de dados de um banco operacional até a disponibilização em uma camada analítica para os gestores.

## 🚀 Arquitetura Proposta

O fluxo de dados seguirá a seguinte arquitetura:

**Postgres (BD Operacional) → Airflow (Orquestração) → Snowflake (BD Stage) → dbt (Transformação) → Snowflake (BD Analítico)**

---

## 📂 Estrutura do Projeto

-   `.devcontainer/`: Configurações do ambiente de desenvolvimento Docker.
-   `airflow/`: Arquivos do Apache Airflow (DAGs, plugins, logs).
-   `dbt/`: Projeto dbt para a camada de transformação.
-   `scripts/`: Scripts de apoio (como a análise exploratória).
-   `modeling.md`: Documentação detalhada do modelo dimensional.

---

## 🛠️ Fase 1: Ambiente de Desenvolvimento

Esta fase estabelece a base para todo o desenvolvimento, garantindo um ambiente de trabalho consistente e validando o acesso à fonte de dados.

### Como Iniciar o Ambiente:
1.  Instale o [Docker Desktop](https://www.docker.com/products/docker-desktop/ ) e o [Visual Studio Code](https://code.visualstudio.com/ ).
2.  Instale a extensão [Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers ) da Microsoft no VS Code.
3.  Clone este repositório: `git clone https://github.com/luccagouveia/novadrive-data-engineering-bootcamp.git`
4.  Abra a pasta do projeto no VS Code.
5.  Clique na notificação **"Reopen in Container"** que aparecerá no canto inferior direito.

---

## 📊 Fase 2: Exploração e Modelagem de Dados

Nesta fase, analisamos o banco de dados operacional para entender a estrutura dos dados e definimos o modelo do nosso Data Warehouse.

### 1. Análise Exploratória
-   Um script Python (`scripts/explore_database_schema.py` ) foi criado para se conectar ao banco de dados e extrair metadados das tabelas principais (`clientes`, `vendas`, etc.).
-   O script analisa a contagem de linhas, a estrutura das colunas e uma amostra dos dados.

### 2. Modelo Dimensional
-   Foi definido um **Esquema Estrela (Star Schema)** para o DW.
-   **Tabela Fato:** `Fato_Vendas`
-   **Tabelas de Dimensão:** `Dim_Cliente`, `Dim_Veiculo`, `Dim_Concessionaria`, `Dim_Data`.
-   A documentação completa do modelo está no arquivo **[modeling.md](./modeling.md)**.

---

## 🧪 Acessos para Teste e Validação

Para simular o ambiente real e validar o pipeline, os seguintes acessos podem ser utilizados:

### 1. Banco de Dados Operacional (Leitura)
-   **Host:** ``
-   **Porta:** ``
-   **Banco de Dados:** ``
-   **Usuário:** ``
-   **Senha:** ``

### 2. Sistema de Vendas (Inserção de Dados)
É possível inserir novos dados de vendas através da interface web, que se refletirão no banco de dados acima.
-   **URL:** ``
-   **Login:** ``
-   **Senha:** ``
-   **Consulta por ID:** ``

---

## ⏩ Próximas Etapas do Projeto

-   [ ] **Etapa 3:** Configurar o Apache Airflow.
-   [ ] **Etapa 4:** Configurar o Snowflake.
-   [ ] **Etapa 5:** Criar a camada Stage no Snowflake via Airflow.
-   [ ] **Etapa 6:** Criar e configurar a camada analítica com dbt.
