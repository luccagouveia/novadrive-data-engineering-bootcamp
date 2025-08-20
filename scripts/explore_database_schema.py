# Comando para executar este script: '/usr/local/bin/python /workspace/scripts/explore_database_schema.py'
"""
Script para realizar uma análise exploratória focada em tabelas específicas de um banco de dados PostgreSQL.
Este script ignora outras tabelas que não sejam relevantes para a análise de Vendas.
"""

import os
import subprocess

# --- CONFIGURAÇÕES ---
# Lista das tabelas que são relevantes para a análise de Vendas.
# Vamos ignorar qualquer outra tabela que possa existir no banco.
TABELAS_DE_INTERESSE = [
    "clientes",
    "concessionarias",
    "veiculos",
    "vendas"
]

# Número de linhas de amostra para buscar de cada tabela
SAMPLE_ROWS = 3

# Carrega as credenciais do ambiente
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

def run_psql_command(command: str) -> str:
    """
    Executa um único comando psql e retorna sua saída como string.
    Lança uma exceção em caso de erro.
    """
    psql_command_list = [
        'psql',
        f'--host={DB_HOST}',
        f'--port={DB_PORT}',
        f'--username={DB_USER}',
        f'--dbname={DB_NAME}',
        '--command',
        command
    ]
    
    process_env = os.environ.copy()
    process_env["PGPASSWORD"] = DB_PASSWORD

    try:
        result = subprocess.run(
            psql_command_list,
            env=process_env,
            capture_output=True,
            text=True,
            check=True,
            encoding='utf-8'
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        error_message = f"Erro ao executar comando para o banco de dados: {command}\n{e.stderr}"
        raise RuntimeError(error_message) from e

def focused_exploratory_analysis():
    """
    Realiza uma análise exploratória focada apenas nas tabelas de interesse.
    """
    if not all([DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME]):
        print("❌ Erro: Variáveis de ambiente do banco de dados não estão definidas.")
        return

    print("=" * 70)
    print(f"🔎 Iniciando Análise Focada do Banco de Dados: '{DB_NAME}'")
    print(f"🎯 Foco: {', '.join(TABELAS_DE_INTERESSE)}")
    print("=" * 70)

    try:
        for table in TABELAS_DE_INTERESSE:
            print(f"\n" + "-" * 60)
            print(f"📊 Analisando Tabela: '{table}'")
            print("-" * 60)

            # 1. Contar o número de linhas
            print(f"\n[1/3] Contando linhas da tabela '{table}'...")
            count_output = run_psql_command(f"SELECT COUNT(*) FROM {table};")
            print(f"✅ {count_output.strip()}")

            # 2. Descrever a estrutura da tabela (colunas e tipos)
            print(f"\n[2/3] Descrevendo estrutura da tabela '{table}'...")
            structure_output = run_psql_command(f"\\d {table}")
            print(f"✅ Estrutura:\n{structure_output}")

            # 3. Mostrar uma amostra dos dados
            print(f"\n[3/3] Buscando amostra de {SAMPLE_ROWS} linhas da tabela '{table}'...")
            sample_output = run_psql_command(f"SELECT * FROM {table} LIMIT {SAMPLE_ROWS};")
            print(f"✅ Amostra de Dados:\n{sample_output}")

        print("\n" + "=" * 70)
        print("🎉 Análise Focada Concluída com Sucesso!")
        print("=" * 70)

    except RuntimeError as e:
        # Adicionamos uma verificação para o erro comum de "tabela não existe"
        if 'does not exist' in str(e):
            print(f"\n❌ FALHA NA ANÁLISE: A tabela '{table}' não foi encontrada no banco de dados.")
            print("   Por favor, verifique a lista 'TABELAS_DE_INTERESSE' no script.")
        else:
            print(f"\n❌ FALHA NA ANÁLISE: {e}")
    except Exception as e:
        print(f"\n❌ Ocorreu um erro inesperado: {e}")

if __name__ == "__main__":
    focused_exploratory_analysis()
