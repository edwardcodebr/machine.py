def mediaa(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3
    return media

def mediag(medias):
    mediageral = sum(medias) / len(medias)
    return mediageral

print("Digite quantos alunos existem")
aluno = int(input())

medias = []

for i in range(aluno):
    print(f'Digite a primeira nota do aluno {i + 1}')
    nota1 = float(input())
    print("Segunda nota")
    nota2 = float(input())
    print("Terceira nota")
    nota3 = float(input())
    
    median = mediaa(nota1, nota2, nota3)
    medias.append(median)
    print(f"A média do aluno {i + 1} é {median}")

for i in range(aluno):
    print(f"Aluno {i + 1}: média {medias[i]}")

mediageral = mediag(medias)
print(f"A média geral é {mediageral}")
