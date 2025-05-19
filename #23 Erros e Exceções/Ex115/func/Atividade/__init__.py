from os import system
system("cls")
def tarefa(esc):
    if esc == 1:
        #$ Mostrar Dict de Cadastro
        from func import Banco, Menu
        Menu.Menu_Cadastradas(Banco.BD(),5,True)
        