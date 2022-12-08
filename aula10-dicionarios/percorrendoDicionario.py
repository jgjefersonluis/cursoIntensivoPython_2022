respostas = {
    'joao':'python',
    'maria':'c',
    'carlos':'ruby',
    'joana':'python',
    'marcelo':'java'
 }
for linguagem in sorted(set(respostas.values())):
    print('A linguagem' + linguagem.title() + 'foi mensionada')
    