# Modelagem Dimensional do Data Warehouse de Vendas

Esta documentação descreve o modelo dimensional adotado para o Data Warehouse (DW) da área de Vendas da NovaDrive Motors. O objetivo é fornecer uma estrutura otimizada para consultas analíticas e relatórios de Business Intelligence.

## Modelo Escolhido: Esquema Estrela (Star Schema)

Foi adotado um **Esquema Estrela** clássico, composto por uma tabela Fato central e múltiplas tabelas de Dimensão. Este modelo é ideal por sua simplicidade, performance de consulta e facilidade de entendimento pelos usuários de negócio.

### Visualização do Modelo
---
|                     +---------------------+
|                     |    Dim_Cliente      |
|                     +---------------------+
|                     | cliente_id (PK)     |
|                     | nome_cliente        |
|                     | email_cliente       |
|                     | cidade_cliente      |
|                     +---------------------+
|                               |
|                               |
+---------------------+         |           +-------------------------+
|    Dim_Veiculo      | <-------+-------->  |      Fato_Vendas        |
+---------------------+         |           +-------------------------+
| veiculo_id (PK)     |         |           | sk_venda (PK)           |
| modelo              |         |           | cliente_id (FK)         |
| ano                 |         |           | veiculo_id (FK)         |
| tipo_motor          | <-------+-------->  | concessionaria_id (FK)  |
+---------------------+         |           | data_id (FK)            |
|                               |           | valor_pago (Métrica)    |                 
|                               |           | quantidade (Métrica)    |                    
|                               |           +-------------------------+
|                    +---------------------+             |       +-----------------------+
|                    | Dim_Concessionaria  |             ------- |      Dim_Data         |
|                    +---------------------+                     +-----------------------+
|                    | concessionaria_id(PK)                     | data_id (PK)          |
|                    | nome_concessionaria |                     | data_completa         |
|                    | cidade              |                     | dia_semana, mes, ano  |
|                    | estado              |                     | trimestre             |
|                    +---------------------+                     +-----------------------+
---

## Detalhamento das Tabelas

### 1. Tabela Fato: `Fato_Vendas`
*   **Propósito:** Armazena os eventos de negócio mensuráveis.
*   **Granularidade:** Cada linha representa uma única venda de um veículo.
*   **Colunas:**
    *   `sk_venda` (Surrogate Key): Chave primária única da tabela fato.
    *   `cliente_id` (Foreign Key): Referencia `Dim_Cliente`.
    *   `veiculo_id` (Foreign Key): Referencia `Dim_Veiculo`.
    *   `concessionaria_id` (Foreign Key): Referencia `Dim_Concessionaria`.
    *   `data_id` (Foreign Key): Referencia `Dim_Data`.
    *   `valor_pago` (Métrica): O valor monetário da transação.
    *   `quantidade` (Métrica): O número de unidades vendidas (neste caso, será sempre 1).

### 2. Tabelas de Dimensão
Fornecem o contexto descritivo ("quem, o quê, onde, quando") para os fatos.

*   **`Dim_Cliente`**
    *   **Descrição:** Atributos do cliente que realizou a compra.
    *   **Exemplos de Colunas:** `nome_cliente`, `email`, `cidade`, `estado`, `faixa_etaria`.

*   **`Dim_Veiculo`**
    *   **Descrição:** Atributos do veículo vendido.
    *   **Exemplos de Colunas:** `modelo`, `ano`, `cor`, `tipo_motor`, `categoria`.

*   **`Dim_Concessionaria`**
    *   **Descrição:** Atributos da loja onde a venda ocorreu.
    *   **Exemplos de Colunas:** `nome_concessionaria`, `cidade`, `estado`, `regiao`.

*   **`Dim_Data`**
    *   **Descrição:** Atributos de tempo para análise de sazonalidade.
    *   **Exemplos de Colunas:** `data_completa` (ex: 2025-08-19), `dia_da_semana`, `mes`, `nome_mes`, `trimestre`, `ano`, `flag_feriado`.
