def Teoria():

    # Manipulando Cadeias de Texto

    frase = 'Curos em Vidio Python'

    # Analize
    len(frase) # <-- vai ler a quandidade de caracter

    frase.count('o') # <-- vai ler a quantidade do caracter determinado

    frase.count('o', 0, 13) # <-- vai ler a quantidade do caracter determinado definido seu fatiamento
    frase.find('deo') # <-- vai informa quantas vezes ele encontrou começando da 1º letra

    'Curso' in frase # <-- vai informar em True ou False

    #Tranformação

    frase.replace('Python', 'de Android') # <-- Vai subistituir pela frase determinada

    frase.upper() # <-- Transforma em maiusculo

    frase.lower() # <-- Transforma em minusculo

    frase.capitalize() # <-- Transforma  em minusculo menos a 1º letra

    frase.title() # <--Transforma todo começo de frase em maiusculo

    frase2 = '   Aprenda Python  '

    frase2.strip() # <-- Remove todos os espaçamentos inuteis

    frase2.rstrip() # <-- remove os espaçamentos a do final

    frase2.lstrip() # <-- remove os espaçamentos a do começo

    #Divisão

    frase = 'Curos em Vidio Python'

    frase.split() # <-- Separa cada frase em uma item de uma lista recomeçando o index 

    # Junção

    '-'.join(frase) # junta a lista determinando o tipo de espaçamento

def pratica():
    frase = 'O Curso em Video Python'
    print(frase[::2])
    print(frase.lower().count('o'))
    print(len(frase))
    frase = frase.replace('Python','de Programação em Python')
    print(frase)
    print('Programação' in frase)
    print(frase.find('Curso'))
    dividido = (frase.split())
    print(dividido[1])

if __name__ == "__main__":
    Teoria()