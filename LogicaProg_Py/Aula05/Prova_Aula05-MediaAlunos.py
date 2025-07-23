print("--- Calculadora de Média de Notas da Turma ---")

# --- Obtenção do número de alunos com validação ---
num_alunos_valido = False
while not num_alunos_valido:
    num_alunos = int(input("Digite o número de alunos na turma: "))
    if num_alunos > 0:
        num_alunos_valido = True
    else:
        print("O número de alunos deve ser maior que zero. Tente novamente.")
else:
    print("Entrada inválida. Por favor, digite um número inteiro para o número de alunos.")

total_soma_turma = 0.0 # Inicializa a soma de todas as notas para a média geral da turma
num_notas_turma = 0    # Contador para o total de notas válidas processadas

print("\n--- Inserção das Notas dos Alunos ---")

# Loop 'for' para iterar sobre cada aluno
for i in range(num_alunos):
    print(f"\n--- Aluno {i + 1} ---")
    
    # Obtenção do nome do aluno
    nome_aluno = input("Digite o nome do aluno: ")
    while not nome_aluno: # Valida se o nome não está vazio
        print("O nome do aluno não pode ser vazio.")
        nome_aluno = input("Digite o nome do aluno: ")

    # Para exibir as notas de cada aluno é necessário a criação de uma LISTA (Solução IA)
    # --- Inicializa uma lista vazia ---
    notas_aluno = [] 

    # Loop 'for' para iterar sobre as três notas de cada aluno
    for j in range(3):
        nota_valida = False
        while not nota_valida:
            nota_str = input(f"  Digite a nota {j + 1} para {nome_aluno}: ")
            
            # Validação manual para float (números com ponto decimal)
            if nota_str:
                ehNumero = True
                cont_ponto = 0
                # verificar se a string é um número float válido
                for char in nota_str:
                    if char == '.':
                        cont_ponto += 1
                    # Verifica se é um dígito ou -
                    elif not ('0' <= char <= '9' or (char == '-' and nota_str.index(char) == 0)):
                        ehNumero = False
                        break
                
                # Validação final do formato numérico e do intervalo de notas
                # 'len(nota_str) > 1' e a segunda parte do 'or' evita que apenas '.' ou '-' sejam considerados válidos
                if ehNumero and cont_ponto <= 1 and (len(nota_str) > 1 or (nota_str == '0' or nota_str == '-0')): 
                    nota = float(nota_str)
                    if 0.0 <= nota <= 10.0: # Valida o intervalo da nota
                        notas_aluno.append(nota) # Adiciona a nota à lista do aluno
                        total_soma_turma += nota # Adiciona à soma total da turma
                        num_notas_turma += 1     # Incrementa o contador de notas da turma
                        nota_valida = True
                    else:
                        print("A nota deve estar entre 0.0 e 10.0. Tente novamente.")
                else:
                    print("Entrada inválida. Por favor, digite um número para a nota (ex: 7.5).")
            else:
                print("A nota não pode ser vazia. Por favor, digite um número.")

    # Calcula a soma das notas do aluno usando a lista
    soma_notas_aluno = 0.0
    for nota_individual in notas_aluno: # Itera sobre a lista para somar
        soma_notas_aluno += nota_individual

    # Calcula a média do aluno
    media_aluno = soma_notas_aluno / len(notas_aluno) # Usa len() para o número de notas

    # Exibe os resultados do aluno
    print(f"\n--- Resumo de {nome_aluno} ---")
    print(f"Notas: {notas_aluno}") # Exibe a lista completa de notas
    print(f"Média: {media_aluno:.2f}") # Formata a média com 2 casas decimais

    # Verifica aprovação/reprovação
    if media_aluno >= 7.0:
        print("Situação: APROVADO!")
    else:
        print("Situação: REPROVADO!")

# Calcula e exibe a média geral da turma
print("\n--- Resumo Final da Turma ---")
if num_notas_turma > 0: # Evita divisão por zero se nenhuma nota válida foi inserida
    media_geral_turma = total_soma_turma / num_notas_turma
    print(f"A média geral da turma é: {media_geral_turma:.2f}")
else:
    print("Não foi possível calcular a média geral da turma (nenhuma nota válida inserida).")

print("\n--- Programa Concluído ---")