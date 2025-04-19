def Teoria():
    def MostraLinha():
        print('-='*10)
    
    MostraLinha()
    print('José Roberto')
    MostraLinha()
    print('Curso em Python')
    MostraLinha()

def Teoria2():
    #* Parametros
    def Titulo(titulo):
        print('-='*10)
        print(f'{titulo:^20}')
        print('-='*10)
    
    Titulo('José Roberto')
    Titulo('Curso em Vidio')

def Teoria3():
    def soma(a, b): # Soma de 2 parametros
        res = a + b
        print('--'*14)
        print(f'Soma dos Valores A: {a} B: {b}')
        print(f' > {a} + {b} = {res}')
    
    soma(2, 8)
    soma(a=5, b=6)
    soma(b=4, a=7)
    #!soma(3) <- Erro de parametro
    #!soma(3, 4, 7)
     
def Teoria4():
    # Empacotar parametro
    def soma_valores(* valores):
        # Controle de tuplas
        for valor in valores:
            print(valor, end=' > ')
        print('FIM')

    def total(*valores):
        valores = len(valores)
        print(f'total de valores: {valores}')
    
    def somas(*valores):
        soma = 0
        for valor in valores:
            soma += valor
        print(f'Soma: {soma}')
    
    
    soma_valores(1,3,5,6,7,9,8)
    soma_valores(1,5,4,7)
    soma_valores(7,9,8,0)

    total(1,3,5,6,7,9,8)
    somas(1,3,5,6,7,9,8)

    

def Teoria5():
    def dobra(lista):
        pos = 0
        while pos < len(lista):
            lista[pos] *= 2
            pos +=1
    
    valores = [1, 2, 3, 4, 5]
    dobra(valores)
    print(valores)
    
    def dobra(*valores):
        valores = list(valores)
        pos = 0
        while pos < len(valores):
            valores[pos] *= 2
            pos +=1
        for valor in valores:
            print(valor, end=' > ')
        print('Fim')
    
    print('Dobro dos Valores')
    dobra(1,3,5,6,7,9,8)
    dobra(1,5,4,7)
    dobra(7,9,8,0)

def Ex96():
    def med(lar, comp):
        area = lar * comp
        print(f"A área do terreno de {lar}x{comp} é: {area}m²")
    print("Controle de Terrenos")
    print("-="*10)
    while True:
        try:
            lar = float(input("Largura: "))
            break
        except ValueError:
            print("Valor inválido, tente novamente.")
    while True:
        try:
            comp = float(input("Comprimento: "))
            break
        except ValueError:
            print("Valor inválido, tente novamente.")
    med(lar, comp)

def Ex97():
    def titulo(frase):
        linha = len(frase)
        print(linha)
        print(f'∿∿{"∿"*linha}∿∿')
        print(f"{frase:^{linha+4}}")
        print(f'∿∿{"∿"*linha}∿∿')
    
    frase = str(input("Digite uma frase: ")).strip()
    titulo(frase)

def Ex98():
    from time import sleep
    '''def contador(Começo, Fim, Passo):
        print("∿∿"*17)
        if Começo < Fim:
            print(f"Contador de {Começo} até {Fim} de {Passo} em {Passo}")
            for valor in range(Começo, Fim+1, Passo):
                print(f"{valor}",end=" ", flush=True)
                sleep(0.5)
            print("Fim")
        else:
            if Passo == 0:
                Passo = 1
            if Passo < 0:
                Passo = abs(Passo)
            print(f"Contador de {Começo} até {Fim} de {Passo} em {Passo}")
            for valor in range(Começo, Fim, -Passo):
                print(f"{valor}",end=" ", flush=True)
                sleep(0.5)
            print(Fim, end=" ", flush=True)
            sleep(0.5)
            print("Fim")'''
    def contador(Começo, Final, Passo):
        if Passo == 0:
            Passo = 1
        elif Passo < 0:
            Passo = abs(Passo)
          
        print("∿∿"*17)
        print(f"Contador de {Começo} até {Final} de {Passo} em {Passo}")
        i = Começo
        if i <= Final:
            while i <= Final:
                print(f"{i}",end=" ", flush=True)
                i += Passo
                sleep(0.5)
            print("Fim")
        else:
            while Final <= i:
                print(f"{i}",end=" ", flush=True)
                i -= Passo
                sleep(0.5)
            print("Fim")               
    contador(1, 10, 1)
    contador(10, 0, 2)
    print("∿∿"*17)
    print("Agora é sua vez!")
    while True:
        try:
            Começo = int(input("Inicio: "))
            Final = int(input("Final:   "))
            Passo = int(input("Passo:   "))
            break
        except ValueError:
            print("Informe somente valores!")
    contador(Começo, Final, Passo)  

def Ex99():
    from time import sleep
    def maior(*valores):
        valores = list(valores)
        maior = valores[0]
        for valor in valores:
            if valor > maior:
                maior = valor
        
        print("∿∿"*17)
        sleep(0.5)
        print("Analisando os valores passados...")
        sleep(0.5)
        for valor in valores:
            print(f"{valor}", end=" ", flush=True)
            sleep(0.5)
        print(f"\nForam informados {len(valores)} valores")
        sleep(0.5)
        print(f"O maior valor informado foi {maior}")
        sleep(0.5)
        
    maior(2,9,4,5,7,1)
    maior(4,7,0)
    maior(1,2)
    maior(6)

def Ex100():
    from random import randint
    from time import sleep
    def sorteia(nums):
        for v in range(0,5):
            nums.append(randint(1,10))
        print(f"Sorteando 5 valores: ",end="")
        for v in nums:
            print(f"{v}",end=' ', flush=True)
            sleep(0.5)
    def somaPar(nums):
        par = 0
        for valor in nums:
            if valor % 2 == 0:
                par += valor
        print(f"\nSomando os valores pares temos {par} ")

    numeros =list()
    sorteia(numeros)
    soma = numeros[:]
    somaPar(soma)
    
if __name__ == "__main__":
    Ex98()