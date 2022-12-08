# lista de dicionarios de lista

pedidos = [

    {'espessura':'grossa', 'coberturas':[
        'molho de tomate','mussarela','catupiry'
    ]},
    
    {'espessura':'fina', 'coberturas':[
        'cebola','catupiry'
    ]},

    {'espessura':'grossa', 'coberturas':[
        'molho de tomate','mussarela','cebola'
    ]}

]
print("...Pedidos pendentes para cozinha...")
for pedido in pedidos:
    print("Pedidos com massa" + pedido['espessura'] + ":")
    print("\t As coberturas são: ")
    for cobertura in pedido ['coberturas']:
        print("\t" + cobertura)