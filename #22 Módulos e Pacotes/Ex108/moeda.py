import Color

#$ Analize de  float
def LeiaFloat(msg):
    while True:
        try:
            valor = float(input(msg))
            return valor
            break
        except ValueError:
            print(f"{Color.c(1)}Informe somente numeros!{Color.c()}")
#$ Metade de um valor
def metade(valor=0):
    return round((valor / 2),1)

#$ Dobro de valor
def dobro(valor=0):
    return valor * 2

#$ Aumento por %
def aumentar(valor=0, por=1):
    return valor + (valor * por / 100)

#$ Reduzir por %
def diminuir(valor=0, por=1):
    return valor - (valor * por /100)

def moeda(valor):
    retorno = str(round(valor,2)).replace(".",",")
    return f"R${retorno}"