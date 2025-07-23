# Solicita o número de alunos
num_alunos = int(input("Digite o número de alunos: "))

# Lista para armazenar as médias
medias = []

# Loop principal para cada aluno
for i in range(num_alunos):
    # Solicita o nome do aluno
    nome = input(f"\nDigite o nome do aluno {i + 1}: ")
    
    # Lista para armazenar as notas do aluno
    notas = []
    
    # Loop para coletar as três notas
    for j in range(3):
        nota = float(input(f"Digite a nota {j + 1} do aluno: "))
        notas.append(nota)
    
    # Calcula a média do aluno
    media = sum(notas) / 3
    medias.append(media)
    
    # Exibe as informações do aluno
    print(f"\nAluno: {nome}")
    print("Notas:", end=" ")
    for nota in notas:
        print(f"{nota:.1f}", end=" ")
    print(f"\nMédia: {media:.1f}")
    
    # Verifica e exibe o status de aprovação
    if media >= 7.0:
        print("Status: APROVADO")
    else:
        print("Status: REPROVADO")

# Calcula e exibe a média geral da turma
media_geral = sum(medias) / num_alunos
print(f"\nMédia geral da turma: {media_geral:.1f}")