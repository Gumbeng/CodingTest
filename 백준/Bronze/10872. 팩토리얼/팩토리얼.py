n = int(input())
if n > 0 and n <= 12 and n != 0:
    answer = n
    for i in range(1,n):
        answer *= (n-i)
    print(answer)
else:
    print(1)