from Color import c

def LeiaInt(msg):
    while True:
        try:
            num = int(input(msg))
        except ValueError:
            print(f"{c(1)}Erro! Informe um numero inteiro :({c()}")
        else:
            print(f"{c(2)}Ok :){c()}")
            return num
            break

def LeiaFloat(msg):
    while True:
        try:
            num = float(input(msg))
        except ValueError:
            print(f"{c(1)}Erro! Informe um numero real :({c()}")
        except KeyboardInterrupt:
            print(f"{c(1)}O usuario não informou esse numero!{c()}")
            return 0
            break
        else:
            print(f"{c(2)}Ok :){c()}")
            return num
            break

inteiro = LeiaInt("Inteiro: ")
real = LeiaFloat("Real: ")

print(f"Numero Inteiro: {inteiro}")
print(f"Numero Real: {real}")