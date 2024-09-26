a,b = map(int, input().split())
count = [v for v in range(1,a+1) if a % v == 0]
temp = 0 if len(count) < b else count[b-1]
print(temp)