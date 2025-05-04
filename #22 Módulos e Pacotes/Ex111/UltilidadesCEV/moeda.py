from . import Color
#$ Exibição Organizada na tela
def resumo(valor, aumento=0, redução=0,sit=True):
    print(f"{"•—"*14+"•"}\n{"RESUMO DO VALOR":^29}\n{"•—"*14+"•"}")
    print(f"Preço analizado:{moeda(valor):>13}")
    print(f"Dobro do preço:{dobro(valor):>14}")
    print(f"Metade do preço:{metade(valor):>13}")
    print(f"{aumento}% de aumento:{aumentar(valor,aumento):>14}")
    print(f"{redução}% de redução:{diminuir(valor,redução):>14}")
    print("—-"*14+"—")
    
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
    return situação(result, sit)

#$ Dobro de valor
def dobro(valor=0, sit=True):
    result =  valor * 2
    return situação(result, sit)
    
#$ Aumento por %
def aumentar(valor=0, por=1, sit=True):
    result = valor + (valor * por / 100)
    return situação(result, sit)

#$ Reduzir por %
def diminuir(valor=0, por=1, sit=True):
    result = valor - (valor * por /100)
    return situação(result, sit)
    
#$ Formatação melhorada
def moeda(valor):
    retorno = str(round(valor,2)).replace(".",",")
    return f"R${retorno}"

def situação(result, sit):
    if sit:
        return moeda(result)
    else:
        return result