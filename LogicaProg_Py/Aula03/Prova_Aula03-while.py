# O número secreto que o jogador deve adivinhar
numero_secreto = 5

# O número máximo de tentativas permitidas
limite_tentativas = 3

# Contador para o número de tentativas que o jogador já usou
tentativa_atual = 0

print("Bem-vindo ao Jogo da Adivinhação!")
print(f"Tente adivinhar o número secreto entre 1 e 10.")
print(f"Você tem {limite_tentativas} tentativas.")

# Loop while para permitir múltiplas tentativas
while tentativa_atual < limite_tentativas:
    palpite = int(input(f"Tentativa {tentativa_atual + 1}/{limite_tentativas}: Digite seu palpite: "))
    # Verifica se o palpite está correto
    if palpite == numero_secreto:
        print("\n--- Parabéns! Você acertou o número secreto! ---")
        break  # Sai do loop se o jogador acertar
    else: # palpite > ou < numero_secreto
        print("Vamos lá! Tente novamente!")     
    # Incrementa o contador de tentativas
    tentativa_atual += 1
else: # tentativa_atual == limite_tentativas:
    print("\n--- Suas tentativas acabaram! ---")
    print("--- Mais sorte da próxima vez! ---")
print("\nFim do jogo.")