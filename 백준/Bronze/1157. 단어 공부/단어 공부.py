t = input().upper()
n = list(set(t))

t_cnt = []

for i in n:
    t_cnt.append(t.count(i))
if t_cnt.count(max(t_cnt)) > 1:
    print("?")
else:
    print(n[t_cnt.index(max(t_cnt))])