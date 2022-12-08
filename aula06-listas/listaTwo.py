pizzas = ['mussarela', 'calabreza', 'bacon com milho', 'strogonoff']
pedido = ['palmito', 'calabreza']
for pizzas in pedido:
    if pizzas in pizzas:
        print('O sabor pedido foi ' + pizzas + ' boa refeição!')
    else:
        print('O sabor da ' + pizzas + ' indisponivel!')
     