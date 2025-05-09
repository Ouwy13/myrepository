def Teoria():
    #$ Analize de Erros
    try: #& <-Tente
        n1 = float(input("Numerador: "))
        n2 = float(input("Denominador: "))
        r = n1 / n2

    except Exception as erro: #$ <- Informa qual erro!
        print(f"Erro Obtido {erro.__class__}")

    except: #& <- Exerção
        print("Deu Erro! :(")

    else: #& <- Caso Contrario
        print(f"A subtração da: {r:.2f}")
    finally: #& <- Exibição Obrigatoria
        print("Tente novamente!")

def Teoria2():
    try: #& <-Tente
        n1 = float(input("Numerador: "))
        n2 = float(input("Denominador: "))
        r = n1 / n2
    except (ValueError, TypeError): #& <- Validação de 2 erros
        print("Tivemos erro com os valores informados!")

    except ZeroDivisionError: #& Um somente
        print("Denominador não pode ser 0!")

    except KeyboardInterrupt: #& Erro obtido Ctrl + c p. Cancelar
        print("O usuario não informou os dados!")

    else: #& <- Caso Contrario
        print(f"A subtração da: {r:.2f}")

    finally: #& <- Exibição Obrigatoria
        print("Tente novamente!")


Teoria2()
