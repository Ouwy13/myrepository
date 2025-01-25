#Faceis
def Ex1_F():
    frutas = ['maçã', 'banana', 'laranja']
    frutas.append('limão')
    print(frutas)

def Ex2_F():
  num = (1,2,3,4,5)
  if 3 in num:
      print("Na lista existe o numero 3!!")

def Ex3_F():
    pessoa = {'nome':1,'idade':2,'cidade':3}
    pessoa['nome'] = input("Qual o nome: ")
    pessoa['idade'] = int(input("Qual a idade: "))
    pessoa['cidade'] = input("Qual a cidade: ")

    print(f"Seu nome é {pessoa['nome']}")
    print(f"Sua idade é {pessoa['idade']} anos")
    print(f"Mora em {pessoa['cidade']}")

#Medios    
def Ex1_M():
    num = [10, 20, 30, 40, 50]
    num.remove(30)
    print(num)

def Ex2_M():
    letra = ('A', 'B', 'C', 'D')
    letra_list = list(letra)
    letra_list.append('E')
    letra = tuple(letra_list)
    print(letra)

def Ex3_M():
   Pro = {'P1':0, 'P2':0, 'P3':0} 
   Pro['P1'] = float(input("Qual o valor do Produto 1: "))
   Pro['P2'] = float(input("Qual o valor do Produto 2: "))
   Pro['P3'] = float(input("Qual o valor do Produto 3: "))
   
   Pro['Total'] = Pro['P1'] + Pro['P2'] + Pro['P3']
   print(Pro)

#Dificeis
def Ex1_D():
    num = [5, 3, 8, 6, 2, 4]
    num.sort()
    print(num)
  
def Ex2_D():
    num = [3, 2 ,6 ,5 ,4]
    print(num)

    num.append(int(input('Adicione um numero a lista: ')))
    
    print(num)
    num_v = int(input('Qual numero deseja o index: '))
    num_p = num.index(num_v)
    
    print('Posição do index é: {}'.format(num_p))

    num_q = int(input('Escolha um numero para saber quantidade: '))
    num_1p = num.count(num_q)
   
    print(f'Repete: {num_1p} vezes')

    print('Ordem Crecente da lista')
    num.sort()
    print(num)

def Ex3_D():
    compras = []

    print('Lista de compras')
    compras.append(input('Deseja adicionar qual produto?\n'))
    Decisao = input('Adicionar mais?\n')
    
    
 
    
    

    compras.append('')

   
if __name__ == "__main__":

    Ex3_D()
