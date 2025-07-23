print("--- Calculadora de Soma de Números Pares em um Intervalo ---")

# --- Obtenção e validação do número inicial do intervalo ---
inicio_intervalo = int(input("Digite o número inicial do intervalo (inteiro): "))   
fim_intervalo = int(input("Digite o número final do intervalo (inteiro): "))


if inicio_intervalo > fim_intervalo:
    print(f"\nO início ({inicio_intervalo}) é maior que o fim ({fim_intervalo}). Invertendo o intervalo para você.")
    # Troca os valores das variáveis usando atribuição múltipla
    temp = inicio_intervalo
    inicio_intervalo = fim_intervalo
    fim_intervalo = temp

soma_pares = 0
encontrou_par = False # Flag para verificar se algum número par foi encontrado

# Loop 'for' para processar o intervalo
# range(inicio, fim + 1) inclui o 'fim' do intervalo
for numero in range(inicio_intervalo, fim_intervalo + 1):
    # Verifica se o número é par (o resto da divisão por 2 é zero)
    if numero % 2 == 0:
        soma_pares += numero
        encontrou_par = True # Marca que um número par foi encontrado

# Exibe o resultado com base na flag
if encontrou_par:
    print(f"\nNo intervalo de {inicio_intervalo} a {fim_intervalo}:")
    print(f"A soma dos números pares é: {soma_pares}")
else:
    # Esta parte será exibida se 'encontrou_par' for False
    print(f"\nNo intervalo de {inicio_intervalo} a {fim_intervalo}:")
    print("Não há números pares neste intervalo.")

print("\n--- Fim do programa. ---")