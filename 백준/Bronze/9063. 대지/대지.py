a = int(input())
n = []
x = []
y = []
if a == 1: # 값이 하나라면 0 출력
    print(0)
else:
    for i in range(a): # a만큼 입력
        n.append(list(map(int,input().split()))) # 배열에 넣어준다
        x.append(n[i][0])
        y.append(n[i][1])
    print((max(x) - min(x)) * (max(y) - min(y)))