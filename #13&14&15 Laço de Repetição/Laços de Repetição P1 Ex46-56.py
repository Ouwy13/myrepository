def Teoria():
    """""for aopa in range(0, 6):
    print('Aopa')
    print('Acabou')"""

    for c in range(0, 6): # contagem até 5
        print(c)
    for c in range(0, 7): # contagem até 6
        print(c)
    for c in range(6, 0, -1): # contar de forma decresente
        print(c)
    for c in range(0, 7, 2): # contando de 1 a 6 fatiando por 2
        print(c)

    from time import sleep
    num = int(input('Informe um valor: '))
    for c in range(0, num+1): #Informando um valor ate o determinado
        print(c)
        sleep(1)
    print("Fim")

    i = int(input('Inicio: '))
    f = int(input('Final: '))
    c = int(input('Contando de: '))
    for com in range(i,f+1,c):
        print(com)
    print('FIM')

    #Contador
    soma = 0
    for com in range(0, 4):
        n = int(input('Informe o valor: '))
        soma += n
        #ou soma = soma + n
    print(f'A soma de todos os valores é: {soma}')
#ATIVIDADES
def Ex46():
    from time import sleep
    print('\033[1;37mSolta de fogos..')
    for contagem in range(10, 1, -1):
        print(contagem)
        sleep(0.5)
    print('BUM!!! BUM!!! POW!!!🎆')

def Ex47():
    print('numeros pares de 1 a 50')
    for pares in range(2, 51, 2):
        print(pares, end=' ')
    #if pares % 2 == 0:
        #print(pares, end=' ')
    
def Ex48():
    print('A soma de todos os impares multiplos de 3 de 1 a 500')
    soma = 0
    cont = 0
    for co in range (1, 501, 2):
       if co % 3 == 0: # Separa todos os impares
        soma += co #Soma de todos os valores impares
        cont += 1 #Soma da quantidade de valores impares
    print(f'São {cont} valores totalizando {soma}')
        
def Ex49():
    print(f'{'Taboada':^16}')

    num = int(input('Qual valor: '))
  
    for tab in range(0,11):
        result = num * tab
        print(f'{num} x {tab:2} = {result}') #{tab:2} ocupa 2 espaços
   
def Ex50():
    print('Soma de 6 valores pares')
  
    S = 0
    cont = 0
    for c in range(1,7):
        num = int(input(f'Informe o {c}º valor: '))
        c += 1
        if num % 2 == 0: # Separar todos os valores pares
            S += num # Soma todos os valores
            cont += 1 # Soma da quantidade de valores pares
    print(f'Você informou {cont} numeros pares e a soma é: {S}')

def Ex51():
    print('\033[1;37m-='*14)
    print('\033[34mPROGRESSÃO ARITMETICA P.A')
    print('\033[1;37m-='*14)
    print('\033[37mOs 10 primeiros termos')
    a1= int(input('Informe o primeiro termo: '))
    R = int(input('Qual a razão: '))
    print('Fomula: An = a1 + (n-1).r')
    
    for PA in range(1, 11):
        An = a1 + (PA - 1)*R
        print(f'\033[1;34mA{PA:2} \033[1;37m= {a1} + ({PA:2} - 1).{R} = \033[1;34mA{PA}: \033[4;37m{An}\033[m')
    '''a10 = a1 + (10 - 1) * R
    for c in range(a1, a10 + R, R):
        print(f'{c}', end=' ')'''

def Ex52():
    c = {
        'l':'\033[m',
        '1':'\033[1;37m',
        '32':'\033[1;32m', #verde
        '31':'\033[1;31m', #vermelho
        '34':'\033[34m' # azul
    }
    # Para um numero for primo ele deve ser divisivel por 1 e por ele mesmo
    
    print(f'{c["1"]}=-'*14)
    print(f'{c["34"]}{'Analize de N. PRIMO 🤓☝️':^28}{c["l"]}')
    print(f'{c["1"]}-='*14)
    
    num = int(input(f'{c["1"]}Qual o numero inteiro: '))
    tot = 0 #Total de divisões
    
    for cont in range(1, num+1): # Começando por: 1 e terminando no numero determinado: num+1
        
        if num % cont == 0: # Se o numero dividido pelo contador de 1 ao numero for de resto 0
            print(f'{c["32"]}', end='') #Pinte o numero de verde
            tot += 1 # mais 1 para o total de divisão
        else: # caso contrario
            print(f'{c["31"]}', end='') # Pinte de vermelho
        
        print(f'{cont}',end=' ') #Informe os numeros até o determinado 
    
    print(f'{c["1"]}\nO numero {num} foi dividido {tot} vezes')
    
    if tot ==2: # Se o total for 2 ele é primo
        print(f'E por isso {c["32"]}É PRIMO!{c["l"]}')
    else: # caso controrio ñ
        print(f'E por isso {c["31"]}Não É PRIMO!{c["l"]}')

def Ex53():
    print('Palindromo')
    frase = input('Qual a frase: ').strip().upper()
    for analise in range(1):
        frase_list = frase.split()
        frase_junt =''.join(frase_list)
        frase_inv = ''
        for letra in range (len(frase_junt) -1, -1, -1):
            frase_inv += frase_junt[letra]
        #lembrete de rever a aula
        
        print(f'A frase {frase_junt} investida é {frase_inv}')
        if frase_inv == frase_junt:
            print('É um palidromo!')
        else:
            print('Não é um palidromo!')
        
        '''frase_inv = frase_junt[::-1] # [::-1] para inverer a ordem das letras
        print(f'O inverso da frase é {frase_inv}')
        if frase_inv == frase_junt:
            print('A frase é Palindrome:')
        else:
            print('A frase não é Palindrome:')'''

def Ex54():
    from datetime import date
    ano_atl = date.today().year
    maior = 0
    menor = 0
    print('Ano de nascimento')
    for nasc in range(1,8):
       
        nascim = int(input(f'Em que ano a {nasc}º pessoa nasceu: '))
     
        anos = ano_atl - nascim
        if anos < 21:
            menor += 1 
        else:
            maior += 1
    print(f'Ao todo tivemos {maior} pessoas de maior de idade')
    print(f'E também tivemos {menor} pessoas menores de idade')

def Ex55():
    print('Analize de peso')
    maior = 0
    menor = 0
    for p in range(1,6):
        Peso = float(input(f'Peso da {p}º pessoa: '))
        
        if p == 1:
            maior = Peso
            menor = Peso
        else:
            if Peso > maior:
                maior = Peso
            if Peso < menor:
                menor = Peso
    print(f'O maior peso foi de {maior}kg')
    print(f'O menor peso foi de {menor}kg') 
             
def Ex56():
    #A media de idade / fazer a soma de idades e dividir pela quantidade de pessoas
    somaidade = 0 #Soma de todas as idades
    media_idade = 0 #Media de idade
    # Homem mais velho
    nome_home = ''
    mais_homi = 0
    # Total de mulheres abaixo dos 20 anos
    totmuleres20 = 0
    for p in range(1, 5):
        print(f'---- {p}ª PESSOA ----')
        nome = input('Nome: ').strip()
        idade = int(input('Idade: '))
        sexo = input('Sexo [M/F]: ').strip()
        # Soma as idades
        somaidade += idade
        #Verificar o homem mais velhor
        if p ==1 and sexo in 'Mn': # Se for o primerio e for do sexo 'M'
            mais_homi = idade # o mais velhor sera o primero homem
            nome_home = nome # o nome do homem sera do primeiro homem
        if sexo in 'Mn' and idade > mais_homi: # Se a idade ainda for maior maior doq o primero homem sera alterada contendo que esteja no sexo 'M'
            mais_homi = idade # Altera para o mais velhor da lista
            nome_home = nome # Altera para o nome do homem da lista

        if sexo in 'Ff' and idade <20: # Se sexo for 'F' e a idade for menor que 20
            totmuleres20 += 1 # adicionar a lista das mulheres com menos de 20 anos +1
    
         
    media_idade = somaidade / 4 # Tira a media das idades
    print(f'A media de idade é {media_idade}anos') 
    print(f'O homem mais velhor é {nome_home} e tem {mais_homi} anos')    
    print(f'São {totmuleres20} mulheres abaixo de 20 anos')
#Mais Exercicios sobre For
def Ex01F():
    soma = 0
    for cont in range(0,11):
        soma += cont
    print(f'a soma dos numeros de 1 a 10 é :{soma}')

def Ex02F():
    lista_frutas = ['maça', 'banana', 'laranja', 'uva']
    for frutas in range(0, len(lista_frutas)):
        print(lista_frutas[frutas])

def Ex03F():
    print('Tabuada de 5')
    mult = 5
    for tab in range(1,11):
        result = mult * tab
        print(f'{mult} X {tab:2} = {result}')

def Ex01M():
    total = 0
    soma = 0
    num = int(input('Informe um numero: '))
    for pares in range(1, num +1):
        if pares % 2 == 0:
            print('\033[1;32m', end=' ')
            total += 1
            soma += pares
        else:
            print('\033[1;31m', end=' ')
        print(pares, end= ' ')
    print(f'\n\033[mSão {total} numeros pares')
    print(f'A soma de todos é {soma}')

def Ex02M():
    print()

def Ex03M():
    palavra = input('Qual a palavra: ').strip()
    palavra_inv = '' 
    for p in range(len(palavra)- 1, -1, -1): #inverter a palavra
        palavra_inv += palavra[p] # <-- [p] faz o menos processo do [::-1]
    print(palavra_inv)
            
def Ex01D():
    print('Numeros primos')
    num1 = int(input('Vai de: '))
    num2 = int(input('Até: '))
    
    for p in range(num1, num2+1):
        num = p
        if p != num2+1:
            total = 0
            for cont in range(1, num+1):
                
                if num % cont == 0:
                    total +=1

                if total ==2:
                    print('\033[1;32m', end='')
                else:
                    print('\033[1;31m', end='')
            print(f'{num}\033[m', end= ' ')
            
def Ex02D():
    n = int(input('Informe um numero: '))
    for triang in range (1, n+1):
        print('*'*triang)
         
if __name__ == "__main__":
    Ex02D()