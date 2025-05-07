from UltilidadesCEV import moeda as m, dados as d, Color as C

valor = d.LeiaFloat(f"{C.c(7)}Diga o preço: R$")
m.resumo(valor, 80, 30)