x = []
y = []
result = []
for i in range(3):
    temp = list(map(int, input().split()))
    x.append(temp[0])
    y.append(temp[1])
for i in range(3):
    if x.count(x[i]) % 2 == 0:
        continue
    result.append(x[i])

for i in range(3):
    if y.count(y[i]) % 2 == 0:
        continue
    result.append(y[i])
print(result[0], result[1])