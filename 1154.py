age = float(input())
sum = 0
i = 0

while(age >= 0):
    sum += age
    age = float(input())
    i += 1

media = float(sum / i)
print(f'{media:.2f}')