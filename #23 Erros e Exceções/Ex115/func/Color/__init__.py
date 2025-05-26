def c(color=""):
    """ --> Função colorir terminal\n
        1 - vermelho| 5 - roxo\n       
        2 - verde   | 6 - azul claro\n         
        3 - amarelo | 7 - branco\n
        4 - azul    |\n        
        paremetro numerico\n
        Text 30/Back 40\n
        Ex: \033[31m or \033[41m
    """
    if color == "":
        return "\033[m"
    else:
        if color > 30:
            return f"\033[m\033[1;{color}m"
        else:
            return f"\033[m\033[1;3{color}m"   

def caixa_arredondada(texto, cor_texto=7, cor_fundo=7):
    """
    Cria uma caixa com bordas arredondadas ao redor do texto.
    
    Args:
        texto (str): O texto a ser exibido dentro da caixa.
        cor_texto (str): Código ANSI para a cor do texto (padrão: branco).
        cor_fundo (str): Código ANSI para a cor do fundo (padrão: preto).
    """
    texto_formatado = f"{c(cor_texto)} {texto} {c(7)}"
    largura = len(texto) + 2
    borda_superior = f"{c(cor_fundo)}╭{'─' * largura}╮{c(7)}"
    borda_inferior = f"{c(cor_fundo)}╰{'─' * largura}╯{c(7)}"
    return f"{borda_superior}\n{c(cor_fundo)}│{texto_formatado}│{c(7)}\n{borda_inferior}"
