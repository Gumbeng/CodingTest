N, M = map(int, input().split())
dic = {}
arr = [input() for _ in range(N+M)]
for i in arr:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
dic_item = sorted(dic.items())
result = ""
count = 0
for a,b in dic_item:
    if b == 2:
        result += a + " "
        count += 1
print(count)
print(result[:-1])