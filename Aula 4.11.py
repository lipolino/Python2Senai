'''
Multa de Pesca

João, um pescador, comprou um microcomputador para controlar o rendimento diário de seu trabalho. 

Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. 

João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. 

Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.
'''

peso = int(input('Digite o peso do peixe em KG: '))
excesso = peso - 50
multa = 0

if peso > 50:
    multa = excesso * 4
    total = 50 + multa
else:
    total = peso

print(f'''
----------------------
Peso do peixe: {peso} KG
Multa a pagar: R${multa:.2f} 
Total a pagar: R${total:.2f}
----------------------''')