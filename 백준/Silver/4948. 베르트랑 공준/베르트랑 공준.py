def sss(a):
    if a == 1:
        return False
    else:
        for i in range(2,int(a**0.5) +1):
            if a % i == 0:
               return False
        return True
arr = list(range(2,246912))
temp = []
for i in arr:
    if sss(i):
        temp.append(i)

while True:
    cnt = 0
    n = int(input())
    if n == 0:
        break
    for i in temp:
        if n < i and n*2 >= i:
            cnt += 1
    print(cnt)