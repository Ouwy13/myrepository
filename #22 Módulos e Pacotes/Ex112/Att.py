import sys
import os

# Adiciona o diretório base ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from UltilidadesCEV import moeda, dados, Color

valor = dados.LeiaFloat(f"{Color.c(7)}Diga o preço: R$")
moeda.resumo(valor, 80, 30)