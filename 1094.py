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