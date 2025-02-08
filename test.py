def Ex59():
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
    from time import sleep 
    from os import system #modulo p. limpar a tela
    n =1
    print(f'{c["n"]}=-'*10)
    print(f'{c["35"]}{'Menu de operações':^20}')
    print(f'{c["n"]}=-'*10)
    n1 = int(input(f'{n}ª valor: '))
    n2 = int(input(f'{n+1}ª valor: '))
    print('Analizando..')
    sleep(1)
    
    op = [
        
        f'{c["n"]}=='*10,
        f'{c["35"]}{'Tabela ☑️':^22}',
        f'{c["n"]}=='*10,
        
        f'{'1️⃣  soma.':<12}{'6️⃣  menor'}',
        f'{'2️⃣  subt.':<12}{'7️⃣  elev.'}',
        f'{'3️⃣  mult.':<12}{'8️⃣  primo'}',
        f'{'4️⃣  divi.':<12}{'9️⃣  outros'}',
        f'{'5️⃣  maior ':<12}{'0️⃣  sair'}'
        
    ]
    opera = 1
    t =1
    
    while opera != 0:
        
        for ops in op:
            print(ops)
        
        print('__'*10)
        print(f'{c["35"]}{t}ª Teste ')
        t += 1
        opera = int(input(f'{c["n"]}Qual deseja 🙃: ')) 
        if opera != 0 and opera <= 9:
            print('=-'*10)
            print(f'{c["32"]}{'OPÇÃO':>10} {opera}✅{c["n"]}')
        print(f'--'*10)
        sleep(0.5)

        if opera <=8:
            if opera ==1:
                res1 = n1 + n2
                
                print(f'{c["35"]}Soma ➕\n{c["n"]}num1: {n1}\nnum2: {n2}') 
                print(f'{c["36"]}{n1} + {n2} = {res1}')
                
            elif opera ==2:
                res1 = n1 - n2
                res2 = n2 - n1
                print(f'{c["35"]}Subtração ➖\n{c["n"]}num1: {n1}\nnum2: {n2}') 
                print(f'{c["36"]}{n1} - {n2} = {res1}')
                print(f'{n2} - {n1} = {res2}')
                
            elif  opera ==3:
                res = n1 * n2
                print(f'{c['35']}Multiplicação ✖️\n{c["n"]}num1: {n1}\nnum2: {n2}') 
                print(f'{c["36"]}{n1} x {n2} = {res}')
                
            elif  opera ==4:
                res1 = n1 / n2
                res2 = n2 / n1
                print(f'{c["35"]}Divisão ➗\n{c['n']}num1: {n1}\nnum2: {n2}') 
                print(f'{c["36"]}{n1} / {n2} = {res1:.1f}')
                print(f'{n2} / {n1} = {res2:.1f}')
                
            elif opera ==5:
                print(f'{c["36"]}Maior 🔼{c["n"]}')
                if n1 > n2:
                    print(f'Núm. {n1} é maior que {n2}')
                elif n2 > n1:
                    print(f'Núm. {n2} é maior que {n1}')
                else: 
                    print('Os números são iguais')
                
            elif opera ==6:
                print(f'{c["36"]}Menor 🔽{c["n"]}')
                if n1 < n2:
                    print(f'Núm. {n1} é menor que {n2}')
                elif n2 < n1:
                    print(f'Núm. {n2} é menor que {n1}')
                else: 
                    print('Os números são iguais')
                
            elif  opera ==7:
                res1 = n1 ** n2
                res2 = n2 ** n1
                print(f'{c["35"]}Elevado 🔝\n{c["n"]}num1: {n1}\nnum2: {n2}') 
                print(f'{c["36"]}{n1} elevado a {n2} é {res1}')
                print(f'{n2} elevado a {n1} é {res2}')
                
            elif opera ==8:
                tot = 0
                for cont in range (1, n1+1):
                    if n1 % cont == 0:
                        tot += 1
                if tot == 2:
                    print(f'Número {c["32"]}{n1}{c["n"]} é primo!')
                else:
                    print(f'Número {c["31"]}{n1}{c["n"]} não é primo!')
                
                for cont in range (1, n2+1):
                    if n2 % cont == 0:
                        tot += 1
                if tot == 2:
                    print(f'Número {c["32"]}{n2}{c["n"]} é primo!')
                else:
                    print(f'Número {c["31"]}{n2}{c["n"]} não primo!')
        
        elif opera != 0 and opera < 9:# tem que ser diferente de 0 p. fazer limpeza e abaixo de 9
            print(f'{c["n"]}=-'*10)
            p = input('Enter p. continuar..')
            sleep(1)
            system('cls') # limpa a tela    
        
        if opera ==9:
            print(f'{c["36"]}Outros valores 🔄️{c["n"]}')
            n1 = int(input(f'{n}ª valor: '))
            n2 = int(input(f'{n+1}ª valor: '))
            print('Analizando..')
            sleep(1)
            system('cls')

        elif opera > 9:
            print(f'{c['31']}Informe opção valida!{c["l"]}')
            sleep(2)
            system('cls')

        
    print(f'{c["36"]}Fim das operações! 😊')
    sleep(2)
    system('cls')
    print(f'{c["n"]}Qual nota p. programa? 🤭')

def test():
    print('\033[1;37m-='*14)
    print('\033[34mPROGRESSÃO ARITMETICA P.A v3')
    print('\033[1;37m-='*14)
    print('\033[37mOs 10 primeiros termos')
    a1= int(input('Informe o primeiro termo: '))
    R = int(input('Qual a razão: '))
    print(f'Fomula: An = a1 + (n-1).r\n {a1}')
    a10 = 10
    PA = 2
   
    while PA <= a10:
        an = a1 + (PA-1)*R
        PA +=1
        print(f'{an}', end= ' → ')  
    print('Pause')
    
    An = 1
    while An != 0:
        print('[0]-Para finalizar')
        int = input('Deseja mostrar mais termos? An: ')
        PA = 2
        while PA <= An:
            an = a1 + (PA-1)*R
            PA +=1
            print(f'{an}', end= ' → ')
        print('Fim')

def test2():
    valores = list[range(4,11)] # Valores recebem 'lista' de 4 a 10
    print(f'{valores}')

if __name__ == "__main__":
    test2()
'''{
  "editor.fontSize": 20,
  "editor.letterSpacing": -0.2,
  "editor.lineHeight": 32,
  "editor.rulers": [80, 120],
  "editor.renderLineHighlight": "gutter",
  "workbench.productIconTheme": "fluent-icons",
  "workbench.iconTheme": "symbols",
  "window.commandCenter": false,
  "workbench.layoutControl.enabled": false,
  "workbench.statusBar.visible": false,
  "errorLens.statusBarColorsEnabled": true,
  "workbench.tree.indent": 18,
  "editor.fontFamily": "JetBrains Mono",
  "window.density.editorTabHeight": "compact",
  "breadcrumbs.enabled": false,
  "editor.guides.highlightActiveIndentation": false,
  "editor.cursorSmoothCaretAnimation": "on",
  "workbench.list.smoothScrolling": true,
  "terminal.integrated.smoothScrolling": true,
  "editor.cursorBlinking": "smooth",
  "workbench.reduceMotion": "off",
  "editor.minimap.sectionHeaderFontSize": 10,
  "editor.minimap.autohide": true,
  "background.windowBackgrounds": [
    "c:/Users/Administrator/Pictures/1351415.png"
  ],
  "workbench.sideBar.location": "right",
  "window.titleBarStyle": "native",
  "background.backgroundBlur": ["6px", "0", "0", "0"],
  "workbench.colorTheme": "Bearded Theme Vivid Black",
  "editor.codeLensFontFamily": "JetBrains Mono",
  "editor.inlayHints.fontFamily": "JetBrains Mono",
  "editor.fontLigatures": true,
  "explorer.compactFolders": false,
  "apc.header": {
    "height": 36
  },
  "apc.font.family": "JetBrains Mono",
  "apc.listRow": {
    "height": 24
  },
  "apc.stylesheet": {
    ".title-label > h2": "display: none",
    ".editor-actions": "display: none",
    ".nosidebar .inline-tabs-placeholder": "width: 75px",
    ".pane-header": "padding: 0 8px",
    ".pane-body": "padding: 8px",
    ".split-view-view:first-child .pane-header": "display: none !important;",
    ".monaco-list-row": "border-radius: 4px;",
    ".monaco-workbench .monaco-list:not(.element-focused):focus:before": "display: none;"
  },
  "editor.scrollbar.vertical": "hidden",
  "terminal.integrated.fontSize": 14,
  "terminal.integrated.fontFamily": "JetBrains Mono",
  "explorer.confirmDragAndDrop": false,
  "explorer.confirmDelete": false,
  "workbench.activityBar.location": "top",
  "window.menuBarVisibility": "hidden",
  "editor.formatOnSave": true,
  "editor.defaultFormatter": "esbenp.prettier-vscode",
  "apc.monospace.font.family": "JetBrains Mono",
  "window.title": "VSCode do Zé 🤙"
}'''
