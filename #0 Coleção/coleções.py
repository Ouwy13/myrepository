#Coleção Lista []
def teoria():
    frutas = ['Maçã', 'Melancia', 'Banana', 'Uva', 'Pera', 'Abacaxi']

# Retorno pelo index
def retorno_index():
    frutas = ['Maçã', 'Melancia', 'Banana', 'Uva', 'Pera', 'Abacaxi']
    print(frutas[0]) # '[]' dentro de '()' retorna o index

#Retorno pela quantidade
def retorno_quant():
    frutas = ['Maçã', 'Melancia', 'Banana', 'Uva', 'Pera', 'Abacaxi']
    print(frutas[:4]) # Retorno da quantidade determinada 

# len & .index
def len():
    frutas = ['Maçã', 'Melancia', 'Banana', 'Uva', 'Pera', 'Abacaxi']
    print(len(frutas)) # Retorna a quantidade 'len'
def index():
    frutas = ['Maçã', 'Melancia', 'Banana', 'Uva', 'Pera', 'Abacaxi']
    print(frutas.index('Abacaxi')) # Retorna a possição do item

# .count
def count():
    frutas = ['Maçã', 'Melancia', 'Banana', 'Uva', 'Pera', 'Abacaxi', 'Banana', 'Banana']
    print(frutas.count('Banana')) # Retorna a quantidade de determidado item '.count'

# Verificação
def Verificao():
    frutas = ['Maçã', 'Melancia', 'Banana', 'Uva', 'Pera', 'Abacaxi', 'Banana']
    if 'Banana' in frutas: # Retorna se existe deternimado item
        print(f"Nas frutas tem {frutas}")

# .append & .insert
def append():
    frutas = ['Maçã', 'Melancia', 'Banana', 'Uva', 'Pera', 'Abacaxi']
    print(frutas)
    frutas_pedido =input("Insira uma fruta para adicionar a lista: ")
    frutas.append(frutas_pedido) # .append ultilizado para adicionar item a lista
    print(frutas) 
def insert():
    frutas = ['Maçã', 'Melancia', 'Banana', 'Uva', 'Pera', 'Abacaxi']
    print(frutas)
    frutas_pedido =input("Insira uma fruta para adicionar a lista: ")
    posicao_fruta = str, int(input("Em qual possição: "))
    frutas.insert(posicao_fruta, frutas_pedido) # .insert ultilizado para adicionar item a lista podendo escolhe o index
    print(frutas) 

# .remove & .pop & clear
def remove():
    frutas = ['Maçã', 'Melancia', 'Banana', 'Uva', 'Pera', 'Abacaxi']
    frutas.remove('Melancia')
    print(frutas) # .remove para remover determinado item
def remover_pop():
    frutas = ['Maçã', 'Melancia', 'Banana', 'Uva', 'Pera', 'Abacaxi']
    print(frutas) 

    frutas_removidas = frutas.pop(int(input("Qual indux da fruta para remover?\n"))) # .pop para remover determinado item pelo index

    print(f"fruta removida: {frutas_removidas}")
    print(f"Lista nova : {frutas}")
def Apaga_list():
    frutas = ['Maçã', 'Melancia', 'Banana', 'Uva', 'Pera', 'Abacaxi']
    frutas.clear() # Apagar toda lista
    print(frutas)

# Soma de listas
def Soma_list():
    frutas1 = ['Maçã', 'Melancia', 'Banana']
    frutas2 = ['Uva', 'Pera', 'Abacaxi']

    frutas_total = frutas1 + frutas2 # É possivel soma listas
    print(frutas_total)

# Copia
def copy():
    frutas = ['Maçã', 'Melancia', 'Banana', 'Uva', 'Pera', 'Abacaxi']
    frutas_copia = frutas.copy() # .copy cria uma copia 
    frutas.remove('Maçã')
    print(frutas)
    print(frutas_copia)

#Ordenar
def sort():
    num = [5, 2, 4, 8, 6, 1]
    num.sort() # .sort ordena os itens
    print(num)
    
    num.sort(reverse=True) # reverse=True inverte os Valores
    print(num)
    #Funciona com str
    frutas = ['Maçã', 'Melancia', 'Banana', 'Uva', 'Pera', 'Abacaxi']
    frutas.sort()
    print(frutas)

if __name__ == "__main__":
    # teoria()
    # retorno_index()
    # retorno_quant()
    # len()
    # index()
    # count()
    Verificao()
    # append()
    # insert()
    # remover_pop()
    # Apaga_list()
    # Soma_list(),
    # copy()
    # sort()