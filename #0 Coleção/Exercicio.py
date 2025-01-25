#Adicionar o numero 6
def Ex1():
    num = [1,2,3,4, 5]
    num_add = 6
    num.append(num_add)
    print(num)
#Remover o numero 2
    num.remove(2)
    print(num)
#Subtituir o numero 4 pelo 40
    posicao = (num.index(4)) # <-Vai informa a posição do index do numero 4 e salva na posicao
    num.insert(posicao, 40) # <- Vai adicionar o numero 40 na posição do index do 4
    num.remove(4) 
    print(num)
#Inverter os numeros da lista
    num.sort(reverse=True)
    print(num)

def Ex2():
    frutas = ('maça', 'banana', 'laranja', 'uva')
#Verificou se havia banana
    if 'banana' in frutas:
        print(f"Tem banana na lista")
#Alterou a Tuple para Lista
    frutas_list = list(frutas) 
#Adicionou Abacaxi  
    frutas_list.append('abacaxi')
#Alterou a Lista para Tuple 
    frutas = tuple(frutas_list)
    
    print(frutas)

def Ex3():
    aluno = {'nome':'Maria', 'Idade': 20, 'Curso':'Engenharia'}
#Atribuiu outro valor    
    aluno['nota'] = 9.5 
#Alterou a idade   
    aluno['Idade'] = 21 
# Removeu o curso   
    aluno.pop('Curso') 
#Atribuiou os Cursos   
    aluno['Cursos'] = ['Informatica', 'Gerenciamento de BD', 'Analize de Dados'] 
    
    print(aluno)

if __name__ == "__main__":
    #Ex1()
    #Ex2()
    Ex3()
    
