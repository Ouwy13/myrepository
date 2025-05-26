from func import Color as C
from time import sleep as pause
from os import system
system("cls")
#&print("—∿•>›─│╭╮╰╯")


def Linha(form="-", tam=0, color=0, final=False, escreva=True):
    from func import Color as C
    if escreva:
        print(f"{C.c(color)}{form}"*tam,end="", flush=True)
        print(f"{form[0]}{C.c()}" if final else f"{C.c()}")
    else:
        retorno = (
            f"{C.c(color)}{form}"*tam,
            f"{form[0]}{C.c()}" if final else f"{C.c()}"
        )
        for r in retorno:
             return r

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
    from func import Analize as A
    system("cls")
    c = [f"{C.c(Color)}", f"{C.c(7)}"] #& <- Cor de destaque
    titulo = f"{"Detalhes de Cadastros 👤🗂️":^31}"
    print(C.caixa_arredondada(titulo, Color))  

    print(f"{c[0]}~>{c[1]}  {"Nª":<3}  {"Nome":<14}{"Idade"}  {"Sexo"}")
    print(f"{C.c(7)}╭{Linha("∿",32,7, True, False)}{C.c(7)}╮")

    for pos, dados in enumerate(Banco):
        nome = A.Tam_nome(dados["Nome"], 12)
        sexo = A.Cor_sx(dados["Sexo"])
        print(f"{C.c(7)}│ {pos+1:>3} {c[0]}-›{c[1]} {nome:14} {dados["Idade"]:<6} {sexo} {C.c(7)}│")
        pause(0.6) if animação else print(end="")
    
    print(f"{C.c(7)}╰{Linha("∿",32,7, True, False)}{C.c(7)}╯")

    c = input(f"{c[0]}~>{c[1]}  Enter Continuar..")
    system("cls")




