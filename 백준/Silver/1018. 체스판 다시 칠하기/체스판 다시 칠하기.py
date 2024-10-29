M,N = map(int, input().split())
arr = []
for _ in range(M):
    arr.append(list(input()))
cnt = []
for a in range(M-7):
    for b in range(N-7):
        index1 = 0
        index2 = 0
        for i in range(a, a+8):
            for j in range(b,b+8):
                if (i+j) % 2 == 0:
                    if arr[i][j] != 'W':
                        index1 += 1
                    if arr[i][j] != 'B':
                        index2 += 1
                else:
                    if arr[i][j] != 'B':
                        index1 += 1
                    if arr[i][j] != 'W':
                        index2 += 1
        cnt.append(min(index1, index2))
print(min(cnt))