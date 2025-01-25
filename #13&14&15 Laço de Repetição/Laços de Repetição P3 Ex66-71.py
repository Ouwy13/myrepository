def Ex66():
    print('Soma de valores')
    n = 1
    Soma = Total = 0
    while True:
        
        num = int(input(f'{n}ª valor: '))
        if num == 999:
            break
        n += 1
        Total += 1
        Soma += num
    print(f'A soma de {Total} valores é {Soma}!')
def Ex67():
    from time import sleep
    print('\033[1;37m∿∿'*10)
    print(f'{'\033[32mTabuada':^26}')
    print('\033[37m∿∿'*10)
    print('\033[31mvalor negativo p. PARAR\033[37m')
    while True:
        mult = int(input('Tabuada qual valor: '))
        if mult < 0:
            break
        cont = 1
        print('——'*10)
        while cont <= 10:
            result = mult * cont
            print(f'{mult} X {cont:2} = {result}')
            cont += 1
        print('——'*10)
        p = str(input('Enter continaur...'))
        sleep(2)
    print('\033[32mFim do programa 🙃\033[m')

def Ex68():
    from random import randint
    from time import sleep
    from os import system
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

    vitor = 0
    while True:
        while True:
            print(f'{c['n']}=-'*14) 
            print(f'{c["36"]}{'X1 Impar ou Par 🖥️':^28}')
            print(f'{c["n"]}-='*14) 
            valor = int(input('Diga um valor [1/10]: '))
            if valor > 0 and valor <= 10:
                break
            else:
                print(f'{c['31']}Valor de [1/10]..{c["n"]}')
                sleep(1)
                system('cls')
        while True:
            esc = str(input('Par ou Impar [P/I]: ')).strip().upper()[0]
            if esc in 'PI':
                break
            else:
                print(f'{c['31']}Escolha [P/I]..{c["n"]}')
                sleep(1)
        valor_pc = randint(1,10)
        total = valor + valor_pc
        vencedor = ''
        if esc == 'P':
            if total % 2 == 0:
                decisão = 'PAR'
                vencedor = 'Você'
                
        elif esc == 'I':
            if total % 2 ==1:
                decisão = 'IMPAR'
                vencedor = 'Você'
    
        print('——'*14)
        print(f'{c["36"]}Valores escolhidos{c["n"]}')
        print(f'🙍: {valor}  🖥️ : {valor_pc}')
        print(f'Total de {total} {c["s"]}DEU {decisão}{c["l"]}{c["n"]}')
        print('——'*14)
        if vencedor == 'Você':
            print(f'{c["32"]}Você ganhou!! 🤔{c["n"]}')
            vitor +=1
            p = input('Enter continuar..')
            sleep(1)
            system('cls')
        else:
            print(f'{c["31"]}Você perdeu!! 🖥️{c["n"]}')
            p = input('Enter continuar..')
            sleep(1)
            system('cls')
            break
    print(f'GAME OVER!', end='')
    if vitor == 1:
        print('Você venceu 1 vez')
    elif vitor > 1:
         print(f'Você venceu {vitor} vezes')

def Ex69():
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
    m18 = mm20 = homem = mulher = 0
    from time import sleep
    print(f'{c["n"]}∿∿'*10)
    print(f'{c["34"]}{'Cadastre de clientes'}')
    print(f'{c["n"]}∿∿'*10)
    while True:
        while True:
            idade = int(input(f'Idade: '))
            if idade <= 0:
                print(f'{c["31"]}Idade Invalida!{c["n"]}')
            else:
                break
        
        while True: 
            sexo = str(input('Sexo [M/F]: ')).strip().upper()[0] 
            if sexo in 'FM':
                break
            else:
                print(f'{c["31"]}Sexo invalido!!{c["n"]}')
        if idade > 18:
            m18 +=1
        if sexo == 'M':
            homem +=1
        if sexo == 'F':
            mulher +=1
        if sexo == 'F' and idade < 20:
            mm20 +=1
        while True:
            print('——'*10)
            cond = str(input('Continar [S/N]: ')).strip().upper()[0]
            if cond in 'SN':
                sleep(2)
                break
            else:
                print(f'{c["31"]}Codição [S/N]{c["n"]}')
        if cond == 'N':
            break
        else:
            print('=—'*10)
            print(f'{c["34"]}Proximo cadastro{c["n"]}')
            print('—='*10)
    print('--'*10)
    print(f'{c["34"]}FIM DO PROGAMA{c['n']}')
    print('--'*10)
    print(f'Total de maiores de 18 anos: {m18}')
    if homem ==1:
        print('Foi 1 homem cadastrado')
    elif homem >1:
        print(f'Foram {homem} homens cadastrados')
    else:
        print('Nem um homem cadastrado')
    if mulher ==1:
        print('Foi 1 mulher cadastrado')
    elif mulher >1:
        print(f'Foram {mulher} mulheres cadastrados')
    else:
        print('Nem um mulher cadastrado')
    if mm20 ==1:
        print(f'Temos {mm20} mulher com menos de 20 anos')
    elif mm20 >1:
        print(f'Temos {mm20} mulheres com menos de 20 anos')
    else:
        print('Nem uma mulher menor de 20 anos')
def Ex70():
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
    total = m1000 = soma = menor = 0
    barato = ''
    print(f'{c["n"]}∿∿'*10)
    print(f'{c['35']}{'Lojão do Zé 🤙':^20}{c['n']}')
    print('∿∿'*10)
    print(f'{c["32"]}Adicione produto 🛍️{c["n"]}')
    while True:
        produto = str(input('Nome produto: ')).strip()
        preço = float(input('Preço: R$'))
        soma += preço
        total +=1
        if preço > 1000:
            m1000 += 1
        '''if total == 1:
            menor = preço
            barato = produto
        else:
            if preço < barato:
                menor = preço
                barato = produto'''
        if total == 1 or preço < menor: # Mesma operação p. saber o mais barato
            menor = preço
            barato = produto

        while True:
            print('__'*10)
            cond = str(input('Continuar [S/N]: ')).strip().upper()[0]
            if cond in 'SN':
                break
            else:
                print(f'{c["31"]}Codição [S/N]..{c['n']}')
        if cond == 'N':
            break
    print('——'*12)
    print(f'Total de {total} é R${soma:.2f}')
    print(f'Temos {m1000} produtor mais de R$1000')
    print(f'O produto mais barato: {barato} de R${menor:.2f}')   
    sleep(2)
    print(f'{c["32"]}FIM DO PROGRAMA 😊{c["n"]}')

def Ex71():
    from time import sleep
    from os import system
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
    while True:
        print(f'{c["n"]}∿∿'*12)
        print(f'{c["32"]}{'Banco do Zé🤙 ':^24}')
        print(f'{c["n"]}∿∿'*12)
        op = [
            f'{c["36"]}Cedulas disponiveis 💰💸{c["n"]}',
            '💴-R$200 | 💶-R$100',
            '💴-R$50  | 💴-R$20',
            '💵-R$10  | 💷-R$5',
            '💶-R$2   |',
            f'❌-{c["33"]}Moedas🪙{c['n']}'
            ]
        for ops in op:
            print(ops)
        valor = int(input('Qual o valor: R$'))
        n = str(valor)
        n_ult = n[-1]
        v_ult = int(n_ult)
        print('Contando cedulas...')
        sleep(2)
        total = valor
        cedul = 200
        tot_cedul = 0
        nota = '💴'
        while True: 
            if v_ult % 2 == 1 and v_ult not in (5,7,9):
                print(f'{c["31"]}Não pode moedas!{c["n"]}')
                break
            if valor < 1:
                print(f'{c["31"]}Valor invalido!{c["n"]}')
                break
            if valor > 1000000:
                print(F'{c["31"]}Valor acima de 1000000 🤑{c["n"]}')
                print('Manda o pix 989999-9999 🤭')
                break
            if total >= cedul:
                total -= cedul
                tot_cedul += 1
            else:
                if tot_cedul >= 1:
                    print(f'{tot_cedul}-notas de R${cedul}{nota}')
                elif cedul == 200:
                    cedul = 100
                    nota = '💶'
                elif cedul == 100:
                    cedul = 50
                    nota = '💴'
                elif cedul == 50:
                    cedul = 20
                    nota = '💴'
                elif cedul == 20:
                    cedul = 10
                    nota = '💵'
                elif cedul == 10:
                    cedul = 5
                    nota = '💷'
                elif cedul == 5:
                    cedul = 2
                    nota = '💶'
                tot_cedul =0
                if total == 0:
                    break
        cond =' '
        while cond not in 'SN':
            cond = str(input(f'{c["36"]}Outro saque [S/N]:{c["n"]} ')).strip().upper()[0]
        if cond == 'S':
            print('Ok mais um Saque..🫡')
            sleep(2)
            system('cls')
        if cond == 'N':
            break
    print('Fim do Programa 😊')
if __name__ == "__main__":
    Ex71()