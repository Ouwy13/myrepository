from os import system
from func.Color import c, caixa_arredondada
from time import sleep
system("cls")
def tarefa(esc, caminho):
    match esc:
        case 1:
            #$ Mostrar Dict de Cadastro
            from func import Banco, Menu
            Menu.Menu_Cadastradas(Banco.carregar_BD(caminho),5,True)
        case 2:
            from func import Banco, Menu
            from func.Analize import Leia_Nome, Leia_Idade, Leia_Sexo, cond_SN

            system("cls")
            Color = [f"{c(3)}", f"{c(7)}"] #& <- Cor de destaque
            #$ 🆕 Novo cadastro
            while True:
                titulo = "Cadastro Novo"
                print(caixa_arredondada(f"{titulo:^19}", 3))
                
                print(f"{Color[0]}~>{Color[1]} Passe os informes📋")
                dados = dict()
                print(Menu.Linha("∿", 21, 7, True, False))
                #$ Coletar os dados
                dados["Nome"] = Leia_Nome(f"{Color[0]}│{Color[1]}🤔 Nome:{Color[1]} ")
                dados["Idade"] = Leia_Idade(f"{Color[0]}│{Color[1]}🎂 Idade:{Color[1]} ")
                dados["Sexo"] = Leia_Sexo(f"{Color[0]}│{Color[1]}🚻 Sexo:{Color[1]} ")
                #$ Salvar o cadastro
                banco = Banco.carregar_BD(caminho)
                banco.append(dados)
                Banco.salva_BD(caminho, banco)
                dados.clear()

                print(f"{Color[0]}>{Color[1]} Cadastro salvo! ✅")
                print(Menu.Linha("∿", 21, 7, True, False))
                sleep(1)
                cond = cond_SN(f"{Color[0]}~>{Color[1]} Outro cadastro? [S/N]: {Color[0]}")
                system("cls")
                if cond == "N":
                    break
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



        