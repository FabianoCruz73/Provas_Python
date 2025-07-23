# Credenciais corretas
usuario_correto = "admin"
senha_correta = "12345"

# Número máximo de tentativas
limite_tentativas = 3

print("--- Sistema de Login ---")

# Loop para as tentativas de login
for tentativa_atual in range(1, limite_tentativas + 1):
    print(f"\nTentativa {tentativa_atual} de {limite_tentativas}:")
    
    # Solicita o nome de usuário
    usuario_digitado = input("Nome de usuário: ")
    
    # Solicita a senha
    senha_digitada = input("Senha: ")
    
    # Verifica se as credenciais estão corretas
    if usuario_digitado == usuario_correto and senha_digitada == senha_correta:
        print(f"\nBem-vindo(a), {usuario_correto}! Login bem-sucedido.")
        break # Sai do loop imediatamente se o login for bem-sucedido
    else:
        # Se as credenciais estiverem incorretas
        tentativas_restantes = limite_tentativas - tentativa_atual
        if tentativas_restantes > 0:
            print(f"Credenciais incorretas. Você tem {tentativas_restantes} tentativa(s) restante(s).")
        else:
            # Esta parte só será executada na última tentativa se o usuário errar
            print("Credenciais incorretas. Nenhuma tentativa restante.")

# Se o loop 'for' terminar sem um 'break' (ou seja, todas as tentativas falharam)
else:
    for _ in range(3): # Loop 'for' para exibir a mensagem 3 vezes
        print("--- Acesso Bloqueado ---")

print("\n--- Fim do programa ---")