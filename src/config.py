from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent

# Path(__file__) = regressao-linear/src/config.py
# .resolve() transforma o caminho em um caminho absoluto, e
# .parent.parent vai para o diretório raiz do projeto
# visto que .parent vai para o diretorio pai (regressao-linear/src) e o outro
# .parent vai para o diretório pai do src, que é o diretório raiz do projeto
# (regressao-linear), entao ROOT_DIR passa a representar a raiz do projeto

DATA_DIR = ROOT_DIR / 'data'
RAW_DATA_PATH = DATA_DIR / 'Preços_de_casas.csv'

RANDOM_STATE = 42
TEST_SIZE = 0.2
TARGET_COLUMN = "preco_de_venda"
