from func import Color as C, Menu
from os import system
from time import sleep as pause

#$ Função de limpa tela
def limpa():
    system("cls")
# Colocar a opçãoss
#$ Analize de Ops
def ops(msg, Color=7):
    c = [f"{C.c(Color)}", f"{C.c(7)}"] #& <- Cor de destaque
    #% Definindo mensagem padrão
    msg = f"{c[0]}~>{c[1]} {msg}: {c[0]}"
    while True:
        try:
            esc = str(input(msg))
            #% Necessario para informar erro!
            caso_erro = esc
            esc = int(esc)
        except ValueError:
            print(f'{C.c(1)}Não é opção válida: {C.c(41)}"{caso_erro}"{C.c(7)}')
            pause(2)
            limpa()
            Menu.Menu_Princ(6)
        else:
            Esta_Aprovado = Analize_Ops(esc)
            if Esta_Aprovado:
                print(f'{C.c(2)}Opção válida!{C.c(7)} ')
                pause(1)
                return esc
                break
            else:
                print(f"{C.c(1)}Opção Invalida!{C.c(7)}")
                pause(2)
                limpa()
                Menu.Menu_Princ(6)

def Analize_Ops(esc):
    #% Pegar cada opção disponivel para analize
    Ops = []
    ops = Menu.Opcao()
    for op in ops:  
        Ops.append(op[21])
    if str(esc) in Ops:
        return True
    else:
        return False



        