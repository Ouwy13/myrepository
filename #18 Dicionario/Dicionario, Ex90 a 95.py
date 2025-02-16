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
    del dados['idade'] # Remover o 'sexo'
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
    
    # Pode ser cirado uma lista com varias bibliotecas dentro
    locadora = [
        {'Titulo':'Star Wors','Ano':1977,'Diretor':'George Lucas'},
        {'Titulo':'Avangers','Ano':2012,'Diretor':'Joss Whedon'},
        {'Titulo':'Matrix','Ano':1999,'Diretor':'Wachonwski'}
    ]
    print(locadora) # Toda a lista
    print(locadora[0]['Ano']) # Ano do filme do index 0 -> 1977
    print(locadora[2]['Titulo']) # Titulo do filme do index 2 -> Matrix

def Teoria3():
    pessoas = {'nome':'José','sexo':'M','idade':16}
    print(pessoas['nome']) # Exibir o nome
    print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos') # Exibição formatada
    print(pessoas.keys()) # Retorna todas as chaves
    print(pessoas.values()) # Retorna todos os valores
    print(pessoas.items()) # Retorna todos os itens
    
    # Exibição por laço
    for key in pessoas.keys(): # Para cada chave em pessoas
        print(key)
    
    for value in pessoas.values(): # Para cada valor em pessoas
        print(value)
    
    for key, value in pessoas.items(): # Para chaves e valores
        print(f'{key} = {value}')

    # Apaga item no dicionario
    del pessoas['sexo'] # Deletar 'sexo' 

    # Atribuir valores
    pessoas['nome'] = 'Cleber' # 'nome' passa a ser 'Cleber'
    pessoas['peso'] = 61 # Atribuir peso no dicionario
    print(pessoas)

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
    
    print(brazil[0]) # Exibição da dict index 0
    print(brazil[0]['uf']) # Exibição da uf da dict intex 0

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
    rankig = sorted(jogos.items(), key=itemgetter(1), reverse=True)
    for pos, jogos in enumerate(rankig):
            print(f'{pos+1}ª lugar {jogos[0]} com {jogos[1]}')
            sleep(1)

def Ex92():
    print()
if __name__ == "__main__":
    Ex91()