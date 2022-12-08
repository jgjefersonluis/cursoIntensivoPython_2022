aliens=[]
for num in range(30):
    alien = {
        'cor':'verde',
        'pontos': 5,
        'pos_x':7,
        'pos_y':27,
        'veloc':'baixa'
    }
#aliens.append(aliens)
for alien in aliens [:3]:
    alien['cor'] = 'amarelo'
    alien['pontos'] = 10
    alien['veloc'] = 'media'
for alien in aliens:
    print(alien)
for alien in aliens:
    if alien['veloc'] == 'baixa':
        alien['pos_x'] = alien ['pos_x'] + 1
    elif alien ['veloc'] == 'media':
        alien['pos_x'] = alien['pos_x'] + 2
    else:
        alien['pos_x'] = alien ['pos_x'] + 3

for alien in aliens:
    print(alien)
print('Total de aliens na lista é ' + str(len(aliens)))
