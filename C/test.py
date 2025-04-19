from os import system
from time import sleep
inventario = ['Espada', 'Machado', 'Picareta']
def titulo():
    print("-="*10)
    print(f'{"Inventario":^20}')
    print("-="*10)

def exib_inv():
    for pos, item in enumerate(inventario):
        print(f"{pos+1} - {item}")
menu = [
    f"{'--'*10}",
    "F-Remover item",
    "A-Adicionar Item",
    "R-Finalizar"
]
def exib_menu():
    for item in menu:
        print(item)
    print(f"{'--'*10}")
def cong():
    sleep(1)
    system('cls')
    titulo()
    exib_inv()
    exib_menu()

while True:
    titulo()
    exib_inv()
    exib_menu()
    while True:
        try:
            pergunta = str(input("Qual opção: ")).strip().upper().split()[0]
            if pergunta.isalpha():
                if pergunta in 'FAR':
                    print("Acertor Fi")
                    break
                else:
                    print("Condição erra Egua!!")
                    cong()
            else:
                print("Informe somente letra burro!!")
                cong()
        except IndexError:
            print('Digite a opção filho da mãe!!')
            cong()
    if pergunta == "A":
        while True:
            add = str(input("Adicionar item: ")).strip()
            if add.isalpha():
                inventario.append(add)
                break
            else:
                print("Informe um item!!")
        print(f"Item {add} adicionado com sucesso!!")
        sleep(2)
        system('cls')
    elif pergunta == "F":
        while True:
            try:
                del_item = str(input("Remover item: ")).strip()
                if del_item not in '':
                    if del_item.isdigit():
                        if 0 < int(del_item) <= len(inventario) :
                            print(f"Item {inventario[int(del_item)-1]} removido com sucesso!!")
                            inventario.pop(int(del_item)-1)
                            break
                        else:
                            print("Item não registrado!!")
                    elif del_item.isalpha():
                        if del_item in inventario:
                            print(f"Item {del_item} removido com sucesso!!")
                            inventario.remove(del_item)
                            break
                        else:
                            print("Item não existe !!")
            except IndexError:
                print("Informe um item!!")
        sleep(2)
        system('cls')
    elif pergunta == "R":
        print("Sistema finalizado com sucesso!!")
        break