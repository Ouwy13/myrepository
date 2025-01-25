n1 = int(input('Informe V1: '))
n2 = int(input('Informe V2: '))
r = n1 + n2
#print(f'A soma do valor {n1} + {n2} = {r}') 
#print(f'A soma é {n1+n2}')
print('A soma é {}'.format(n1+n2))
print('A subritação é {}\nA multiplicação é {}\nA divisão é {:.2f}' # :.2f Determina a quantifade de ponto flutuante
.format(n1-n2, n1*n2, n1/n2))
print(f'A divisão inteira é {n1//n2}\nA potencia é {n1**n2}')


#Regra praa continuar na mesma linha
print('Banana', end= ' ')  # <-- ,Final = 'espaço'
print('Maça', end= ' ') # continua
print('Cenoura')


# Ordem de procedencia
# 1- ( ) <- parenteses
# 2- ** <- elevado
# 3- * / // %  <- resto por inpar, resto
# 4- + -

# lembrete de espaçamento {:>10} <-- Define o tamanho que o item pode ocupar .format() 
N1 = 'Ana'
N2 = 'João'
N3 = 'Pedro'
N4 = 'Paulo'

print('{:>10}{:>10}{:>10}{:>10}'.format(N1, N2, N3, N4))

print('{:^10}{:^10}{:^10}{:^10}'.format(N1, N2, N3, N4))

print('{:<10}{:<10}{:<10}{:<10}'.format(N1, N2, N3, N4))

print('{:-<10}{:-<10}{:-<10}{:-<10}'.format(N1, N2, N3, N4))