alien = {}
alien['cor'] = 'verde'
alien['pontos'] = 5
alien['veloc'] = 'baixa' # trocar para media
alien['x_pos'] = 7
alien['y_pos'] = 25
print('A posição x do alien é ' + str(alien['x_pos']))
if alien ['veloc'] == 'baixa':
    x_incr = 1
if alien ['veloc'] == 'media':
    x_incr = 2
else:
    x_incr = 3
alien ['x_pos'] = alien ['x_pos'] + x_incr
print('A posição x do alien é ' + str (alien['x_pos']))
