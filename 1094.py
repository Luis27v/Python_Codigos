coelhos = ratos = sapos = total = 0

for i in range (int(input())):
    qtde, animal = input(). split()
    total += int(qtde)

    if animal == 'c':
        coelhos += int(qtde)
    elif animal == 'r':
        ratos += int(qtde)
    elif animal == 's':
        sapos += int(qtde)

print(f'Total: {total} cobaias')
print(f'Total de Coelhos: {coelhos}')
print(f'Total de Ratos: {ratos}')
print(f'Total de Sapos: {sapos}')
print (f'Percentual de coelhis: {((100.0/total) * coelhos): .2f}')
print (f'Percentual de ratis: {((100.0/total) * ratos): .2f}')
print (f'Percentual de sapis: {((100.0/total) * sapos): .2f}')