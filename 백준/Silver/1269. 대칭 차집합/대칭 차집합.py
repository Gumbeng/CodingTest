import sys
n,m = map(int,sys.stdin.readline().split())
a = list(map(int,sys.stdin.readline().split()))
b = list(map(int,sys.stdin.readline().split()))
for i in range(len(b)):
    a.append(b[i])
dic = {}
for i in a:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
count = 0
for a in dic.values():
    if a == 1:
        count += 1
    continue
print(count)