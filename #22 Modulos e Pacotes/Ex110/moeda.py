import Color
#$ Exibição Organizada na tela
def resumo(valor=0, aumento=0, redução=0,sit=True):
    print(f"{"•—"*14+"•"}\n{"RESUMO DO VALOR":^29}\n{"•—"*14+"•"}")
    print(f"Preço analizado:{moeda(valor,sit):>13}")
    print(f"Dobro do preço:{dobro(valor, sit):>14}")
    print(f"Metade do preço:{metade(valor, sit):>13}")
    print(f"{aumento}% de aumento:{aumentar(valor,aumento, sit):>14}")
    print(f"{redução}% de redução:{diminuir(valor,redução, sit):>14}")
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
    
def moeda(valor, sit=True):
    if sit:
        retorno = f'R${valor:.2f}'.replace(".",",")
    else:
        retorno = valor
    return retorno