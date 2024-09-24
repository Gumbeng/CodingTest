t = int(input())
for i in range(t):
    a,b = input().split()
    length = len(b)
    for j in range(length):
        print(b[j] * int(a), end = '')
    print()