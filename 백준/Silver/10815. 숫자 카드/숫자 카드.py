N = int(input())
arr = list(map(int,input().split()))
S = int(input())
arr2 = list(map(int,input().split()))
temp = {}
for i in range(N):
    temp[arr[i]] = 0
for i in range(S):
    if arr2[i] in temp:
        print(1, end=" ")
    else:
        print(0, end=" ")