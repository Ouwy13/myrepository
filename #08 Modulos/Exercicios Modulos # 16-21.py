def Ex16():
    from math import floor, trunc # tender a ter a mesma função 'floor', 'trunc'
    num = float(input('Informe um valor: '))
    print(f'O valor digitado foi {num} e a sua porção interira é {trunc(num)}')

    print(f'O valor digitado foi {num} e sua parte inteira é {int(num)}') # int(num) mesma função

def Ex17():
    from math import hypot # função de calcular a hipotenusa
    cat_opost = float(input('Comprimento do cateto oposto: '))
    cat_adja = float(input('Comprimento do catet adjacente: '))
    #hipor = (cat_opost **2 + cat_adja **2) ** (1/2)
    hipor = hypot(cat_opost, cat_adja)

    print('A hipotenusa vai medir {:.2f}'.format(hipor))

def Ex18():
    from math import sin, cos, tan, radians
    ang = int(input('Digite o ângulo que deseja: '))
    ang_rad = radians(ang)
    seno = sin(ang_rad)
    coss = cos(ang_rad) 
    tang = tan(ang_rad)
    print('O ângulo de {} o SENO de {:.2f}'.format(ang, seno))
    print('O ângulo de {} o COSSENO de {:.2f}'.format(ang, coss))
    print('O ângulo de {} a TANGENTE de {:.2f}'.format(ang, tang))

def Ex19():
    from random import randint, choice
    print('Escolha do aluno p. Limpa o quadro!')
    N1 = input('Primeiro aluno: ')
    N2 = input('Segundo aluno: ')
    N3 = input('Terceiro aluno: ')
    N4 = input('Quarto aluno: ')

   
    Alunos = [N1, N2, N3, N4]
    escolhido = choice(Alunos) # escolha de algo da lista

    print(f'Parabens {escolhido}')
    
    num = randint(1,4) # escolha de um numero inteiro
    '''if num == 1:
      print(f'Parabens {N1}')
    elif num == 2:
       print(f'Parabens {N2}')
    elif num == 3:
        print(f'Parabens {N3}')
    elif num == 4:
        print(f'Parabens {N4}')'''
  
def Ex20():
    from random import shuffle
    print('Escolha do aluno p. Apresentação!')
    N1 = input('Primeiro aluno: ')
    N2 = input('Segundo aluno: ')
    N3 = input('Terceiro aluno: ')
    N4 = input('Quarto aluno: ')

    Alunos = [N1, N2, N3, N4]
    shuffle(Alunos) # Embaralha Lista
    print(f'A ordem de apresentação será\n{Alunos}')

    
if __name__ == "__main__":
    Ex16()