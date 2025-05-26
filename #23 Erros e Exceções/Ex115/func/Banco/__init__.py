
def BD():
    Banco = [
        {"Nome": "João Pedro", "Idade": 32, "Sexo": "M"},
        {"Nome": "Maria Eduarda", "Idade": 19, "Sexo": "F"},
        {"Nome": "Luiz Felipe", "Idade": 28, "Sexo": "M"},
        {"Nome": "Carlos Alberto", "Idade": 45, "Sexo": "M"},
        {"Nome": "Laura Beatriz", "Idade": 22, "Sexo": "F"},
        {"Nome": "Pedro Henrique", "Idade": 30, "Sexo": "M"},
        {"Nome": "Julia Vitória", "Idade": 27, "Sexo": "F"},
        {"Nome": "Rafael Augusto", "Idade": 35, "Sexo": "M"},
        {"Nome": "Isabela Cristina", "Idade": 24, "Sexo": "F"},
    ]
    return Banco

#$ Função para carregar o banco de dados do arquivo
def carregar_BD(caminho):
    import os #& Modulo para abrir arquivos ou caminhos
    import json #& Modulo para ler e salvar dados em formato JSON
    from func.Analize import arq_ext
    if arq_ext(caminho): #& Se o arquivo existir
        with open(caminho, "r", encoding="utf-8") as f:
            return json.load(f) #& Carregar e retorna a lista de cadastrados
    return [] #! Se não exitir o arquivo retorna vazio

#$ Função para salvar Lista de Cadastro no BD
def salva_BD(caminho, banco):
    import json
    with open(caminho, "w", encoding="utf-8") as f:
        #& Salva a lista no destino
        json.dump(banco, f, ensure_ascii=False, indent=4)

