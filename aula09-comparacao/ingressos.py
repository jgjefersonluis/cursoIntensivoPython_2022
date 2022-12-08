# variavel que armazena a idade do cliente que comprara o ingresso
idade = 18
# de acordo com a idade, vamos definir a variavel preco com o valor a ser pago pelo cliente
if idade <= 5:
    preco = 0
elif idade <= 12:
    preco = 5
elif idade <= 18:
    preco = 10
elif idade <= 65:
    preco = 15
else:
    preco = 0
print("O preco do ingresso para sua faixa de idade é : " + str(preco))
