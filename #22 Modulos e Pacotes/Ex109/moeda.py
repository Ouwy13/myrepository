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
def metade(valor=0, sit=True):
    result = round((valor / 2),1)
    return situação(sit, result)

#$ Dobro de valor
def dobro(valor=0, sit=True):
    result =  valor * 2
    return situação(sit, result)
    
#$ Aumento por %
def aumentar(valor=0, por=1, sit=True):
    result = valor + (valor * por / 100)
    return situação(sit, result)

#$ Reduzir por %
def diminuir(valor=0, por=1, sit=True):
    result = valor - (valor * por /100)
    return situação(sit, result)

#$ Condição de analize
def situação(sit, result):
    if sit:
        return moeda(result)
    else:
        return result
    
def moeda(valor):
    retorno = f'R${valor:.2f}'.replace(".",",")
    return retorno