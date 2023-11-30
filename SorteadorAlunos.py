import random
n_alunos = int(input('Digite a quantidade de alunos: '))
nomes_alunos = []
for i in range(n_alunos):
    nome = input(f'Digite o nome do aluno {i + 1}: ')
    nomes_alunos.append(nome)

print('Lista dos alunos')
for nome in nomes_alunos:
    print(nome)

print(f'O(A) representante de sala será: {random.choice(nomes_alunos)}')
random.shuffle(nomes_alunos)
print(f'A ordem de apresentações do trabalho será: {nomes_alunos}')