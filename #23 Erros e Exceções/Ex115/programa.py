from func import Menu, Analize, Atividade
from func.Analize import arq_ext

caminho = r"C:\Users\ᒎᗝᔕᗴ亗セ\Desktop\Python\#23 Erros e Exceções\Ex115\func\Banco\Banco.JSON"

"""#& Carregar o arquivo
#print(carregar_BD(caminho))
for dado in carregar_BD(caminho):
    print(dado)"""

#& Animação Inicial
Anima = False
while True:
    Menu.Menu_Princ(6, Anima)
    Analize.pruc_BD(caminho,6)
    Opção = Analize.ops("Qual opção", 6)
    Att = Atividade.tarefa(Opção, caminho)
    Anima = False
    #& Para as Operações
    if Att:
        break