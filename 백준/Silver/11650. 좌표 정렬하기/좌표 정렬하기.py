n = int(input())
arr = []
for i in range(n):
    arr.append(tuple(map(int, input().split())))
arr.sort()
for x,y in arr:
    print(x,y)