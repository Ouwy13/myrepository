def Teoria1():
    #? Anotar sobre
    #&isalpha()
    #&isnumeric()
    #&flush= True
    
    #? Interactive Help
    # Comando usado pra ver a documentação de uma função
    import math
    help(input) #* Com função
    help(math) #* Com Bibliotecas
    # Auxilio pra saber funcionalidade

def Teoria2():
    #? Docstrings
    # Como fazer a documentação de uma função
    # Documentação auxilia da compreensão da função
    #* Função interna
    def contador(inicio, final, passo):
        #*Criação de uma docstring --> """doc"""
        """--> Função que faz contagem determinando seus prontos...
            inicio: Ponto inicial da contagem
            final: Ponto final da contagem
            passo: Passo que a contagem vai ser usada
            return: Sem retorno
        """
        c = inicio
        while c <= final:
            print(f"{c}",end=" ")
            c += passo
        print("Fim")
    
    #*Comando principal
    contador(2,10,2)
    
    help(contador)

def Teoria3():
    #? Parâmetros 
    # Quando na função algum parametro pode ser opcional 
    # Não multi-parametros
    
    #* Função Interna
    def soma(a,b,c=0): #* Paramentro opcional
        #$ > Caso variavel c não for apresentada recebe 0
        s = a+b+c
        print(f"A soma é {s}")
    #* Comando princial
    soma(2,4,7)
    soma(5,6) # evitando erros
    soma(b=3, a=10)

def Teoria4():
    #? Escopo de Variável
    # Local onde variavel coseguir ser execultado
    #* Função
    def test():
        #$ Escopo Local
        # As declarações afetam somente em sua função
        x = 10
        print(f"Na função, x vale {x}")
        print(f"Na função, n vale {n}")

    #* Comando principal
    #$ Escopo Global
    # As declarações afeta todo o codigo
    n = 3
    print(f"No comando princial, n vale {n}")
    #! Dar erro!
    #print(f"No comando princial, x vale {x}")
    test()

    def testa(b):
        global a #* Toda atribuição vai valer para o codigo inteiro
        a = 8
        b +=4
        c = 2
        print(f"A dentro vale {a}")
        print(f"B dentro vale {b}")
        print(f"C dentro vale {c}")
    
    a = 5
    testa(a)
    print(f"A fora vale {a}")

def Teoria5():
    #? Retorno de Valores
    def soma(a=0,b=0,c=0):
        s = a+b+c
        return s #* Vai retorna a soma
    resp = soma(3,5,8)
    print(f"A soma é {resp}")
    # Ou
    print(f"A soma é {soma(5,7)}")
    print(soma(4))

def Pratica():
    print("Fatorial")
    def fatorial(valor=1):
        c = 1
        total = 1
        while c <= valor:
            total *= c
            c +=1
        return total
    v = int(input("Qual o valor: "))
    r = fatorial(v)
    while v > 0:
        print(f"{v}", end=" ")
        v -=1
    print(f"= {r}")

    def par(num=0):
        if num %2==0:
            return True
        else:
            return False
    num = int(input("Informe outro valor: "))
    if par(num):
        print("O valor é Par")
    else:
        print("O valor é Impar")

def Ex101():
    # 18 - OBRIGATORIO
    # <18 - NÃO VOTA
    # >65 - OBCIONAL
    def voto(ano=0):
        from datetime import date
        ano_atual = date.today().year
        global idade
        idade = ano_atual - ano
        print(idade)
        if 18 < idade < 65:
            return f"Com {idade}: VOTO OBRIGATORIO"
        if idade >= 65:
            return f"Com {idade}:VOTO OPCIONAL"
        else:
            return f"Com {idade}:NÃO VOTA"
    print("-="*14)
    print(f"{"Analize de Idade":^28}")
    print("-="*14)
    while True:
        try:
            ano_nsc = int(input("Em que ano você nasceu: "))
            break
        except ValueError:
            print("Informe o Ano!")
    print(voto(ano_nsc))

def Ex102():
    
    
    def fatorial(valor=1, show=False):
        """--> Função que calcula o fatorial de um numero
                valor: Numero escolhido para fazer fatoração
                show: Caso queira mostrar processo de fatoração
        """
        total = 1
        for i in range(valor, 0, -1):
            total *= i
            if show:
                print(i, end=" ")
                if i != 1:
                    print("X",end=" ")
                else:
                    print("=",end=" ")
        return total
    print(fatorial(5, show=True))
    help(fatorial)
def Ex103():
    def ficha(jogador="", gols=0):
        if jogador == "":
            print(f"O jogador <desconhecido> fez {gols} gol(s) no campeonato")
        else:
            print(f"O jogador {jogador} fez {gols} gol(s) no campeonato")
    jogador = str(input("Qual o jogador: ")).strip()
    gols = str(input("Quantos Gols: ")).strip()
    if gols.isnumeric():
        gols = int(gols)
    else:
        gols = 0
    ficha(jogador, gols)

def Ex104():
    def c(color=""):
        """ --> Função colorir terminal\n
            1 - vermelho| 5 - roxo\n       
            2 - verde   | 6 - azul claro\n         
            3 - amarelo | 7 - branco\n
            4 - azul\n  |        
            paremetro numerico\n
            Text 30/Back 40\n
            Ex: \033[31m or \033[41m
        """
        if color == "":
            return "\033[m"
        else:
            if color > 30:
                return f"\033[1;{color}m"
            else:
                return f"\033[1;3{color}m"
    
    def leiaInt(msg):
            while True:
                num = str(input(msg)).strip()
                if num.isnumeric():
                    return num
                    break
                else:
                    print(f"{c(1)}Digite somente numeros!{c()}")
    def Cond(msg):
        def c(color=""):
            """ --> Função colorir terminal\n
                1 - vermelho| 5 - roxo\n       
                2 - verde   | 6 - azul claro\n         
                3 - amarelo | 7 - branco\n
                4 - azul\n  |        
                paremetro numerico\n
                Text 30/Back 40\n
                Ex: \033[31m or \033[41m
            """
            if color == "":
                return "\033[m"
            else:
                if color > 30:
                    return f"\033[1;{color}m"
                else:
                    return f"\033[1;3{color}m"
        while True:
            try:
                cond = str(input(msg)).strip().upper()[0]
                if cond in 'SN':
                    return cond
                    break
                else:
                    print(f"{c(1)}A condição é [S/N]!{c(7)}")
            except IndexError:
                print(f"{c(1)}Informe a Condição!{c(7)}")

    num = leiaInt('Digite um número: ')
    print(f"Você acabou de digitar o numero {num}")
    resp = Cond('Condição S/N: ')
    print(f"Condição Apresentada {resp}")

def Ex105():
    
    def notas(*nota, sit=False):
        """--> Função pra analizar notas de alunos

        Args:
            sit (bool, optional): 
            (True) exibir situação das médias.
            (False) não exibir situação das médias

        Returns:
            nota: Aceita varia notas em float 
            sit: Para exibir a situação das notas
            return: retorna uma dict com sua devidas informações
            
       """
        cads = dict()
        #$ Total de Notas
        cads["Total"] = len(nota)
        #$ Maior e Menor
        cads["Maior"] = max(nota)
        cads["Menor"] = min(nota)
        #$ Média
        total = 0
        for n in nota:
            total += n
        cads["Média"] = round(total / len(nota), 1) #* Lembrete
        #$ Situação
        # >= 7 BOA / < 6 RAZOÁVEL / <= 4 RUIM / > 8 EXCELENTE
        if sit:
            if cads["Média"] > 8:
                cads["Situação"] = "EXCELENTE"
            elif 7 <= cads["Média"] < 8:
                cads["Situação"] = "BOA"
            elif 4 < cads["Média"] <= 6:
                cads["Situação"] = "RAZOÁVEL"
            else:
                cads["Situação"] = "RUIM"
        return cads
    
    print(notas(9, 2, 2, 9, sit=True))
    help(notas)  

def Ex106():
    def c(color=""):
            """ --> Função colorir terminal\n
                1 - vermelho| 5 - roxo\n       
                2 - verde   | 6 - azul claro\n         
                3 - amarelo | 7 - branco\n
                4 - azul\n  |        
                paremetro numerico\n
                Text 30/Back 40\n
                Ex: \033[31m or \033[41m
            """
            if color == "":
                return "\033[m"
            else:
                if color > 30:
                    return f"\033[1;{color}m"
                else:
                    return f"\033[1;3{color}m"
    #$ Titulo
    def titule(msg="", color=7):
        from random import randint
        if color == 99:
            color = randint(1,6)

        lin = len(msg)+4
        print(f"{c(7)}{"∿"*lin}")
        print(f"{c(color)}{msg:^{lin}}")
        print(f"{c(7)}{"∿"*lin}")
    def esc():
        from time import sleep
        from os import system
        while True:
            while True:
                titule(f"  AJUDA PYHELP 📖  ", color=4)
                ops = str(input(f"{c(4)}•{c(7)} Função ou Biblioteca\n{c(2)}>>>{c(4)} ")).strip()
                if ops == "":
                    print(f"{c(1)}Informe o Comando!{c(7)}")
                    sleep(1)
                    system("cls")
                else:
                    break        
                
            if ops == "exit":
                break
            titule(f"Manual comando {ops}", color=99)
            print(help(ops))
            print(f"{c(7)}—"*22)
            p = str(input(f"{c(4)}>{c(7)} Enter continuar..."))
            system("cls")

    esc()
    print(f"{c(7)}Fim do Programa 😊")
if __name__ == "__main__":
    Ex106()



#! JESUS CRISTO
#@ JESUS CRISTO
#$ JESUS CRISTO
#% JESUS CRISTO
#& JESUS CRISTO
#* JESUS CRISTO
#? JESUS CRISTO
#// JESUS CRISTO


