def Teoria():
    # Dicionario definido como {}
    dados = dict()
    dados = {'nome':'Pedro','idade':25}
    
    # Retorno
    print(dados) # Todo o dicionario
    print(dados['nome']) # Vai retorna somente o nome
    print(dados['idade']) # Vai retorna idade
    
    # Adicionar Elementos
    dados['sexo'] = 'M' # Dados recebe 'sexo':'M'
    
    # Remover Elementos
    del dados['idade'] # Remover o 'idade'
    print(dados)

def Teoria2():
    filme = {'Titulo':'Star Wors',
             'Ano':1977,
             'Diretor':'George Lucas'
    }
    
    # Valores
    print(filme.values()) # Retorna todos os valores dentro da biblioteca
    '''(['Star Wors', 1977, 'George Lucas'])'''
    
    # Chaves
    print(filme.keys()) # Retorna todas aa keys da biblioteca
    '''(['Titulo', 'Ano', 'Diretor'])'''

    # Valores e chaves
    print(filme.items()) # Retorna Tudo da biblioteca

    # Laço de repetição com valores e chaves
    for keys, valor in filme.items():
        print(f'O {keys} é {valor}')
    # Saida
    '''O Titulo é Star Wors
    O Ano é 1977
    O Diretor é George Lucas'''
    
    # Pode ser criado uma lista com varias bibliotecas dentro
    dados = [
        {'Nome':'Ana','Idade':21,'Sexo':'F'},
        {'Nome':'Paulo','Idade':17,'Sexo':'M'},
        {'Nome':'José','Idade':16,'Sexo':'M'}
    ]
    print(dados) # Toda a lista
    print(dados[0]['Idade']) # Idade da pessoa do index 0 -> 21
    print(dados[2]['Sexo']) # Sexo da pessoa do index 2 -> M
    print(dados[1]['Nome']) # Nome da pessoa do index 1 -> Paulo

def Teoria3():
    dados = {'nome':'José','sexo':'M','idade':16}
    print(dados['nome']) # Exibir o nome
    print(f'O {dados["nome"]} tem {dados["idade"]} anos') # Exibição formatada
    print(dados.keys()) # Retorna todas as chaves
    print(dados.values()) # Retorna todos os valores
    print(dados.items()) # Retorna todos os itens
    
    # Exibição por laço
    for key in dados.keys(): # Para cada chave em dados
        print(key)
    
    for value in dados.values(): # Para cada valor em dados
        print(value)
    
    for key, value in dados.items(): # Para chaves e valores
        print(f'{key} = {value}')

    # Apaga item no dicionario
    del dados['sexo'] # Deletar 'sexo' 

    # Atribuir valores
    dados['nome'] = 'Cleber' # 'nome' passa a ser 'Cleber'
    dados['peso'] = 61 # Atribuir peso no dicionario
    print(dados)

def Teoria4():
    # Lista
    brazil = list()
    # Dicionarios
    estado1 = {
        'uf':'Maranhão','sigla':'MA'
    }
    estado2 = {
        'uf':'São Paulo','sigla':'SP'
    }
    # Adicionando dict a list
    brazil.append(estado1)
    brazil.append(estado2)
    
    print(brazil[0]['sigla']) # Exibição da uf da dict intex 0
    print(brazil[1]) # Exibição da dict index 0

def Teoria5():
    estado = dict()
    brazil = list()
    for c in range(0,2):
        estado['uf'] = str(input('Qual estado: '))
        estado['sigla'] = str(input('Qual a sigla: '))
        brazil.append(estado.copy()) # Obrigatorio criar uma copy para salva a dict em uma lsit
        # Da mesma forma se fosse um dado para uma lista [:]
    
    # Exibição
    print(brazil)
    # Forma formatada
    for estado in brazil:
        print(f'{estado['uf']} sua sigla é {estado['sigla']}')
    
    # Forma exibir valores
    for estado in brazil:
        for value in estado.values():
            print(value, end=' ')
        print()

    # Forma exibindo a chave e o valor
    for estado in brazil:
        for key, value in estado.items():
            print(f'Na chave {key} tem o valor {value}')

    # Ordena uma biblioteca
    # Biblioteca para ordenar dict
    from operator import itemgetter
    # Vai 'ordenar' a 'dict' atravez de seus valores
    rankig = sorted(brazil.items(), key=itemgetter(1), reverse=True)

def Ex90():
    print('—-'*10)  
    print('Analize de Media')
    print('-—'*10)
    dados = dict()
    while True:
        try:
            nome = str(input('Nome do Aluno: ')).strip().capitalize().split()[0]
            if nome.isalpha():
                dados['Nome'] = nome
                break
            else:
                print('Deve conter somente letras!')
        except IndexError:
            print('Informe o Aluno!')

    while True:
        try:
            media = float(input(f'Qual a Media de {dados["Nome"]}: '))
            if media >10:
                print('Media Invalida!')
            else:
                dados['Média'] = media
            break
        except ValueError:
            print('Somente Numeros!')

    if dados['Média'] < 4:
        dados['Situação'] = 'Reprovado⛔'
    elif dados['Média'] < 6:
        dados['Situação'] = 'Recuperação🔄'
    else:
        dados['Situação'] = 'Aprovado✅'
    
    print('——'*10)
    for key, value in dados.items():
        print(f'{key} é igual a {value}')
    
def Ex91():
    from random import randint
    from time import sleep
    # Biblioteca para ordenar dict
    from operator import itemgetter

    jogos = dict()
    rankig = list()
    print('•—'*12+'•')
    print(f'{'Jogo de dados':^25}')
    print('•—'*12+'•')
    print('> Valores Sortiados:')
    for c in range(1,5):
        jogos[f'Jogado {c}'] = randint(1,6)
    sleep(1)
    for key, value in jogos.items():
        print(f'{key} tirou {value} no dado')
        sleep(1)  
    print('——'*12+'—')
    print('>>Ranking dos Jogadores<<')
    print('——'*12+'—')
    # Ranking vai 'ordenar' a 'dict' atravez de seus valores
    rankig = sorted(jogos.items(), key=itemgetter(1), reverse=True) # forma decrescente
    for pos, jogos in enumerate(rankig):
            print(f'{pos+1}ª lugar {jogos[0]} com {jogos[1]}')
            sleep(1)

def Ex92():
    from datetime import date
    dados = dict()
    title = [
        '—•'*15,
        f'{'Analize de Aposentadoria 😊':^30}',
        '•—'*15
    ]
    for t in title:
        print(t)
    while True:
        try:
            nome = str(input('> Qual seu nome: ')).strip().title()
            if nome.replace(" ", "").isalpha():
                dados['Nome'] = nome
                break
            else:
                print('Somente letras!')
        except IndexError:
            print('Digite seu nome!')
    while True:
        while True:
            try:
                ano_nsc = int(input(f'• Que ano você nasceu {dados["Nome"].split()[0]}?: '))
                if ano_nsc >= date.today().year or ano_nsc < 1000:
                    print('Idade Invalida!')
                else:
                    idade = date.today().year - ano_nsc
                    if idade < 18:
                        cond = str(input(f'> Você tem {idade} anos? [S/N]: ')).strip().upper().split()[0]
                        if cond == 'S':
                            print('——'*15)
                            print('Ainda não pode ultilizar  programa!')
                            break
                break
            except ValueError:
                print('Somente a idade!')
        dados['Idade'] = idade
        break

    if idade >= 18:
        while True:
            dados['CTPS'] = int(input('• Carteira de Trabanho [0 não tem]: '))
            if dados['CTPS'] == 0:
                break
            
            while True:
                try:
                    dados['Contrato'] = int(input('• Qual ano de contratação: '))
                    if dados['Contrato'] >= date.today().year or dados['Contrato'] < 1000 or dados['Contrato'] <= ano_nsc:
                        print('Ano Invalida!')
                    else:
                        break
                except ValueError:
                    print('Informe o Ano!')
            
            while True:
                try:
                    dados['Salário'] = float(input('• Qual salário: R$'))
                    break
                except ValueError:
                    print('Somente Numeros!')
            dados['Aposentadoria'] = (35 -(date.today().year - dados['Contrato']))+idade
            break
    print('——'*15)
    #print(dados)
    for key, value in dados.items():
        print(f'{key} tem o valor {value}') 
    
def Ex93():
    jogador = dict()
    gols = list()
    from time import sleep
    title = [
        '∿∿'*15,
        f'{'Partidas Futebol 🥳⚽':^30}',
        '∿∿'*15
    ]
    for t in title:
        print(t)
    while True:
        nome = str(input('Nome do jogador: ')).strip().title()
        if nome.replace(" ", "").isalpha():
            jogador['Nome'] = nome
            break
        else:
            print('Informe o nome!')
    while True:
        try:    
            partidas = int(input(f'Quantas partidas {jogador["Nome"].split()[0]} jogou: '))
            break
        except ValueError:
            print('Somente Numero!')
    print('——'*15)
    for c in range(1, partidas+1):
        while True:
            try:
                jogos = int(input(f'Quantos gols partida {c}: '))
                break
            except ValueError:
                print('Informe somente numeros!')
        gols.append(jogos)
    jogador['Gols'] = gols.copy()
    total = 0
    #for jogo in jogador['Gols']:
        #total += jogo
    #jogador['Total'] = total
    jogador['Total'] = sum(gols)
    print('——'*15)
    print(jogador)
    sleep(1)
    print('——'*15)
    
    
    for key, value in jogador.items():
        print(f'No campo {key} tem o valor {value}')
        sleep(0.5)
    print('——'*15)
    sleep(0.5)

    print(f'O jogador {jogador['Nome']} jogou {partidas} partidas')
    for pos,gols in enumerate(jogador['Gols']):
        print(f' -> Na partida {pos+1}, fez {gols} gols')
        sleep(0.5)
    print(f"Foi um total de {jogador['Total']} gols")
    sleep(0.5)

def Ex94():
    cadastrados = list()
    dados = dict()
    cont = 1
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
    title = [
        f'{c["n"]}∿∿'*15,
        f'{c["33"]}{'Analize de Cadastro🤔':^30}',
        f'{c["n"]}∿∿'*15
    ]
    for t in title:
        print(t)
    while True:
        while True:
            dados['Nome'] = str(input(f'{c["33"]}>{c["n"]} {cont}ª Nome:{c["33"]} ')).strip().title()
            if dados['Nome'].replace(" ", "").isalpha():
                break
            else:
                print(f'{c["31"]}Somente letras!{c["n"]}')
        cont +=1
        while True:
            try:
                dados['Sexo'] = str(input(f'{c["33"]}•{c["n"]} Sexo [M/F]:{c['33']} ')).strip().upper().split()[0]
                if dados['Sexo'] in 'FM':
                    break
                else:
                    print(f'{c['31']}Sexo Invalido!{c['n']}')
            except IndexError:
                print(f'{c['31']}Informe o Sexo!{c['n']}')
            
        while True:
            try:
                dados['Idade'] = int(input(f'{c["33"]}•{c["n"]} Idade:{c["33"]} '))
                break
            except ValueError:
                print(f'{c["31"]}Somente Numeros!{c["n"]}')
        while True:
            try:
                cond = str(input(f'{c["33"]}>{c["n"]} Continuar {c["33"]}[S/N]{c["n"]}: ')).strip().upper().split()[0]
                if cond in 'SN':
                    break
                else:
                    print(f'{c["31"]}Condição [S/N]!{c["n"]}')
            except IndexError:
                print(f'{c["31"]}Informe [S/N]!{c["n"]}')
        cadastrados.append(dados.copy())
        dados.clear()
        
        if cond == 'N':
            break
        print('——'*10)
    
    #print(cadastrados)
    print('——'*20)
    print(f'{c["33"]}>{c["n"]} O grupo tem {c["33"]}{len(cadastrados)}{c["n"]} pessoas')
    
    tot = 0
    for dado in cadastrados:
        tot += dado['Idade']
    med = tot / len(cadastrados)
    print(f'{c["33"]}•{c["n"]} A média de idade é de {c["33"]}{med:.2f}{c["n"]} anos')

    print(f'{c["33"]}•{c["n"]} As mulheres cadastradas: ',end='')
    for dado in cadastrados:
        if dado['Sexo'] == 'F':
            print(f'{c["33"]}{dado['Nome']}{c["n"]},', end=' ')
    
    print(f'\n{'——'*20}')
    print(f'> {c["33"]}Lista pessoas acima da média: {c["n"]}')
    for dado in cadastrados:
        if dado['Idade'] > med:
            for key , value in dado.items():
                print(f' {key} {c["33"]}:{c["n"]} {value}{c["33"]}|{c["n"]} ',end='')
            print('\n',end='')
    print('——'*20)
    print(f'{f'>>> {c["33"]}FIM DO PROGRAMA 😊{c["n"]} <<<':^54}')        

def Ex95():
    jogador = dict()
    gols = list()
    jogadores = list()
    cont = 1
    from time import sleep
    from os import system
    from operator import itemgetter
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

    title = [
        f'{c["n"]}∿∿'*15,
        f'`{c["32"]}{'Partidas Futebol 🏟️ 🥳🎉':^30}{c["n"]}',
        '∿∿'*15
    ]
    while True:
        for t in title:
            print(t)
        while True:
            nome = str(input(f'{c['32']}{cont}ª{c['n']} jogador: ')).strip().title()
            if nome.replace(" ", "").isalpha():
                jogador['Nome'] = nome
                break
            else:
                print(f'{c['31']}Informe o nome!{c['n']}')
        cont +=1
        while True:
            try:    
                partidas = int(input(f'{c['32']}•{c['n']} Partidas que {jogador["Nome"].split()[0]} jogou:{c['32']} '))
                break
            except ValueError:
                print(f'{c['31']}Somente Numero!{c['n']}')
        print(f'{c['n']}—•'*15)
        for v in range(1, partidas+1):
            while True:
                try:
                    jogos = int(input(f'{c["32"]}›{c["n"]} Gols da {v}ª partida:{c["32"]} '))
                    break
                except ValueError:
                    print(f'{c['31']}Informe somente numeros!{c['n']}')
            gols.append(jogos)
        print(f'{c["n"]}•—'*15)
        jogador['Gols'] = gols.copy()
        jogador['Total'] = sum(gols)
        gols.clear()
        jogadores.append(jogador.copy())
        jogador.clear()
        while True: 
            try:
                cond = str(input(f'{c["32"]}>{c["n"]} Continuar {c["32"]}[S/N]{c["n"]}: ')).strip().upper().split()[0]
                if cond in 'SN':
                    break
                else: 
                    print(f'{c["31"]}Condição [S/N]!{c["n"]}')
            except IndexError:
                print(f'{c["31"]}Informe a Condição!{c["n"]}')
            
        system('cls')
        if cond == 'N':
            break

    res = [
        f'{c['n']}—•'*20,
        f'{c["32"]}{'Tabela da Colocação 👕🏅':^40}{c['n']}',
        '•—'*20
    ]
    
    
    # Ordena dict atravez dos valores de 'Total'
    jogadores.sort(key=lambda x: x["Total"], reverse=True)
    
    while True:
            c = {
                
                'n':'\033[1;37m',#negrito
                '31':'\033[1;31m', #vemelho
                '32':'\033[1;32m',#verde
                '33':'\033[1;33m',#amarelo
            }
            for r in res:
                print(r)
            print(f'{c["32"]}>{c["n"]} Colocação dos {len(jogadores)} jogadores 🔥')
            print('——'*20)
            print(f' {c['33']}{' Nª'}{'Nome':>6}{'Total':>10}{'Gols':>9}{c['n']}')
            print('——'*20) 
            def medalha(lugar):
                if lugar == 0:
                    return ' 🥇'
                elif lugar == 1:
                    return ' 🥈'
                elif lugar == 2:
                    return ' 🥉'
                else:
                    return f' {lugar+1}ª'
            for pos, jogador in enumerate(jogadores):
                print(f'{medalha(pos)} {c['32']}>{c['n']} {jogador['Nome'].split()[0][:7]:<9}{c['32']}•{c['n']} {jogador['Total']:<8}{jogador['Gols']}')  
            print(f' 0ª {c['32']}>{c['n']} Finalizar programa')
            print('—-'*20)
            
            while True:
                try:
                    cond = int(input(f'{c['32']}>{c['n']} Dados de qual jogador:{c['32']} '))
                    if cond > len(jogadores):
                        print(f'{c['31']}Jogador {cond} não registrado!{c['n']}')
                    else:
                        break
                except ValueError:
                    print(f'{c['31']}Somente numeros!{c['n']}')
            if cond == 0:
                print(f'{f'{c['32']}>>>>{c['n']} FIM DO PROGRMA😊 {c['32']}<<<<{c['n']}'}')
                break
            system('cls')
            print(f'{c['n']}—›'*20)
            print(f'{c['33']}{f'Levantamento jogador {jogadores[cond-1]['Nome']}🚀':^40}{c['n']}')
            print('‹—'*20)
            for pos, partida in enumerate(jogadores[cond-1]['Gols']):
                print(f'{c['33']}•{c['n']} Partida {pos+1} fez {c['33']}{partida}{c['n']} gols')
            print('—-'*20)
            c = str(input(f'{c['33']}>{c['n']} Enter continuar...'))
            system('cls')



if __name__ == "__main__":
    Ex95()  