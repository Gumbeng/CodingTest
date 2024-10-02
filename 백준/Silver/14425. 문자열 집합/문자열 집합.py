n, m = map(int, input().split())
S = []
for _ in range(n):
    S.append(input())
temp = []
for _ in range(m):
    temp.append(input())
count = 0
_dict = {}
for i in range(n):
    _dict[S[i]] = 0
for i in range(m):
    if temp[i] in _dict:
        count += 1
    else:
        continue
print(count)