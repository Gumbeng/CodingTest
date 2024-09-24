N, M = map(int, input().split())
numbers = [i for i in range(1, N+1)]
for i in range(M):
    j,k = map(int, input().split())
    te = numbers[j-1:k]
    te.reverse()
    numbers[j-1:k] = te
for i in range(N):
    print(numbers[i], end=" ")