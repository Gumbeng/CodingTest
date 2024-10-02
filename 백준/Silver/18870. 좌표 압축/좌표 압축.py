n = int(input())
arr = list(map(int,input().split()))
temp = list(set(arr))
temp.sort()
dic = {temp[i] : i for i in range(len(temp))}
for i in arr:
    print(dic[i], end=" ")