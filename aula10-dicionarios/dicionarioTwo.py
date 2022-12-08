alien_1 ={'cor':'vermelho', 'pontos': 10}
print("A cor do alien one é: " + alien_1['cor'])
pontos_novos = alien_1['pontos']
print("Se matar o alien one você ganha: " + str(pontos_novos))
alien_1['x_pos'] = 7
alien_1['y_pos'] = 25
print("A posição x do alien na tela é: " + str(alien_1['x_pos']))
print("A posição y do alien na tela é: " + str(alien_1['y_pos']))
print(alien_1)

