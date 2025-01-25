def P1():
    import math
    num = int(input('Informe um numero: '))
    raiz = math.sqrt(num)
    print('A raiz de {} é igual a {:.2}'.format(num, raiz))

def P2():
    
    from math import sqrt
    num = int(input('Informe um numero: '))
    raiz = sqrt(num)
    print('A raiz de {} é igual a {}'.format(num, raiz))

if __name__ == "__main__":
    P2()


