import moeda
from moeda import LeiaFloat

valor = LeiaFloat("Diga o preço: R$ oi")

moeda.resumo(valor, 80, 30)