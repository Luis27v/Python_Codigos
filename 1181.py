line = int(input())
op = input()
m = [] 

for i in range(12):
    linem = []

    for j in range(12):
        linem.append(float(input()))
    m.append(linem)

result = sum(m[line])

if op == "M":
    result = result / 12
    print(f'the result is: {result:.1f}')