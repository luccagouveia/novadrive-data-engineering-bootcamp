# Bootcamp de Engenharia de Dados - Nova Drive Motors
- Este repositório contém o desenvolvimento do projeto de bootcamp para a Nova Drive Motors, focado na construção de um Data Warehouse (DW) completo para a área de Vendas.

# Sobre o Projeto
- A Nova Drive Motors é uma empresa fictícia do ramo automotivo que está crescendo rapidamente devido ao alto volume de carros vendidos nos últimos meses. O Diretor de Vendas Nacional procurou ajuda para estruturar os dados da empresa, pois atualmente só recebe planilhas pouco confiáveis da gerente de vendas.
Objetivo principal: Criar um pipeline de dados completo, desde a extração de dados de um banco operacional PostgreSQL até a disponibilização em uma camada analítica, fornecendo informações precisas para a área de vendas e gestores.

# Abordagem Diferenciada
- Este projeto segue o Bootcamp de Engenharia de Dados do Fernando Amaral (Udemy), mas com adaptações importantes para melhor aprendizado e desenvolvimento:
    Arquitetura Original do Bootcamp:
    PostgreSQL (Operacional) → AWS EC2 (Ubuntu/Docker/Airflow) → Snowflake (Stage) → dbt → Snowflake (Analítico)

# Minha Arquitetura Adaptada:
- VS Code + Docker + DevContainer → PostgreSQL (Operacional) → Airflow (Local) → Snowflake (Stage) → dbt → Snowflake (Analítico)

- Principais diferenças:

    Ambiente totalmente containerizado com Docker e DevContainer
    Desenvolvimento local no VS Code para facilitar debugging e aprendizado
    Configuração simplificada sem necessidade de AWS EC2
    Foco educacional com maior controle sobre cada etapa

# Arquitetura do Pipeline
- O fluxo de dados seguirá a seguinte arquitetura:

    mermaidflowchart LR
        A[PostgreSQL<br/>BD Operacional] --> B[Apache Airflow<br/>Orquestração]
        B --> C[Snowflake<br/>Stage Layer]
        C --> D[dbt<br/>Transformação]
        D --> E[Snowflake<br/>Analytic Layer]
        E --> F[Looker Studio<br/>Visualização]

    Tecnologias utilizadas:

        PostgreSQL: Banco de dados operacional (fonte)
        Apache Airflow: Orquestração de pipelines ETL
        Snowflake: Data Warehouse (Stage e Analytics)
        dbt: Transformação de dados e modelagem
        Looker Studio: Visualização e dashboards
        Docker: Containerização do ambiente


# Estrutura do Projeto
- novadrive-data-engineering-bootcamp/
    ├── .devcontainer/          # Configurações do ambiente Docker
    │   ├── devcontainer.json
    │   └── Dockerfile
    ├── airflow/              # Apache Airflow
    │   ├── dags/             # DAGs do Airflow
    │   ├── plugins/          # Plugins customizados
    │   ├── logs/             # Logs de execução
    │   └── docker-compose.yml
    ├── dbt/                  # Projeto dbt
    │   ├── models/           # Modelos de transformação
    │   ├── macros/           # Macros reutilizáveis
    │   └── dbt_project.yml
    ├── scripts/              # Scripts auxiliares
    │   └── explore_database_schema.py
    ├── docs/                 # Documentação
    ├── modeling.md           # Modelo dimensional detalhado
    └── README.md

# Como Executar o Projeto
- Pré-requisitos

    Docker Desktop instalado
    Visual Studio Code instalado
    Git instalado

- Passo a Passo para Iniciantes

    Clone o repositório:
    bashgit clone https://github.com/luccagouveia/novadrive-data-engineering-bootcamp.git
    cd novadrive-data-engineering-bootcamp

- Instale a extensão Dev Containers no VS Code:

    Abra o VS Code
    Vá em Extensions (Ctrl+Shift+X)
    Procure por "Dev Containers"
    Instale a extensão da Microsoft

- Abra o projeto no VS Code:
    bashcode .

- Inicie o ambiente containerizado:
    Uma notificação aparecerá: "Reopen in Container"
    Clique na notificação OU
    Use Ctrl+Shift+P e digite "Dev Containers: Reopen in Container"

- Aguarde a construção do container:
    O Docker irá baixar as imagens necessárias
    Isso pode levar alguns minutos na primeira vez

- Verifique se o ambiente está funcionando:
    bashpython --version
    pip list

# Etapas do Projeto
- Etapa 1: Ambiente de Desenvolvimento
    Configuração do Docker e DevContainer
    Ambiente Python com dependências
    Acesso ao banco de dados PostgreSQL

- Etapa 2: Exploração e Modelagem de Dados
    Análise exploratória do banco operacional
    Definição do modelo dimensional (Star Schema)
    Documentação das tabelas fato e dimensão

- Etapa 3: Configuração do Apache Airflow
    Setup do Airflow em container
    Configuração de conexões
    Criação das primeiras DAGs

- Etapa 4: Configuração do Snowflake
    Criação da conta Snowflake
    Configuração de databases e schemas
    Setup das conexões

- Etapa 5: Camada Stage no Snowflake
    Extração de dados via Airflow
    Carregamento na camada Stage
    Validação de qualidade dos dados

- Etapa 6: Camada Analítica com dbt
    Configuração do projeto dbt
    Implementação dos modelos dimensionais
    Testes e documentação

- Etapa 7: Visualização e Dashboards
    Conexão com Looker Studio
    Criação de dashboards executivos
    Validação com stakeholders

# Acessos para Teste e Validação
    1. Banco de Dados Operacional (Somente Leitura)
        bashpsql -h 159.223.187.110 -p 5432 -d novadrive -U etlreadonly

        Host: 
        Porta: 
        Database: 
        Usuário: 
        Senha: 

        2. Sistema de Vendas (Interface Web)
        Para inserir novos dados de teste:

        URL: http://143.244.215.137:3002/
        Login: vendedor1
        Senha:
        Consulta: http://143.244.215.137:3002/procura


# Modelo Dimensional
- Foi implementado um Esquema Estrela (Star Schema) otimizado para análises de vendas:

    Tabela Fato: Fato_Vendas
    Dimensões:

        Dim_Cliente - Informações dos clientes
        Dim_Veiculo - Catálogo de veículos
        Dim_Concessionaria - Rede de concessionárias
        Dim_Data - Dimensão temporal

# Documentação completa: modeling.md
- Contribuições
    Este é um projeto educacional, mas sugestões e melhorias são bem-vindas:

        Fork o projeto
        Crie uma branch para sua feature (git checkout -b feature/AmazingFeature)
        Commit suas mudanças (git commit -m 'Add some AmazingFeature')
        Push para a branch (git push origin feature/AmazingFeature)
        Abra um Pull Request

# Licença
- Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

# Sobre o Bootcamp
- Este projeto faz parte do Bootcamp de Engenharia de Dados ministrado por Fernando Amaral na plataforma Udemy. O curso     aborda as principais tecnologias e práticas do mercado de dados.
    Link do curso: Bootcamp Engenharia de Dados - Fernando Amaral

# Contato
    Desenvolvedor: Lucas A. Gouveia
    Cargo: Aspirante a Engenheiro de Dados, atualmente Diretor Técnico na Área de Dados
    LinkedIn: https://www.linkedin.com/in/lucas-gouveia-447094ab/
    GitHub: https://github.com/luccagouveia

# Recursos Úteis
    Documentação dbt
    Airflow Documentation
    Snowflake Documentation
    Docker Documentation