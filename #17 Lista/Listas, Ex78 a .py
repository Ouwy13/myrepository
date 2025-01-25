def Teoria():
    # Listas podem ser modificadas
    lanche = [
        'Hanburgue','Suco','Pizza','Pudim'
    ]
    # Adicionar itens
    lanche[3] = 'Regrigerante' # Vai substituir o item por outro
    lanche.append('Refrigerante') # Adiciona no final
    lanche.insert(0,'Refrigerante') # Adiciona determiando o index

    # Remover itens
    del lanche[3] # Delete item do index 3
    lanche.pop(3) # Remove item do index 3
    lanche.remove('Pizza') # Remove item pelo nome
    lanche.pop() # Remove o ultimo item
    if 'Pizza' in lanche: # Verifica se tiver o item
        lanche.remove('Pizza')

    # Cria listas com o 'Range'
    valores = list[range(4,11)] # Valores recebem 'lista' de 4 a 10

    # Ordenar itens
    valores = [8,4,6,9,1,3]
    valores.sort() # Ordena em ordem crescente
    valores.sort(reverse=True) # Ordena em ordem decrescente

    # Ver a quantidade
    len(valores) # Ler a quantidade de itens

    # Fazer uma copia
    a = list(2,4,2,1)
    b = a[:] # B recebe todos os itens de A

def Test():
    num = [2,5,9,1]
    num[2] = 3 # Subtituir o valor do  index 2
    num.append(4) # Adiciona no final
    num.sort() # Organizar em ordem
    #num.sort(reverse=True) # Organiza em forma descresente
    num.insert(2, 0) # Adicionar sem remover no posição 2 valor 0
    num.pop() # Remove o ultimo item
    num.pop(2) # Remove o valor do index 2
    num.remove(2) # Remove o primeiro valor 2
    if 0 in num: # Se 0 em num
        num.remove(0) # Remova o numero 0
    else:
        print('Não achei o valor 0')
    print(num)
    print(f'Essa lista tem {len(num)} itens')

def Test2():
    valores = list()
    # Valores determinados
    '''valores.append(5)
    valores.append(9)
    valores.append(3)'''

    # Valores informados pelo usuario
    for cont in range(1,6):
        valores.append(int(input(f'Informe {cont} valor: ')))
    
    # Apaga toda a  lista
    del(valores)
    print('Os valores: ',end='')
    for valor in valores: # Somente o valor
        print(f'{valor}',end='...')
    print('\nPosições')
    
    for pos,valor in enumerate(valores): # Valores e Posição
        print(f'Na posição {pos} está o valor {valor}')

def Test3():
    a = [2,4,4,6]
    # Ligação
    b = a # ligação de listas
    # Copia
    b = a[:] # b recebe todos os valores de a
    b.remove(4)
    print(f'Lista A: {a}')
    print(f'Lista B: {b}')
def Ex78():
    print('Ordem')
    valores = list()

    for cont in range(1,6):
        valores.append(int(input(f'Informe {cont}ª valor: ')))
    
    # Lista com os valores
    for pos,valor in enumerate(valores):
        print(f'Valor {valor} posição {pos}')
    # Maior valor e sua posição
    print(f'O maior valor foi {max(valores)} e suas posiçãos: ',end='')

    for pos,valor in enumerate(valores):
        if valor == max(valores):
            print(f'{pos}', end= '..')
    # Menor valor e sua posição
    print(f'\nO maior valor foi {min(valores)} e suas posiçãos: ',end='')
    
    for pos, valor in enumerate(valores):
        if valor == min(valores):
            print(f'{pos}', end='..')

def Ex79():
    print('——'*12)
    print('Adicione valores a lista')
    print('——'*12)
    valores = list()
    v = 1
    while True:
        valor = int(input(f'Informe {v}ª valor: '))
        v +=1
        if valor in valores:
            print('Valor ja existente')
        else:
            valores.append(valor)
            print('Valor registrado..')
        while True:
            cond = str(input('Continuar [S/N]: ')).strip().upper()[0]
            if cond in 'SN':
                break
        if cond == 'N':
            break
            
    print('——'*12)
    print(f'Valores em ordem: ',end='')
    valores.sort()
    for valor in valores:
        print(valor,end =' ')
    
def Ex80():
        print('Lista')
        valores = list()
        v = 1
        ultimo = primeiro = 0

def Ex81():
    print('Lista de numeros')
    v =1
    valores = list()
    while True:
        valores.append(int(input(f'Qual o {v}ª valor: ')))
        v +=1
        while True:
            cond = str(input('Continaur [S/N]: ')).strip().upper()[0]
            if cond in 'SN':
                break
        if cond == 'N':
            break
    # Numero de valores
    print(f'Você digitou {len(valores)} valores')
    # Ordem descresente
    print('Os valores em ordem descresente: ',end='')
    valores.sort(reverse=True)
    for valor in valores: 
        print(valor,end= ' ')
    # Quantas vezes apareceu o numero 5
    if 5 in valores:
        print('\nO valor 5 apareceu nas posições: ',end=' ')
        for pos,valor in enumerate(valores):
            if valor == 5:
                print(f'{pos}', end=' ')
    else:
        print('\nO valor 5 não apareceu!')
def Ex82():
    valores = list()
    pares = list()
    impares = list()
    v = 1
    print('Valores Pares e Impares')
    while True:
        valores.append(int(input(f'qual o {v}ª valor: ')))
        v+=1
        while True:
            cond = str(input('Condição [S/N]: ')).strip().upper()[0]
            if cond in 'SN':
                break
        if cond == 'N':
            break
        
    valores.sort()
    print('——'*20)
    # Exibição da lista inteira
    print('A lista completa:', end=' ')                
    for valor in valores:
        print(f'{valor}',end=' ')
    # Analize de numeros pares e impares
    for valor in valores:
        if valor % 2 == 0:
            pares.append(valor)
        else:
            impares.append(valor)
    # Valores Pares
    print('\nValores Pares: ',end='')
    for par in pares:
        print(par,end=' ')
    # Valores Impares
    print('\nValores Impares: ',end='')
    for impar in impares:
        print(impar,end=' ')
   
def Ex83():
    caracter = list()
    print('\033[1;37m∿∿'*10)
    print(f'{'\033[36m'}{'Analize de expresão':^20}{'\033[37m'}')
    print('∿∿'*10)
    expressão = str(input('Digite a expressão:\n\033[36m '))
    for letra in expressão:
        caracter.append(letra)
    a = caracter.count('(')
    b = caracter.count(')')
    print(f'{'\033[37m'}{'——'*10}')
    if (a + b) % 2 == 0 and a == b:
        print('\033[32mSua expressão é valida!\033[m')
    else:
        print('\033[31mSua expressão não é valida!\033[m')

if __name__ == "__main__":
    Ex80()