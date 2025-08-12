valor = float(input('Digite o total a pagar (em R$): '))
taxa_servico = float(input('Digite a taxa de serviço (em %): '))

valor_taxa_servico = (taxa_servico * valor) / 100
total_pagar = valor + valor_taxa_servico

print(f"""
---------- COMPROVANTE ----------
Consumo total: R${valor:.2f}
Valor da Taxa de Serviço: R${valor_taxa_servico:.2f}
Total a pagar: R${total_pagar:.2f}
---------------------------------""")

              