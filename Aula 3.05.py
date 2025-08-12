cidade = input('Digite a cidade: ')
temperatura = int(input('Digite a temperatura (em °C): '))
umidade = int(input('Digite a umidade do ar (em %): '))
condicao_tempo = input('Digite a condição do tempo (ex: ensolarado, nublado, chuvoso): ')

print(f"""
----- Previsão do Tempo -----
Cidade: {cidade}
Temperatura: {temperatura}°C
Umidade: {umidade}%
Condição: {condicao_tempo}
-----------------------------""")