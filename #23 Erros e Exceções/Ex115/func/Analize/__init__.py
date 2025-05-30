from func import Color as C, Menu
from os import system
from time import sleep as pause
#&print("—∿•>›─│╭╮╰╯")

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

#$ Tamanho de exibição de um nome
def Tam_nome(nome,tam):
    if len(nome) > tam:
        return f"{nome[:tam]}."
    else:
        return nome[:tam]
    
#$ Cor de exibição do sexo
def Cor_sx(sexo):
    sexo = sexo.split()[0].upper() 
    if sexo == "M":
        return f"{C.c(4)}{sexo}{C.c(7)}"
    else:
        return f"{C.c(95)}{sexo}{C.c(7)}"

#$ Analizar se o arquivo banco existe
def arq_ext(caminho):
    import os
    #& Verifica se o arquivo está criado no caminho retornado True ou False
    return os.path.exists(caminho)

#$ Analizar e criar o arquivo
def pruc_BD(caminho, Color):
    from func.Banco import salva_BD, BD
    from func.Menu import Menu_Princ
    c = [f"{C.c(Color)}", f"{C.c(7)}"] #& <- Cor de destaque
    if not arq_ext(caminho):
        print(f"{C.c(1)}Banco de Dados não encontrado! :/{C.c(7)}")
        pause(1)
        system("cls")
        cond = cond_SN(f"{c[0]}~>{c[1]}  Deseja adicinar lista com sugestões 🤔📤👥[S/N]: {c[0]}")
        if cond == "S":
            print(f"{c[0]}•{c[1]} Criando o BD com cadastros ✅..")
            salva_BD(caminho, BD())
        else:
            print(f"{c[0]}•{c[1]} Criando o BD Vazil ✅..")
            salva_BD(caminho, [])
        
        pause(1)
        system("cls")
        Menu_Princ(Color,True)  

def cond_SN(msg):
    while True:
        try:
            cond = str(input(msg)).upper().split()[0]
            if cond in "SN":
                return cond
            else:
                print(f"{C.c(1)}Condição [S/N]!{C.c(7)}")
        except IndexError:
            print(f"{C.c(1)}Condição Invalida!{C.c(7)}")

#$ Cadastro nova pessoa
def Leia_Nome(msg):
    while True:
        try:
            nome = str(input(msg)).capitalize()
            if nome.replace(" ","").isalpha():
                return nome
                break
            else:
                print(f'{C.c(1)}Nome invalido! {C.c(41)}"{nome}"{C.c(7)}')
        except IndexError:
            print(f"{C.c(1)}Informe o Nome!{C.c(7)}")

def Leia_Idade(msg):
    while True:
        try:
            idade = int(input(msg))
            if 0 < idade < 150:
                return idade
                break
            else:
                print(f"{C.c(1)}Idade invalida!{C.c(7)}")
        except ValueError:
            print(f"{C.c(1)}Informe a Idade!{C.c(7)}")

def Leia_Sexo(msg):
    while True:
        try:
            sexo = str(input(msg)).upper().split()[0]
            if sexo in "MF":
                return sexo
                break
            else:
                print(f"{C.c(1)}Sexo invalido!{C.c(7)}")
        except IndexError:
            print(f"{C.c(1)}Informe o Sexo!{C.c(7)}")


    


    



        