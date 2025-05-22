from func import Color as C
from time import sleep as pause
from os import system
system("cls")
#&print("—∿•>")

def Linha(form="-", tam=0, color=0, final=False):
    from func import Color as C
    print(f"{C.c(color)}{form}"*tam,end="", flush=True)
    print(f"{form[0]}{C.c()}" if final else f"{C.c()}")

def Opcao():
        ops = [
            f"{c[0]}~>{c[1]} 🔍 Informações.. ",
            f"{c[0]}|{c[1]}1 Pessoas Cadastradas",
            f"{c[0]}|{c[1]}2 Adicionar Pessoa ",
            f"{c[0]}|{c[1]}3 Editar Pessoa ",
            f"{c[0]}|{c[1]}4 Remover Pessoa ",
            f"{c[0]}|{c[1]}0 Finalizar o programa",
        ]
        return ops

#$ Menu Inicial
def Menu_Princ(Color=7, animação=False):
    global c
    c = [f"{C.c(Color)}", f"{C.c(7)}"] #& <- Cor de destaque
    Linha("•—",12, 7, True)
    print(f"{c[0]}{"Menu Principal":^25}{c[1]}")
    Linha("•—",12, 7, True)
    
    #% Extrair as opção da função
    ops = Opcao()
    for op in ops:
        print(op)
        pause(0.6) if animação else print(end="")
    Linha("-—",12,7,True)
    pause(0.6) if animação else print(end="")

#$ Menu de Pessoas Cadastrdas
def Menu_Cadastradas(Banco, Color=7, animação=False):
    c = [f"{C.c(Color)}", f"{C.c(7)}"] #& <- Cor de destaque
    Linha("∿∿",14,7, True)
    print(f"{c[0]}{"Detalhes de Cadastros 👤📄":^28}{c[1]}")  
    print(f"~> {""}{"Nome"}{"Idade"}{"Sexo"}")
    Linha("∿∿",14,7, True)

    for pos, dados in enumerate(Banco):
        print(f"{pos+1:<3} {dados["Nome"]} {dados["Idade"]} {dados["Sexo"]}")
        pause(0.6) if animação else print(end="")
    Linha("-—",12,7,True)




