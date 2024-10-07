def gcd(m,n):
    if m < n:
        m, n = n,m
    if n == 0:
        return m
    if m % n == 0:
        return n
    else:
        return gcd(n, m%n)
n = int(input()) # 입력값
a = int(input()) # 첫 번째 가로수
arr = []
for i in range(n-1): # 가로수의 차
    num = int(input())
    arr.append(num -a)
    a = num
g = arr[0]
for i in range(1, len(arr) ):
    g = gcd(g,arr[i])
result = 0
for i in arr:
    result += i // g -1
print(result)