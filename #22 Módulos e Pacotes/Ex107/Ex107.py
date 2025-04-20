import moeda
from moeda import LeiaFloat

valor = LeiaFloat("Diga o preço: R$ ")

print(f"A metade de {valor} é {moeda.metade(valor)}")
print(f"O dobro de {valor} é {moeda.dobro(valor)}")
print(f"Aumentado em 10% ,temos {moeda.aumentar(valor, 10)}")
print(f"Reduzindo em 13% ,temos {moeda.diminuir(valor, 13)}")