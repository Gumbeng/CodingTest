n = input()
cnt = 0
if len(n) % 10 != 0:
    cnt = len(n) // 10 + 1
else:
    cnt = len(n) // 10
temp = 10
for i in range(cnt):
    if i == 0:
        print(n[0:temp])
    else:
        print(n[i*10:temp])
    temp += 10