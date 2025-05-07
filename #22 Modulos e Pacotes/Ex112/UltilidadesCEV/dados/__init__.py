from UltilidadesCEV import Color
def LeiaFloat(msg):
    while True:
        valor = str(input(msg)).strip()
        if -1 < valor.count(",") < 2:
            valor = valor.replace(",",".")
            if valor.replace(".", "").isnumeric():
                return float(valor)
                break
            else:
                print(f'{Color.c(1)}ERRO {Color.c(41)}"{valor}"{Color.c(1)} é invalido!{Color.c()}')
        else:
            print(f'{Color.c(1)}Somente uma virgula!{Color.c()}')