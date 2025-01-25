def Teoria():
# if & else
    nome = str(input('Qual seu nome: '))
    if nome.lower() == 'josé':
      print('Belo nome! ')
    else:
       print('Marromeno')
    print(f'Bom dia, {nome}')



    n1 = float(input('Primeira nota :'))
    n2 = float(input('Segunda nota: '))
    n3 = float(input('Terceira nota: '))
    n4 = float (input('Quarta nota: '))

    m = (n1 + n2 + n3 + n4)/4
    if m >= 6.0:
        print('Media Boa!')
    else:
        print('Melhora mais!')

def Ex28():
    from random import randint
    from time import sleep
    print('=-'* 20)
    print('Computador pensando em um numero...')
    print('=-'* 20)
    print('Já decidir!')
    
    num_esc = randint(0,5) 
    num = int(input('Qual numero você acha que deve ser?\nDe 0 a 5: '))
    print('PROCESSANDO...')
    sleep(2)
    if num == num_esc and num <=5:
       print('\033[32mParabens Você ganhou :(\033[m')
    elif num != num_esc and num <=5:
       print('\033[31mVocê Errou o numero!!\033[m')
       print('Computador ganhou :)')
    else:
       print('Escolha um numero valido!!')
    print(f'O numero era {num_esc}')

def Ex29():
    V = int(input('Qual era a velocidade do carro?\nKm: '))
    
    if V > 80:
       print('\033[31mVai pagar multa!!\nCada 1km ultrapassado paga-se R$ 7.00\033[m')
       M = V - 80
       P = float(M * 7.0)
       print('Vai pagar por anda a {}Km \033[31mR$ {:.2f}\033[m '.format(V, P))
    else:
       print('\033[32mParabéns por seguir a lei!!')
    print('Se bebê não dirija :)\033[m')

def Ex30():
    print('Impar ou Par')
    num = int(input('Irforme um numero: '))
    if num % 2 == 0:
      print('Seu numero é Par!')
    else:
       print('Seu numero é Impar!')

def Ex31():
    D = int(input('Qual a distancia da viagem companheiro?\nKm: '))
    if D < 200:
       V = float(D * 0.50)
       print(f'\nViagem de até 200km R$0.50 por 1km\nDeu no total R${V}!')
       
    else:
       V = float(D * 0.45)
       print(f'\nViagem acima de 200Km R$0.45 por 1km\nDeu ao total R$: {V}!')
    print('Boa Viagem :)')
       
def Ex32():
    from datetime import date
    Ano = int(input('Que ano quer analizar?\nColoque 0 para analizar o ano atual: '))
    if Ano == 0:
       Ano = date.today().year
       
    if Ano % 4 == 0 and Ano % 100 != 0 or Ano % 400 == 0:
      print(f'O Ano {Ano} é Bissexto!')
    else:
       print(f'O Ano {Ano} não é Bissexto!')

def Ex33():
   print('--Informe-3-numeros--')
   n1 = int(input('Primeiro valor: '))
   n2 = int(input('Segundo valor: '))
   n3 = int(input('Terceiro valor: '))
   menor = n1
   maior = n1
   if n2<n1 and n2<n3:
      menor = n2
   if n3<n1 and n3<n2:
      menor = n3
   
   if n2>n1 and n2>n3:
      maior = n2
   if n3>n1 and n3>n2:
      maior = n3
   
   print(f'O menor valor foi: {menor}')
   print(f'O maior valor foi: {maior}')
   

def Ex34():
    print('Aumento de salario :)')
    s = float(input('Informe seu salario: '))
    if s > 1250.00:
      print('Você recebeu um aumento de 10%') 
      print('Seu salario atual R$ {:.2f}'.format(s + (s * 10/100)))
    else:
      print('Você recebeu um aumento de 15%') 
      print('Seu salario atual R$ {:.2f}'.format(s + (s * 15/100)))

def Ex35():
 
   print('=-'*12)
   print('Analisador de Triângulos')
   print('=-'*12)
   v1 = float(input('Primeiro valor: '))
   v2 = float(input('Segundo valor: '))
   v3 = float(input('Terceiro valor: '))
   AB = 0
   if (v1 + v2) >= v3:
      if (v1 + v3) >= v2:
         if (v2 + v3) >= v1:
            print('PODE FORMAR um triângulo')
            print('Se a soma de dois lados forem maior ou igual ao terceiro lado.\nPode ser possivel fazer um triângulo!')
   else:
      print('NÂO PODE FORMAR um triângulo')
      print('Se a soma de dois lados forem menor ao terceiro lado.\nNão é possivel fazer um triângulo!')



if __name__ == "__main__":
   Ex31()