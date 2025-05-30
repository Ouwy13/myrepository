from func import Menu, Analize, Atividade
from func.Analize import arq_ext

caminho = r"C:\Users\ᒎᗝᔕᗴ亗セ\Desktop\Python\#23 Erros e Exceções\Ex115\func\Banco\Banco.JSON"

#& Animação Inicial
Anima = True
while True:
    Menu.Menu_Princ(6, Anima)
    Analize.pruc_BD(caminho,6)
    Opção = Analize.ops("Qual opção", 6)
    Att = Atividade.tarefa(Opção, caminho)
    Anima = False
    #& Para as Operações
    if Att:
        from func.Color import c
        from os import system
        system("cls")
        print(f"{c(2)}>>>{c(7)} Programa Finalizado! {c(2)}<<<{c()}")
        break