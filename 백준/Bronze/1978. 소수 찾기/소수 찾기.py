n = int(input())
arr = list(map(int, input().split()))
count = 0
for i in arr:
    if i == 1:
        continue
    for v in range(2, i):
        if i % v == 0:
            break
    else:
        count += 1
print(count)
            