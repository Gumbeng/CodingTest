T = int(input())
result = [0] * (T)

for i in range(T):
    a,b = map(int, input().split())
    result[i] = a + b
for i in range(T):
    print(result[i])