from os import system
from func.Color import c, caixa_arredondada
system("cls")
def tarefa(esc, caminho):
    match esc:
        case 1:
            #$ Mostrar Dict de Cadastro
            from func import Banco, Menu
            Menu.Menu_Cadastradas(Banco.carregar_BD(caminho),5,True)
        case 2:
            from func.Analize import Leia_Nome, Leia_Idade, Leia_Sexo
            system("cls")
            Color = [f"{c(3)}", f"{c(7)}"] #& <- Cor de destaque
            #$ 🆕 Novo cadastro
            titulo = f"{" 🆕 Novo cadastro ":^19}"
            print(caixa_arredondada(titulo, 3)) #& Alterar a cor de destaque daq. tbm
            print(f"{Color[0]}~>{Color[1]} Passe os informes📋")
            dados = dict()
            dados["Nome"] = Leia_Nome(f"{Color[0]}│{Color[1]}🤔 Nome:{Color[1]} ")
            #dados["Idade"] = Leia_Idade("│Idade: ")
            #dados["Sexo"] = Leia_Sexo("│Sexo: ")

        case 3:
            #$ 📝 Editar cadastro
            print("📝 Editando cadastro...")
        case 4:
            #$ 🗑️ Excluir cadastro
            print("🗑️ Excluindo cadastro...")
        case 0:
            #$ Para Programa
            para = True
            return para



        