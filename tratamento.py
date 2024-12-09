import pandas as pd
from unidecode import unidecode
import os

caminho_arquivo = "arrecadacao-estado.csv"

dados = pd.read_csv(caminho_arquivo, encoding='latin1', delimiter=';')

dados.columns = [unidecode(col).strip() for col in dados.columns]  # Corrige nomes de colunas

dados = dados.applymap(lambda x: unidecode(str(x)).replace(',', '') if isinstance(x, str) else x)  # Remove formatação inválida

# Conversão para numérico com tratamento seguro
numericas = [
    'IMPOSTO SOBRE IMPORTACAO',
    'IMPOSTO SOBRE EXPORTACAO',
    'IPI - FUMO',
    'IPI - BEBIDAS',
    'IPI - AUTOMOVEIS',
    'IPI - VINCULADO A IMPORTACAO',
    'IPI - OUTROS',
    'IRPF',
    'IRPJ - ENTIDADES FINANCEIRAS',
    'IRPJ - DEMAIS EMPRESAS',
    'IRRF - RENDIMENTOS DO TRABALHO',
    'IRRF - RENDIMENTOS DO CAPITAL',
    'IRRF - REMESSAS P/ EXTERIOR',
    'IRRF - OUTROS RENDIMENTOS',
    'IMPOSTO S/ OPERACOES FINANCEIRAS',
    'IMPOSTO TERRITORIAL RURAL',
    'IMPOSTO PROVIS.S/ MOVIMENT. FINANC. - IPMF',
    'CPMF', 'COFINS',
    'COFINS - FINANCEIRAS',
    'COFINS - DEMAIS'
]

for col in numericas:
    if col in dados.columns:
        dados[col] = pd.to_numeric(dados[col], errors='coerce').fillna(0)  # Converte para numérico e substitui NaNs por 0

# Preenchendo valores vazios com padrões
dados['Mes'] = dados['Mes'].fillna('Desconhecido')
dados['UF'] = dados['UF'].fillna('Desconhecida')

diretorio_alvo = "tratamento"
os.makedirs(diretorio_alvo, exist_ok=True)

caminho_novo_arquivo = os.path.join(diretorio_alvo, "arrecadacao-estado-limpo.csv")

dados.to_csv(caminho_novo_arquivo, index=False, encoding='utf-8')

print(f"Os dados foram salvos no novo arquivo: {caminho_novo_arquivo}")
