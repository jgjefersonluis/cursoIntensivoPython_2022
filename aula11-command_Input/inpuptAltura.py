prompt = "Qual a sua altura em metros?"
mensagem = input(prompt)
altura = int(mensagem)

if altura > 1:
    print(altura + " metros.")
else: 
    print("Voçê não tem altura suficiente para este brinquedo.")
