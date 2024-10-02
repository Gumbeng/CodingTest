n = int(input())
arr = []
for _ in range(n):
    arr.append(input())
arr = set(arr)
arr = list(arr)
temp = []
for i in range(len(arr)):
    temp.append((len(arr[i]), arr[i]))
temp.sort()
for _ , i in temp:
    print(i)