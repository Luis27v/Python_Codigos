t = int(input())
n = [i % t for i in range(1000)]

for i,j in enumerate(n):
    print(f'N[{i}] = {j}')