#Coleção Tuples ()
def tuples():
    cores = ('Roxo', 'Laranja', 'Azul')
    cores_lista = list(cores) #Tranforma uma tuple  em um lista
    cores_lista.sort() #Ordenando a lista
    print(cores_lista)

    cores_lista.append('Verde') # Adicionando item
    cores = tuple(cores_lista)  #Tranforma um lista em tuple
    print(cores)

#Coleção Dicionario {}

def get():
    cachorro = {'nome':'Cleitin', 'raça':'Husk', 'idade':'5'}
    
    print(f"Nome do cachorro: {cachorro['nome']}") # [] ultizada para exibir item escolhido
    
    print(f"Idade do cachorro: {cachorro.get('idade')}") # .get subtitui as [] 
    
    print(cachorro.get('Sexo', 'Sexo não encontrado')) # Sexo do cachorro ñ encontrado
    cachorro_Sexo = str(input("Qual o Sexo do cachorro: ")) # Pedio para informa 
    if cachorro_Sexo == 'M': # Se 'M' eh Macho
     cachorro['Sexo'] = 'Macho'
    elif cachorro_Sexo == 'F': # Se 'F' eh Femia
       cachorro['Sexo'] = 'Femia'
    print(f"Sexo do cachorro é: {cachorro['Sexo']}")

if __name__ == "__main__":
    # tuples()
    get()