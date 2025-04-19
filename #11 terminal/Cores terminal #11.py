#Cores terminal
#Style 
# 0 = padrão
# 1 = negrito
# 4 = Subliada
# 7 = inverter cores

#Text                  #Back
# 30 - branco          .40
# 31 - vermelho        .41
# 32 - verde           .42
# 33 - amarelo         .43
# 34 - azul            .44
# 35 - roxo            .45
# 36 - azul claro      .46
# 37 - cinza           .47

# \033[Style;Text;Back m
# \033[0:33:44m

print('\033[1;31;40mJesus is \033[33mKing!\033[m')

print('\033[41mJesus is King!\033[m')

print('\033[4;33;46mJesus is King!\033[m')

print('\033[1;35;43mJesus is King!\033[m')

print('\033[1;42mJesus is King!\033[m')

print('\033[mJesus is King!\033[m')

print('\033[7;37mJesus is King!\033[m')


frutas = ('\033[1;31mMaçã\033[m, \033[1;33mBanana\033[m, \033[1;32mLimão\033[m, \033[1;35mUva\033[m')
print(frutas)

nome = 'José'

print(f'Olá {'\033[4;36m'}{nome}{'\033[m'}')

fruta = 'maça'
cores = {
    'limpa':'\033[m',
    'azul':'\033[1;33m',
    'verde':'\033[1;32m',
    'vermelho':'\033[1;31m',
    'amarelo':'\033[1;33m'
}
print(f'{cores["vermelho"]}maçã{cores["limpa"]}, {cores['amarelo']}banana{cores["limpa"]} ')

c = {
    'l':'\033[m',#limpa
    'n':'\033[1;37m',#negrito
    's':'\033[4;37m',#subliando
    '31':'\033[1;31m', #vemelho
    '32':'\033[1;32m',#verde
    '33':'\033[1;33m',#amarelo
    '34':'\033[1;34m',#azul
    '35':'\033[1;35m',#roxo
    '36':'\033[1;36m',#azul ciano

}

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
print(f"{c(7)} Oiee")
