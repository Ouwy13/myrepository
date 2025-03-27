def Teoria():
    def MostraLinha():
        print('-='*10)
    
    MostraLinha()
    print('José Roberto')
    MostraLinha()
    print('Curso em Python')
    MostraLinha()

def Teoria2():
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
    #soma(3) <- Erro de parametro
    #soma(3, 4, 7)
     
def Teoria4():
    # Empacotar parametro
    def soma_valores(* valores):
        # Controle de tuplas
        for valor in valores:
            print(valor, end=' > ')
        print('FIM')
    def dobra(*valores):
        valores = list()
        print(valores)
        pos = 0
        while pos < len(valores):
            valores[pos] *= 2
        for valor in valores:
            print(valor, end=' > ')
        print('Fim')
    soma_valores(1,3,5,6,7,9,8)
    soma_valores(1,5,4,7)
    soma_valores(7,9,8,0)

    print('Dobro dos Valores')
    dobra(1,3,5,6,7,9,8)
    dobra(1,5,4,7)
    dobra(7,9,8,0)
if __name__ == "__main__":
    Teoria4()