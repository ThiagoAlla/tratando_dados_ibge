import pandas as pd
from unidecode import unidecode
import os

caminho_arquivo = "arrecadacao-estado.csv"

dados = pd.read_csv(caminho_arquivo, encoding='latin1', delimiter=';')

dados.columns = [unidecode(col) for col in dados.columns]

dados = dados.apply(lambda x: unidecode(x) if isinstance(x, str) else x)

diretorio_alvo = "tratamento"
os.makedirs(diretorio_alvo, exist_ok=True)

caminho_novo_arquivo = os.path.join(diretorio_alvo, "arrecadacao-estado-limpo.csv")

dados.to_csv(caminho_novo_arquivo, index=False, encoding='utf-8')

print(f"Os dados foram salvos no novo arquivo: {caminho_novo_arquivo}")
