def Ex05():
    num = int(input('Informe um valor: '))
    print('O seu antecessor é {}\nO seu sucessor é {}'.format(num-1, num+1))
    print(f'{num-1, num, num+1}')

def Ex06():
    num = int(input('Informe outro valor: '))
    print('O dobro: {}\nO triplo: {}\nRaiz quadrada: {}'.format(num*2, num*3, pow(num, (1/2)) ))  # pow ultilizado para fazer raiz quadrada

def Ex07():
    print('Soma de 2 Medias')

    N1 = float(input('Nota 01: '))
    N2 = float(input('Nota 02: '))
    print('Media do periodo {:.1f}'.format((N1 + N2) /2))

def Ex08():
    M = float(input('valor em metro: '))

    print('Valor em Cm: {:.0f}'.format(M * 100))
    print('Valor Em Mm: {:.0f}'.format(M *1000))

def Ex09():
    tab = 'taboada'
    print('\n{:-^16}'.format(tab))
    T = int(input('Informe o valor: '))
    print('-' *12)
    print(f'{T} x  1 = {T*1}')
    print(f'{T} x  2 = {T*2}')
    print(f'{T} x  3 = {T*3}')
    print(f'{T} x  4 = {T*4}')
    print(f'{T} x  5 = {T*5}')
    print(f'{T} x  6 = {T*6}')
    print(f'{T} x  7 = {T*7}')
    print(f'{T} x  8 = {T*8}')
    print(f'{T} x  9 = {T*9}')
    print(f'{T} x 10 = {T*10}')
    print('-' *12)

def Ex10():
    D = 'Compra de Dolar'
    print('{:^24}'.format(D))
    R = float(input('Quantos R$ você tem: '))
   
    print('Você tem {:.2f} em dolar'.format(R/6.17))

def Ex11():
    p = 'Pintura de parede'
    print('{:^25}'.format(p))
    La = float(input('Qual a largura da parede: '))
    Alt = float(input('Qual a altura: '))
    A = La * Alt
    print('Ária da parede: {:.1f}m²'.format(A))
    T = A / 2 #tinta printa 2m cada 
    print('Quantidade necessaria de {:.2f}L de tinta'.format(T))

def Ex12():
    print('Desconto de 5%')
    V = float(input('Qual valor do produto: '))
    P = V * 5/100
    print('Vocé ganhou de desconto R$ {:.2f}'.format(P))

    print('Produto ficou por R$ {:.2f}'.format(V - P))

def Ex13():
    print('Aumento de salario!!')
    V = float(input('Qual seu salario compalheiro: '))
    print('Você ganhou um aumento de 15%')
    print('Seu salario é de R$ {:.2f} '.format(V + (V * 15/100)))

def Ex2_13():
    # pagar a vista 10% de desconto
    # pagar pacelado 8% de aumento
    print('Venda de produto')
    V = float(input('Qual o valor do produto: '))
    
    print('Valor do produto a vista R$ {}'.format(V - (V * 10/100)))
    print('Valor do produto parcelado R$ {}'.format(V + (V * 8/100)))
    
def Ex14():
    A = int(input('Quandos dias alugado: '))
    K = float(input('Quantos Km percorridos: '))
    print('Por {} dias de alugel paga-se R$ {:.2f}'.format(A, A * 60))
    print('Por {} Km rodados R$: {:.2f}'.format(K, K * 0.15))
    print('Totalizando R$ {:.2f}'.format((A * 60) + (K * 0.15)))
   

if __name__ == "__main__":
    Ex14()