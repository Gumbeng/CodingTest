n = int(input())
cnt = 1
for i in range(n-1,-1,-1):
    print((" " * i) + ('*' * cnt))
    cnt += 2