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
    if sit:
        return moeda(result)
    else:
        return result

#$ Dobro de valor
def dobro(valor=0, sit=True):
    result =  valor * 2
    if sit:
        return moeda(result)
    else:
        return result
    
#$ Aumento por %
def aumentar(valor=0, por=1, sit=True):
    result = valor + (valor * por / 100)
    if sit:
        return moeda(result)
    else:
        return result
#$ Reduzir por %
def diminuir(valor=0, por=1, sit=True):
    result = valor - (valor * por /100)
    if sit:
        return moeda(result)
    else:
        return result
    
def moeda(valor):
    retorno = str(round(valor,2)).replace(".",",")
    return f"R${retorno}"