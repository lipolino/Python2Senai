preco_mercadoria = float(input('Digite o preço da mercadoria (em R$): '))
desconto = float(input('Digite o percentual de desconto (em %): '))

valor_desconto = (preco_mercadoria * desconto) / 100
total_pagar = preco_mercadoria - valor_desconto

print(f"""
-------- COMPROVANTE --------
Preço da Mercadoria: {preco_mercadoria}
Valor do Desconto: {valor_desconto}
Total a pagar: {total_pagar}""")
                         