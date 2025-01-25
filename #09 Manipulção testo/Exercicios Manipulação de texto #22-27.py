def Ex22():
    nome = input('Digite seu nome: ').strip()
    List = nome.split()
    
    print('Analisando seu nome..')
    print(f'Seu nome em maiúsculas é {nome.upper()}')
    print(f'Seu nome em minúsculo é {nome.lower()}')
    #print(f"Seu nome tem ao todo {len(''.join(List))} letras")
    print(f'Seu nome tem ao todo {len(nome) - nome.count(' ')} letras') # Pode ser também assim sem tranforma em Lista
    # print(f'Seu primeiro nome tem {nome.find(' ')} letras')
    print(f'Seu primeiro nome é {List[0]} e contém {len(List[0])}')

def Ex23():
    num = int(input('Infome um numero: '))
    u = num // 1 % 10
    d = num // 10 % 10
    c = num // 100 % 10
    m = num // 1000 % 10
    print(f'Unidade: {u}')
    print(f'Dezena: {d}')
    print(f'Centena: {c}')
    print(f'Milhar: {m}')

def Ex24():
    cid = input('Informe o nome da cidade: ').strip()
    cid = cid.lower()
    if cid.count('santo', 0,6):
         print('Sua cidade começa "Santo"')
    else:
        print('Sua cidade não começa com "Santo"')

def Ex25():
    nome = input('Qual seu nome: ').strip()
    nome = nome.lower()
    if nome.count('silva') or 'silva' in nome:
        print('Seu nome Tem "Silva"')
    else:
        print('Seu nome não tem "Silva"')

def Ex26():
    frase = input('Digite uma Frase: ').strip()
    frase = frase.lower()
    print(f'Aparece a letra "a" {frase.count('a')} vezes')
    
    #print(f'A letra "a" aparece pela 1ºvez no index: {frase.find('a')}')
    print(f'A letra "a" aparece pela 1ºvez na posição: {frase.find('a')+1}')
    
    #print(f'A letra "a" aparece pela ultima vez no index: {frase.rfind('a')}')
    print(f'A letra "a" aparece pela ultima vez na posição: {frase.rfind('a')+1}')

def Ex27():
    nome = input('Qual seu nome: ')
    nome = nome.split()
    print(f'Seu primeiro nome: {nome[0]}')
    print(f'Seu ultimo nome: {nome[-1]}')
    
def A01():
    frase = input('Informe uma frase: ')
    frase_list = frase.split()
    print(f'Total de palavras {len(frase_list)}')
if __name__ == "__main__":
    A01()