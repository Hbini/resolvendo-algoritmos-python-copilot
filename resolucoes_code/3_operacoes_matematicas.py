# 3 - Operações Matemáticas Simples
# Descrição: Realiza operações matemáticas simples entre dois números.

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

print(f"Adição: {num1 + num2}")
print(f"Subtração: {num1 - num2}")
print(f"Multiplicação: {num1 * num2}")
if num2 != 0:
    print(f"Divisão: {num1 / num2}")
else:
    print("Erro: Divisão por zero")
