def Teoria():
    # Tuplas são imutaveis
    # Pode ser de varios tipos de dados
    # Fatiamento
    lanche = ('Hamburge', 'Suco', 'Pizza', 'Pudim')
    print(lanche) # Exibi a lista
    print(lanche[1]) # Exibi o item do index 1
    print(lanche[-2]) # Exibi o item do index -2/ o item voltando da lista 'Pizza'
    print(lanche[1:3]) # Exibi os itens do index 1,3
    print(lanche[2:]) # Exibi os itens do index 2 até o final
    print(lanche[:2]) # Exibi do inicio até o iten do index 2 'Sem mostra o item 2'
    print(lanche[-2:]) # Exibi do item do index -2 até o final
    
    # Regra de Exibição sem ('')
    for comida in lanche: # Para cada comida em lanche
        print(comida) # Exibi cada item da lista 
    
    #Leitura de itens na tuplas
    len(lanche) # Ver quantos item tem 
    
    # Exibição dos ites da tupla
    for cont in range(0, len(lanche)): # fazer a contagem de 0 até a quantidade de item
        print(cont) # 0 a 4
        print(lanche[cont]) # exibir lanche[na posição 'cont']

        # Exibição com posição
        for comida, pos in enumerate(lanche): #exibi o item com sua posição enumerate()
            print(f'{comida} na posição {pos}')
        
        for cont in range (0, len(lanche)): #exibi o item com sua posição cont
            print(f'{lanche} na posição {cont}')
        
        # Exibição em ordem de tamnho
        print(sorted(lanche)) # sorted mostra a tupla em ordem do maior p. menor 

        # Soma de listas
        a = (1, 3, 5, 6)
        b = (3, 5, 7, 9)
        c = a + b # ordem intefere a sequencia
        print(c) # (1, 3, 5, 6, 3, 5, 7, 9)
        
        # Exibição de quantidade determinado
        print(c.count(3)) # Exibi a quantidade desse item '3'
        
        # Exibi o index do item determinado
        print(c.index(9)) # Index do 9
        print(c.index(3)) # O primeiro idex do item 3

        # Apagar a tuplas
        del(c) # Apaga toda a tupla

def Ex72():
    num = 1
    num_extenso = (
        'zero','um','dois','três','quatro','cinco',
        'seis','sete','oito','nove','dez','onze',
        'doze','treze','catorze','quinze','dezesseis',
        'dezessete','dezoito','dezenove','vinte'
        )
    while True:
        while True:
            num = int(input('Informe um numero entre 0 e 20: '))
            if num >= 0 and num <=20:
                break
        '''for esc in num_extenso[num]:
            print(esc,end='')'''
        print(f'Você digitou o numero {num_extenso[num]}')
        cond = ''
        while True:
            cond = str(input('Continuar [S/N]: ')).strip().upper()[0]
            if cond not in 'SN':
                print('Condição [S/N]')
            else:
                break   
        if cond == 'N':
            break
    print('Fim do Programa')  

def Ex73():
    '''
    print(times) #Lista completa
    print(times[0:5]) # Lista dos 5 primeiros
    print(times[-4:]) # Lista dos 4 ultimos
    print(times.index('Flamengo')+1) #Posição do item 'Flamengo'
    '''
    
    from os import system
    from time import sleep
    times = (
        'Botafogo','Palmeiras','Flamengo','Fortaleza','Internacional',
        'São Paulo','Corinthians','Bahia','Cruzeiro','Vasco da Gama',
        'Vitória','Atlético Mineiro','Fluminense','Grêmio',
        'Red Bull Bragantino','Juventude','Athletico Paranaense',
        'Criciúma','Atlético Goianiense','Cuiabá'
    )
    tab = [
        f'{'\033[1;37m'}{'——'*12}',
        F'{'\033[36mCampeonato Brasileiro':^28}',
        f'{'\033[37m'}{'——'*12}',
        '1️⃣ -Os 20ª colocados',
        '2️⃣ -Os 5ª primeiros',
        '3️⃣ -Os 4ª ultimos',
        '4️⃣ -Ordem Alfabetica',
        '5️⃣ -Possição Mengão',
        '0️⃣ -Sair',

    ]
    esc = 3
    while esc != 0:
        for tabe in tab:
            print(tabe)
        while True:
            esc = int(input('Qual sua escolha: '))
            if esc > 5:
                print('Condição de 0 a 5!!')
            else:
                break
        if esc ==1:
            #todos os times
            print('\033[1;37m∿∿'*12)
            print(f'\033[32m20ª Colocados Brasileirão\033[37m')
            print('∿∿'*12)
            for pos,time in enumerate(times):
                print(f'|{'0'if pos+1 <=9 else ''}{pos+1:<1}-{time:20}|')
            print('——'*12)
        elif esc ==2:
            # Os 5 primeiros
            print('\033[32mOs 5ª primeiros\033[37m')
            for pos, time in enumerate(times[:5]):
                print(f'{pos+1}-{time}')
            print('——'*12)
        elif esc ==3:
            # Os 4 ultimos
            print('\033[31mOs 4ª ultimos\033[37m')
            for pos,time in enumerate(times[-4:]):
                print(f'{pos+1}-{time}')
            print('——'*12)
        elif esc ==4:
            # Times em ordem alfabetica
            print('\033[36mOrdem alfabetica\033[37m')
            for time in sorted(times):
                print(time)
            print('——'*12)
        elif esc ==5:
            #Colocação do flamengo
            print(f'Flamengo está em {times.index('Flamengo')+1}ª lugar')
        if esc != 0:
            p = input('Continuar Enter...')
        system('cls')
    print('Fim do programa 😊')

def Ex74():
    from random import randint
    nums = (randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))
    print(f'Os valores sorteados: ',end='')
    for num in nums:
        print(f'{num}',end=' ')
    #print(f'\nO maior valor: {sorted(n)[-1]}')
    #print(f'O menor valor: {sorted(n)[0]}')
    print(f'\nO maior valor: {max(nums)}')
    print(f'O menor valor: {min(nums)}')

def Ex75():

    nums = (
        int(input('Digite 1ª valor: ')),
        int(input('Digite 2ª valor: ')),
        int(input('Digite 3ª valor: ')),
        int(input('Digite 4ª valor: ')))

    # Valores digitados
    print(f'Você digitou os valores: {nums}')
    # Quantas vezes apareceu o num 9
    if nums.count(9):
        print(f'O valor 9 apareceu {nums.index(9)} vezes')
    else:
        print('O valor 9 não apareceu')
    # Posição do numero 3
    if 3 in nums: # 3 em numeros faça..
        print(f'O valor 3 apareceu na {nums.index(3)+1}ª posição')
    else:
        print('O valor 3 não foi digitado')
    # Analize numeros pares
    print('Pares: ',end='')
    for n in nums:
        if n %2 ==0:
            print(f'{n}',end=' ')
    # Analize numeros impares
    print('\nImpares: ',end='')
    for n in nums:
        if n %2 ==1:
            print(f'{n}',end=' ')
    
def Ex76():
    produtos  = (
        'Lápis',1.75,'Borracha', 2.00,
        'Caderno',15.90,'Estojo',25.00,
        'Transferidor',4.20,'Compasso',9.99,
        'Mochila',120.3,'Canetas',22.30,'Livro',34.90
    )
    print('\033[1;37m——'*17)
    print(f'{'\033[34mLISTA DE PREÇOS 🛍️\033[37m':^44}')
    print('——'*17)
    for cont in range(0,len(produtos)):
        # primeira linha
        if cont % 2 == 0: #Exibir os produtos
            print(f'{produtos[cont]:•<24}', end=' ')
        else: #Exibir os preços
        # segunda linha
            print(f'R${produtos[cont]:>7.2f}') #Funciona com o espaçamento e a formatação :>6.2f
    
    print('——'*17)

def Ex77():
    palavras = (
        'curso','paralelepipedo','estudar','faculdade','programação',
        'matematica'
    )
    for palavra in palavras:
        print(f'\033[1;37m\nNa palavra {palavra.upper()} temos ',end='')
        for letra in palavra:
            if letra.lower() in 'aeiou':  # Verificação se a letra é uma vogal
                print(letra,end=' ')
            '''if letra.count('a'):
                print('a',end=' ')
            elif letra.count('e'):
                print('e',end=' ')
            elif letra.count('i'):
                print('i',end=' ')
            elif letra.count('o'):
                print('o',end=' ')
            elif letra.count('u'):
                print('u',end=' ')'''
            
                
        
if __name__ == "__main__":
    Ex76()