from os import system
from time import sleep
inventario = ['Espada', 'Machado', 'Picareta']
menu = [
    f"{'--'*10}",
    "F-Remover item",
    "A-Adicionar Item",
    "R-Finalizar"
]

while True:
    print("-="*10)
    print(f'{"Inventario":^20}')
    print("-="*10)
    for pos, item in enumerate(inventario):
        print(f"{pos+1} - {item}")
    for m in menu:
        print(m)
    print("--"*10)
    while True:
        try:
            pergunta = str(input("Qual opção: ")).strip().upper().split()[0]
            if pergunta.isalpha():
                if pergunta in 'FAR':
                    print("Acerto Misseravel")
                    break
                else:
                    print("Condição erra Egua!!")
            else:
                print("Informe somente letra burro!!")
        except IndexError:
            print('Digite a opção filho da mãe!!')
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

                
    else:
        print()