# Solicita a base do retângulo
# float() - entrada um número decimal
base = float(input("Digite o valor (cm) da base do retângulo: "))

# Solicita a altura do retângulo
altura = float(input("Digite o valor (cm) da altura do retângulo: "))

# Calcula a área
area = base * altura

# Exibe a área calculada
# f-string formata a saída
print(f"A área do retângulo com base {base} e altura {altura} é: {area} cm²")