n, m = map(int, input().split())
baskets = [0] * n

for i in range(m):
    i, j, k = map(int, input().split())
    for l in range(i-1, j):
        baskets[l] = k

for i in range(n):
    print(baskets[i], end=' ')
