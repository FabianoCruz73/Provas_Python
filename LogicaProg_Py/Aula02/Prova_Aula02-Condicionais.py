# Solicita inserir um número.
# int() usado para apenas números inteiros.
numero = int(input("Digite um número inteiro: "))

# Verifica a natureza do número usando if-elif-else.
if numero > 0:
    print(f"O número {numero} é positivo.")
elif numero < 0:
    print(f"O número {numero} é negativo.")
else:
    print(f"O número {numero} é zero.")