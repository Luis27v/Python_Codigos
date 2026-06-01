n = int(input())
vetor = input()
vetor = vetor.split()
vetor = map(int, vetor)
vetor = list(vetor)
menor = min(vetor)

print(f'menor valor: {menor}')
print(f'posição: {vetor.index(menor)}')