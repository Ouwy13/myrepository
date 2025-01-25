def Ex36():
    # Valor da casa / Pelas parcelas dos anos determinado
    # Parcela = Vai ter que paga tanto todo mês
    # Cada parcela não deve ultrapassar 30% do salario
    from time import sleep

    print('-='*10)
    print('\033[1;36mFINANCIAMETO DE CASA\033[m')
    print('=-'*10)
    Valor = float(input('Valor da casa: R$'))
    Salario = float(input('Seu salario: R$'))
    Anos = int(input('Quantos anos: '))
    print('PROCESSANDO...')
    sleep(2)
    #1 calcular o valor da parcela
    ''' Anos x 12meses = (n) <-- Numeros de meses de pagamento
        PTM = Valor / n
    Pagamento total Mensal R$: PMT'''
    #2 calcular se o cliente pode financiar 30%
    ''' PM = 0.30 x salario
        PTM <= PM'''
    Presta = Anos * 12
    PTM = Valor / Presta
    PMP = 0.30 * Salario
    if PTM <= PMP:
        print('--'*20)
        print('O financiamento de R${:.2f} em {}anos'.format(Valor, Anos))
        print('\033[32mPODE SER FINANCIADA!!\033[m')
        print('Cada parcela ficará \033[4mR${:.2f}\033[m Mensalmente'.format(PTM))
        print('Sua renda de R${:.2f} é compativel :)'.format(Salario))
        print('--'*20)
    else:
        print('--'*20)
        print('O financiamento de R${:.2f} em {}anos'.format(Valor, Anos))
        print('\033[31mNÃO PODE SER FINANCIADA!!\033[m')
        print('Cada parcela ficará \033[4mR${:.2f}\033[m Mensalmente'.format(PTM))
        print('Renda de R${:.2f} não é compativel :('.format(Salario))
        print('--'*20)

def Ex37():
    print('-='*10)
    print(f'{'Conversão de base':^19}')
    print('=-'*10)
    num = int(input('Informe um numero: '))
    print(f'{'__'*10}')
    print(f'{'Tabela de Conversão':^20}') 
    ops = [
        f'[ 1 ] BINÁRIO',
        f'[ 2 ] OCTAL',
        f'[ 3 ] HEXADECIMAL'
    ]
    for op in ops:
        print(f'{op}') 
    esc = int(input('Sua opção: '))
    if esc == 1:
        print(f'Convertido será: {bin(num)[2:]}')
    elif esc == 2:
        print(f'Convertido será: {oct(num)[2:]}')
    elif esc == 3:
        print(f'Convertido será: {hex(num)[2:]}')
    else:
        print('Informe opção valido!!!')

def Ex38():
    n1 = int(input('Primeiro valor: '))
    n2 = int(input('Segundo valor: '))
    if n1 > n2:
        print(f'Valor {n1} é maior')
        print(f'Valor {n2} é menor')
    elif n2 > n1:
        print(f'Valor {n2} é maior')
        print(f'Valor {n1} é menor')
    else:
        print(f'Valores são iguais')
    
def Ex39():
    from datetime import date
    from emoji import emojize
    print('--'*14)
    print(emojize('ALISTAMENTO MILITAR :bandeira_brasil: :capacete_militar: ', language='pt'))
    print('--'*14)
    Ano = int(input('Qual seu ano de nascimento: '))
    Ano_Atual = (date.today().year)
    idade = Ano_Atual - Ano
    
    if idade == 18:
        print('\033[1;37mHora de se Alistar!!\033[m')
        print(emojize('Ao serviço militar :medalha_militar:', language='pt'))
    elif idade < 18:
        ano_rest = 18 - idade
        print('\033[1;33mAinda vai se Alistar..\033[m')
        print(f'\033[1;37mFalta {ano_rest} ano para prestar..\033[m')
        print(emojize('Ao Serviço militar :medalha_militar:', language='pt'))
        print(f'Alistamento em {Ano_Atual + ano_rest}')
    
    elif idade > 18:
        pendecia = idade - 18
        print('\033[1;31mPassou do tempo!!\033[m')
        print(f'\033[1;37m{pendecia} anos de pendencia..\033[m')
        print(f'Seu alistamento foi em {Ano_Atual - pendecia}')
        print('\033[4mProcure auxilio militar\033[m..')

def Ex40():
    from emoji import emojize
    print(emojize('\033[1;37mSoma de médias\033[m :escrevendo_à_mão:', language= 'pt'))
    n1 = float(input('Primeira nota: '))
    n2 = float(input('Segunda nota: '))
    M = (n1 + n2)/2
    if M > 5 and M <6.9:
        print(emojize('\033[31mRecuperação!!\033[m :rosto_desapontado:', language= 'pt'))
    elif M >= 7:
        print(emojize('\033[1;32mAprovado!!\033[m :rosto_risonho_com_olhos_sorridentes:', language= 'pt'))
    else:
        print(emojize('\033[1;31mReprovado!!\033[m :rosto_implorando:', language= 'pt'))
    print('Média final: {:.1f}'.format(M))

def Ex41():
    from emoji import emojize
    from datetime import date
    print('__'*16)
    titulo = 'Categoria p. Atletas :medalha_esportiva:'
    print(emojize('\033[1;37m{:^48}\033[m'.format(titulo), language= 'pt'))
    print('__'*16)
    Nasc = int(input('Qual sua data de nacimento: '))
    Ano_Atl = date.today().year
    idade = Ano_Atl - Nasc

    print(f'Vocé tem \033[4m{idade}anos\033[m')
    if idade <= 9:
        print('\033[1;36mMIRIM\033[m')
    elif idade <= 14:
        print('\033[1;34mINFANTIL\033[m')
    elif idade <= 19:
        print('\033[1;33mJUNIOR\033[m')
    elif idade == 25:
        print('\033[1;32mSÊNIOR\033[m')
    else:
        print('\033[1;35mMASTER\033[m')

def Ex42(): 
    # EX35 aprimorada
    print('=-'*12)
    print('\033[1;37mAnalisador de Triângulos\033[m')
    print('=-'*12)
    v1 = float(input('Primeiro valor: '))
    v2 = float(input('Segundo valor: '))
    v3 = float(input('Terceiro valor: '))
    

    if v1 < v2 + v3 and v2 < v1 + v3 and v3 < v1 + v2:
        print('\033[1;32mPODE FORMAR um triângulo\033[m')
        if v1 == v2 ==v3:
            print('\033[1;37mTRIÂNGULO EQUILÁTERO\033[m')
        elif v1 != v2 != v3 != v1:
            print('\033[1;37mTRIÂNGULO ESCALENO\033[m')
        else:    
            print('\033[1;37mTRIÂNGULO ISÓSCELES\033[m')
        print('Se a soma de dois lados forem maior ou igual ao terceiro lado.\nPode ser possivel fazer um \033[4mtriângulo\033[m!')

    else:
      print('\033[1;31mNÃO PODE FORMAR um triângulo\033[m')
      print('Se a soma de dois lados forem menor ao terceiro lado.\nNão é possivel fazer um \033[4mtriângulo\033[m!')

def Ex43():
    from emoji import emojize
    print('-'*20)
    print(emojize('\033[1;37mSeu IMC e status\033[m :bíceps:', language= 'pt'))
    print('-'*20)
    P = float(input('Qual seu peso: '))
    A = float(input('Qual sua altura: '))
    IMC = P / (A**2)
    
    if IMC < 18.5:
        Status = ('Abaixo do Peso')
    elif 18.5 <= IMC < 25:
        Status = ('Peso ideal')
    elif 25 <= IMC < 30:
        Status = ('Sobrepeso')
    elif 30 <= IMC < 40:
        Status = ('Obersidade')
    else:
        Status = ('Obersidade mórbida')
    print(f'O seu IMC: {IMC:.1f}')
    print(f'Status: \033[4m{Status}\033[m!!')

def Ex44():
    from time import sleep
    from emoji import emojize
    c = {
        'l':'\033[m',
        '31':'\033[31m',
        '32':'\033[32m',
        '33':'\033[33m',
        '34':'\033[34m',
        '35':'\033[1;35m',
        '36':'\033[36m',
        '37':'\033[37m',
        '4':'\033[4m',
        '1':'\033[1;37m'
    }
    
    p = 'Pagamento :sacolas_de_compras:'
    print('=-'*10)
    print(emojize('\033[1;37m{:^38}\033[m'.format(p), language='pt'))
    print('=-'*10)  
    v = float(input(f'{c["1"]}Valor das compras R$: '))
    print(emojize(f'{c["l"]}\033[1;32mFormas de pagamento\033[m :marca_de_seleção_branca:', language='pt'))
    '''Formas de pagamento ✅'''
    
    print(emojize(f'{c["1"]}1{c["l"]}-À vista {c["34"]}dinheiro/cheque :dinheiro_voando:{c["l"]}\n{c["33"]}10%{c["l"]} {c["4"]}desconto{c["l"]}',language='pt'))
    ''' 1-À vista dinheiro/cheque 💸
        10% desconto'''
    
    print(emojize(f'{c["1"]}2{c["l"]}-À vista no {c["34"]}cartão{c["l"]} :cartão_de_crédito:\n{c["33"]}15%{c["l"]} {c["4"]}desconto{c["l"]}',language='pt'))
    ''' 2-À vista no cartão 💳
        15% desconto'''
    
    print(emojize(f'{c["1"]}3{c["l"]}-{c["34"]}Cartão 2x{c["l"]} :cartão_de_crédito:\n{c["4"]}Preço{c["l"]} {c["4"]}normal{c["l"]}',language='pt'))
    ''' 3-Cartão 2x 💳
        Preço normal'''
    
    print(emojize(f'{c["1"]}4{c["l"]}-{c["34"]}Cartão 3x ou mais{c["l"]} :cartão_de_crédito:\n{c["33"]}20%{c["l"]} {c["4"]}de{c["l"]} {c["4"]}juros{c["l"]}',language='pt'))
    ''' 4-Cartão 3x ou mais 💳
        20% de juros'''
    esc = int(input(f'{c["1"]}Qual sua escolha:{c["1"]} ')) #Qual sua escolha: 
    print(f'{c["l"]}PROCESSANDO...')
    sleep(2)

    if esc == 1:
        desc = v - (v * 10/100)
        print(emojize(f'{c['35']}DESCONTO APLICADO{c['l']} {c['33']}10%{c['l']} :caixa_de_seleção_marcada_com_tique:',language='pt'))
        '''DESCONTO APLICADO 10% ☑️'''
        print('{}A vista por R$: {}{:.2f}{}'.format(c['1'],  c['4'], desc, c['l']))
        '''A vista por R$: 108.00'''
    elif esc ==2:
        desc = v - (v * 15/100)
        print(emojize(f'{c['35']}DESCONTO APLICADO{c['l']} {c['33']}15%{c['l']} :caixa_de_seleção_marcada_com_tique:', language='pt'))
        '''DESCONTO APLICADO 15% ☑️'''
        print('{}A vista no cartão por R$: {}{:.2f}{}'.format(c['1'], c['4'], desc, c['l']))
        '''A vista no cartão por R$: 102.00'''
    elif esc == 3:
        desc = v
        print(emojize(f'{c["35"]}Preço Atual{c["l"]} :caixa_de_seleção_marcada_com_tique:', language='pt'))
        '''Preço Atual ☑️'''
        print('{}No cartão 2x por R$: {}{:.2f}{}'.format(c['1'], c['4'], desc, c['l']))
        '''No cartão 2x por R$: 120.00'''
    elif esc == 4:
        print(emojize(f'{c["33"]}20% de Juros{c['l']} :caixa_de_seleção_marcada_com_tique:', language='pt'))
        '''20% de Juros ☑️'''
        q = int(input(f'{c['36']}Quantas parcelas: '))
        '''Quantas vezes x: '''
        desc = v + (v * 20/100)
        print('{}{}No cartão {}x por R$: {}{:.2f}{}'.format(c['l'], c['1'], q, c['4'], desc, c['l']))
        '''No cartão 12x por R$: 144.00'''
    else:
        print(f"{c['31']}Opção inválida!{c['l']}")
        exit()
    
def test():
    opcoes = [
        f"1 - À vista dinheiro/cheque - 10% desconto",
        f"2 - À vista no cartão :cartão_de_crédito: - 15% desconto",
        f"3 - Cartão 2x :cartão_de_crédito: - Preço normal",
        f"4 - Cartão 3x ou mais :cartão_de_crédito: - 20% de juros"
    ]
    for opcao in opcoes:
        print('''emojize'''(opcao, language='pt'))
        '''
        :mão_aberta_com_os_dedos_separados:
        :mão_em_v_de_vitória:
        :punho_levantado:
        :botão_vs:
        :rosto_contente_com_olhos_sorridentes:
        :rosto_desapontado:
        :rosto_franzido_com_boca_aberta:
        :pedra:
        :página_voltada_para_cima:
        :tesoura:
        :troféu:
        :aperto_de_mãos:
           '''

def Ex45():
    from random import randint
    from time import sleep
    cor = {
        'l':'\033[m',
        '31':'\033[31m',
        '32':'\033[32m',
        '33':'\033[33m',
        '34':'\033[1;34m',
        '35':'\033[1;35m',
        '36':'\033[36m',
        '37':'\033[37m',
        '4':'\033[4m',
        '1':'\033[1;37m'
    }
    
    print(f'{cor["1"]}=-'*12)
    print(f'{cor["34"]}{'Jokenpô 💻':^23}')
    print(f'{cor["1"]}-='*12)
    print(f'{'X1 COM O PC 😌':^24}')
    opcoes = [
        f'1️⃣  Pedra 🪨',
        f'2️⃣  Papel 📄',
        f'3️⃣  Tesoura ✂️{cor["l"]}'
    ]
    for opcao in opcoes:
        print(opcao)
    
    esc = int(input(f'{cor['34']}Qual sua escolha: '))
    if esc < 4:
        print(f'{cor["1"]}🧑🆚💻...')
        sleep(1)
        print('JO')
        sleep(1)
        print('KEN')
        sleep(1)
        print(f'PO!!!{cor["l"]}')
        sleep(1)
        esc_pc = randint(1,3)
        # 1 Pedra ✊
        # 2 Papel 🖐️
        # 3 Tesoura ✌️

        if esc_pc == 1: # Pedra
            if esc == 1: #pedra
                pc = 'Pedra ✊'
                jogado = 'Pedra ✊'
                vencedor = 'Empate 🤝'
            if esc == 2: #papel
                pc = 'Pedra ✊'
                jogado = 'Papel 🖐️'
                vencedor = 'Jogador 🧑🏆'
            if esc == 3: #tesoura
                pc = 'Pedra ✊'
                jogado = 'Tesoura ✌️'
                vencedor = 'PC 💻💥'
    
        elif esc_pc == 2: #Papel
            if esc == 1: #pedra
                pc = 'Papel 🖐️'
                jogado = 'Pedra ✊'
                vencedor = 'PC 💻💥'
            if esc == 2: #papel
                pc  = 'Papel 🖐️'
                jogado = 'Papel 🖐️'
                vencedor = 'Empate 🤝'
            if esc == 3: #tesoura
                pc = 'Papel 🖐️'
                jogado = 'Tesoura ✌️'
                vencedor = 'Jogador 🧑🏆'
        
        elif esc_pc == 3: #Tesoura
            if esc == 1: # pedra
                pc = 'Tesoura ✌️'
                jogado = 'Pedra ✊'
                vencedor = 'Jogador 🧑🏆'
            if esc ==2: # papel
                pc = 'Tesoura ✌️'
                jogado = 'Papel 🖐️'
                vencedor = 'PC 💻💥'
            if esc ==3: # tesoura
                pc = 'Tesoura ✌️'
                jogado = 'Tesoura ✌️'
                vencedor = 'Empate 🤝'
        
        print(f'{cor["1"]}__'*14)
        print(f'Sua escolha🧑: {jogado}')
        print(f'Escolha do PC💻: {pc}')
        print('__'*14)
        if vencedor == 'PC 💻💥' or vencedor == 'Jogador 🧑🏆':
            print(f'Vencedor: {vencedor}{cor["l"]}')
        else:
            print(f'Deu {vencedor}{cor["l"]}')  
    else:
        print(f'{cor["31"]}Valor invalido!!!{cor["l"]}')
if __name__ == "__main__":
    Ex45()