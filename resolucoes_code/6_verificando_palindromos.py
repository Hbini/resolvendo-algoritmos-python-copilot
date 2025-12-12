# 6 - Verificando Palíndromos
# Descrição: Verifica se uma palavra é um palíndromo.

palavra = input("Digite uma palavra: ").lower().replace(" ", "")

palavra_invertida = palavra[::-1]

if palavra == palavra_invertida:
    print(f"{palavra} é um palíndromo!")
else:
    print(f"{palavra} não é um palíndromo")
