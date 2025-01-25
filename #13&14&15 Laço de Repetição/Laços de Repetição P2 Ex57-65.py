def Teoria():
    # Form For
    '''for c in range(1, 10):
        print(c)
    print('Fim')'''
    # Form While
    # Pode ser usando tbm quando se sabe o limite 
    c =1
    while c <10:
        print(c)
        c += 1
    print('Fim')
    # Pode ser usando determinado o valor que vai ser o limite
    n =1
    while n != 0: #Determina o ponto de parada, quando for igual a 0
        n = int(input('Digite um valor: '))
    print('Fim')

    r = 'S'
    while r == 'S': # Determina o ponto de parada, quando for diferente se 'S'
        n = int(input('Digite uma valor: '))
        r = str(input('Deseja continuar [S/N]: ')).upper()
    print('Fim')

    
    n = 1
    pares = inps = 0
    while n != 0:
        n = int(input('Informe um numero: '))
        if n != 0:
            if n % 2 == 0:
                pares += 1
            else:
                inps += 1
    print(f'Você digitou {pares} pares e {inps} impares')

def Ex57():
    sexo = str(input('Qual seu sexo [M/F]: ')).strip().upper()[0] # <-- ler somente a primera letra
    
    while sexo not in 'FM': # Enquanto o sexo não é ''F' ou 'M' realizar...
        sexo = str(input('Informe um sexo valido, Qual seu sexo: ')).strip().upper()[0]
    if sexo == 'M':
        sexo = 'Masculino'
    if sexo == 'F':
        sexo = 'Feminino'
    print(f'Pronto, sexo registrado {sexo}')

def Ex58():
    from random import randint
    from time import sleep
    print('=-'* 20)
    print('Computador pensando em um numero...')
    print('=-'* 20)
    sleep (2)
    print('Já decidir!')
    
    num_esc_pc = randint(1,10) 
    num = int(input('Qual numero você acha que deve ser?\nDe 1 a 10: '))
    acertou = False
    tev = 0
    
    if num == num_esc_pc:
        print('Parabéns você acertou de primeira!')
        acertou = True
    elif num <1 or num >10:
        print('O numero deve ser de 1 a 10!')
    else:
        print('Tá errado!, tente novamente..')
    
    while not acertou:
        
        num = int(input('Qual você acha que deve ser: '))
        
        if num == num_esc_pc:
            acertou = True
        elif num < num_esc_pc:
            print('Mais.. Tente mais uma vez')
            tev += 1
        else:
            print('Menos.. Tente mais uma vez')
            tev += 1
        if num < 1 and num > 10:
            print('O numero deve ser de 1 a 10!')
            tev += 1
    if tev >1:      
        print('Parabéns você acertou!')
        print(f'O numero era {num_esc_pc}')
        print(f'Foi {tev+1} tentativas')

def Ex59():
    c = {
    'l':'\033[m',#limpa
    'n':'\033[1;37m',#negrito
    's':'\033[4;37m',#subliando
    '31':'\033[1;31m', #vemelho
    '32':'\033[1;32m',#verde
    '33':'\033[1;33m',#amarelo
    '34':'\033[1;34m',#azul
    '35':'\033[1;35m',#roxo
    '36':'\033[1;36m',#azul ciano
    }
    from time import sleep
    from os import system #modulo p. limpar a tela
    n =1
    print(f'{c["n"]}=-'*10)
    print(f'{c["35"]}{'Menu de operações':^20}')
    print(f'{c["n"]}=-'*10)
    n1 = int(input(f'{n}ª valor: '))
    n2 = int(input(f'{n+1}ª valor: '))
    print('Analizando..')
    sleep(1)
    
    op = [
        
        f'{c["n"]}=='*10,
        f'{c["35"]}{'Tabela ☑️':^22}',
        f'{c["n"]}=='*10,
        
        f'{'1️⃣  soma.':<12}{'6️⃣  menor'}',
        f'{'2️⃣  subt.':<12}{'7️⃣  elev.'}',
        f'{'3️⃣  mult.':<12}{'8️⃣  primo'}',
        f'{'4️⃣  divi.':<12}{'9️⃣  outros'}',
        f'{'5️⃣  maior ':<12}{'0️⃣  sair'}'
        
    ]
    opera = 1
    t =1
    
    while opera != 0:
        
        for ops in op:
            print(ops)
        
        print('__'*10)
        print(f'{c["35"]}{t}ª Teste ')
        t += 1
        opera = int(input(f'{c["n"]}Qual deseja 🙃: ')) 
        if opera != 0 and opera <= 9:
            print('=-'*10)
            print(f'{c["32"]}{'OPÇÃO':>10} {opera}✅{c["n"]}')
        print(f'--'*10)
        sleep(0.5)

        if opera <=8:
            if opera ==1:
                res1 = n1 + n2
                
                print(f'{c["35"]}Soma ➕\n{c["n"]}num1: {n1}\nnum2: {n2}') 
                print(f'{c["36"]}{n1} + {n2} = {res1}')
                
            elif opera ==2:
                res1 = n1 - n2
                res2 = n2 - n1
                print(f'{c["35"]}Subtração ➖\n{c["n"]}num1: {n1}\nnum2: {n2}') 
                print(f'{c["36"]}{n1} - {n2} = {res1}')
                print(f'{n2} - {n1} = {res2}')
                
            elif  opera ==3:
                res = n1 * n2
                print(f'{c['35']}Multiplicação ✖️\n{c["n"]}num1: {n1}\nnum2: {n2}') 
                print(f'{c["36"]}{n1} x {n2} = {res}')
                
            elif  opera ==4:
                res1 = n1 / n2
                res2 = n2 / n1
                print(f'{c["35"]}Divisão ➗\n{c['n']}num1: {n1}\nnum2: {n2}') 
                print(f'{c["36"]}{n1} / {n2} = {res1:.1f}')
                print(f'{n2} / {n1} = {res2:.1f}')
                
            elif opera ==5:
                print(f'{c["36"]}Maior 🔼{c["n"]}')
                if n1 > n2:
                    print(f'Núm. {n1} é maior que {n2}')
                elif n2 > n1:
                    print(f'Núm. {n2} é maior que {n1}')
                else: 
                    print('Os números são iguais')
                
            elif opera ==6:
                print(f'{c["36"]}Menor 🔽{c["n"]}')
                if n1 < n2:
                    print(f'Núm. {n1} é menor que {n2}')
                elif n2 < n1:
                    print(f'Núm. {n2} é menor que {n1}')
                else: 
                    print('Os números são iguais')
                
            elif  opera ==7:
                res1 = n1 ** n2
                res2 = n2 ** n1
                print(f'{c["35"]}Elevado 🔝\n{c["n"]}num1: {n1}\nnum2: {n2}') 
                print(f'{c["36"]}{n1} elevado a {n2} é {res1}')
                print(f'{n2} elevado a {n1} é {res2}')
                
            elif opera ==8:
                tot = 0
                for cont in range (1, n1+1):
                    if n1 % cont == 0:
                        tot += 1
                if tot == 2:
                    print(f'Número {c["32"]}{n1}{c["n"]} é primo!')
                else:
                    print(f'Número {c["31"]}{n1}{c["n"]} não é primo!')
                
                for cont in range (1, n2+1):
                    if n2 % cont == 0:
                        tot += 1
                if tot == 2:
                    print(f'Número {c["32"]}{n2}{c["n"]} é primo!')
                else:
                    print(f'Número {c["31"]}{n2}{c["n"]} não primo!')
        
        if opera != 0 and opera < 9:# tem que ser diferente de 0 p. fazer limpeza e abaixo de 9
            print(f'{c["n"]}=-'*10)
            p = input('Enter p. continuar..')
            sleep(1)
            system('cls') # limpa a tela    
        
        if opera ==9:
            print(f'{c["36"]}Outros valores 🔄️{c["n"]}')
            n1 = int(input(f'{n}ª valor: '))
            n2 = int(input(f'{n+1}ª valor: '))
            print('Analizando..')
            sleep(1)
            system('cls')

        elif opera > 9:
            print(f'{c['31']}Informe opção valida!{c["l"]}')
            sleep(2)
            system('cls')

        
    print(f'{c["36"]}Fim das operações! 😊')
    sleep(2)
    system('cls')
    print(f'{c["n"]}Qual nota p. programa? 🤭')

def Ex60():
    #Form Modulo
    from math import factorial
    print('Fatorial de um numero')
    num = int(input('Informe o numero: '))
    factor = factorial(num)
    print(f'O fatoria do {num} é {factor}')
    
    # Form for
    print('Fatorial de um numero')
    num = int(input('Informe o numero: '))
    factor =1
    print(f'{num}!',end=' ')
    for n in range(1, num+1):
        print(f' {n} ', end='x')
        factor *= n
    print(f' = {factor}')
   
   # Form While
    print('Fatorial de um numero')
    num = int(input('Informe o numero: '))
    c = num
    factor = 1
    print(f'{num}!',end= ' = ')
    while c > 0: # Enquanto contador menor que 0 fassa..
        print(c, end = '')
        if c > 1: # se contador for menor que 1 add igual '='
            print(end= ' X ')
        else:
            print(end= ' = ')
        factor *= c # factor = factor * contador
        c -= 1 # vai diminuir o contador
    print(factor)

def Ex61():
    print('\033[1;37m-='*14)
    print('\033[34mPROGRESSÃO ARITMETICA P.A v2')
    print('\033[1;37m-='*14)
    print('\033[37mOs 10 primeiros termos')
    a1 = int(input('Informe o primeiro termo: '))
    Razão = int(input('Qual a razão: '))
    print(f'Fomula: An = a1 + (n-1).r\n {a1}')
    a10 = 10
    PA = 2
    
    '''for c in range(a1, a10 + Razão, Razão):
        print(f'{c}', end=' ')'''
    
    #a10 = a1 + (10 - 1) * Razão
    '''for PA in range(1, 11):
        An = a1 + (PA - 1)*Razão
        print(f'\033[1;34mA{PA:2} \033[1;37m= {a1} + ({PA:2} - 1).{Razão} = \033[1;34mA{PA}: \033[4;37m{An}\033[m')'''

    while PA <= a10:
        an = a1 + (PA-1)*Razão
        PA +=1
        print(f'{an}', end= ' → ')  
    
    while PA <= a10:
        PA +=1
        print(f'{a1:2} + ({PA:2} - 1) x {Razão}: {an}')
    print('Fim')
    
    termo = a1
    contador = 1
    while contador <= a10:
        print(f'{termo}',end=' ')
        termo += Razão
        contador += 1
    print('Fim')


def Ex62():
    from time import sleep
    print('\033[1;37m-='*14)
    print('\033[36mPROGRESSÃO ARITMETICA P.A v3')
    print('\033[1;37m-='*14)
    a1= int(input('Informe o primeiro termo: '))
    Razão = int(input('Qual a razão: '))
    print('__'*14)
    print(f'Fomula: An = a1 + (n-1).r')
    Termo = a1
    pergunta = 10
    Total_term = 0
    print('\033[36mOs 10 primeiros termos\033[37m')
    
    while pergunta != 0:
        Total_term += pergunta
        contador = 1
        while contador <= pergunta:
            print(f'{Termo}', end=' → ')
            Termo += Razão
            contador += 1
        print('PAUSE')
        
        if pergunta == 10 and Total_term == 10:
            print('\033[36mPara encerra [0]!\033[37m')
            sleep(2)
        
        pergunta = int(input('Mais quantos termos deseja mostra: '))
    
    print('——'*14)
    print(f'\033[36mProgressão finalizada com {Total_term} termos mostrados\033[m')
   
    
def Ex63():
    print('\033[1;37m——'*14)
    print('\033[32mSequencia de Fibonacci v1\033[37m')
    print('——'*14)
    termina = int(input('Quatos termos você quer mostrar: '))
    contador = 3
    n1 = 0
    n2= 1
    print('∿∿'*14)
    print(f'{n1} → {n2}', end=' → ')
    while contador <= termina:
        contador +=1
        n3 = n1 +n2
        print(f'{n3}',end=' → ')
        n1 = n2
        n2 = n3
        
    print('FIM')
    print('∿∿'*14)
def Ex64():
    print('\033[1;37m——'*14)
    print(f'{'\033[33mSoma de valores\033[37m':^38}')
    print('——'*14)
    print('Finalizar programa: 999')
    n =1
    total_termo = soma = valor = 0
    valor = int(input(f'{n}ª valor: '))
    while valor != 999:
        total_termo += 1
        n += 1
        soma += valor
        valor = int(input(f'{n}ª valor: '))
    print('__'*14)
    print(f'\033[33mA soma de {total_termo} valores é {soma}\033[m')

def Ex65():
    print('Maior/Menor')
    n = 1
    cond = 'S'
    maior = menor = soma = todos = 0
    while cond == 'S':
        num = int(input(f'{n}ª valor: '))
        n += 1
        todos +=1
        soma += num
        if todos == 1: # se total de num. for 1ª, o maior e o menor sera o primeiro
            maior = menor = num
        else: # senão
            if num > maior: # se o num. for maior que o 1ª maior
                maior = num # o maior recebe esse outro num.
            if num < menor: # se o num for menor que o 1ª menor
                menor = num # o menor recebe esse outro num.
        cond = str(input('Continuar[S/N]: ')).strip().upper()[0]
    media = soma / todos
    print(f'Você digitou {todos} valores e a média foi {media}')
    print(f'O maior foi {maior} e o menor foi {menor}')
if __name__ == "__main__":
    Ex65()
    
    