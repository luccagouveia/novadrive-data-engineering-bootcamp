# Bootcamp de Engenharia de Dados - NovaDrive Motors

Este repositório contém o desenvolvimento do projeto de bootcamp para a **NovaDrive Motors**, focado na construção de um Data Warehouse (DW) para a área de Vendas.

O objetivo é criar um pipeline de dados completo, desde a extração de dados de um banco operacional até a disponibilização em uma camada analítica para os gestores.

## 🚀 Arquitetura Proposta

O fluxo de dados seguirá a seguinte arquitetura:

**Postgres (BD Operacional) → Airflow (Orquestração) → Snowflake (BD Stage) → dbt (Transformação) → Snowflake (BD Analítico)**

---

## Fase 1: Ambiente de Desenvolvimento e Acesso aos Dados

Esta primeira fase do projeto estabelece a base para todo o desenvolvimento futuro.

### Como Iniciar o Ambiente:
1.  Instale o Docker e o VS Code com a extensão Dev Containers.
2.  Clone este repositório.
3.  Abra a pasta do projeto no VS Code e clique em "Reopen in Container".

### Status da Conexão:
- [x] Acesso ao banco de dados PostgreSQL remoto validado.
- [x] Credenciais gerenciadas como variáveis de ambiente.

---

## Próximas Etapas do Projeto

- [ ] **Etapa 3:** Configurar o Apache Airflow.
- [ ] **Etapa 4:** Configurar o Snowflake.
- [ ] **Etapa 5:** Criar a camada Stage no Snowflake via Airflow.
- [ ] **Etapa 6:** Criar e configurar a camada analítica com dbt.
