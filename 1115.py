while True:
    x, y = map(int, input().split(' '))
    if x * y > 0:
        print ("primeiro" if x > 0 else "terceiro")
    elif x * y < 0:
        print ("quarto" if x < 0 else "segundo")
    else: 
        break