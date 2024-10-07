n, m = map(int, input().split())
x = n * m
while m != 0:
    if n < m:
        n,m = m,n
    t = n % m
    n = m
    m = t
print(int(x / n))