respostas = {
    'joao':'python',
    'maria':'c',
    'carlos':'ruby',
    'joana':'python',
    'marcelo':'java'
 }

 # escreve na tela as pessoas que votaram
for nome in respostas.keys():
    print('O ' + nome.title() + ' votou')
# pula uma linha
print('\n')
# monta lista de pessoas que devem votar
obrigados = ['joao', 'eduardo','jeferson']
# verifica se todos votaram. Caso não, escreva
# o nome dos que não votaram
for nome in obrigados:
    if nome not in respostas.keys():
        print(nome.title() + 'não votou!')
