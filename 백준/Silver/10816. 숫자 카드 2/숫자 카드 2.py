N = int(input())
aww = list(map(int,input().split()))
_da = {i:0 for i in set(aww)}
M = int(input())
temp = list(map(int,input().split()))
for i in aww:
    _da[i] += 1
for i in temp:
    if _da.get(i) == None:
        print(0,end=" ")
    else:
        print(_da.get(i), end=" ")