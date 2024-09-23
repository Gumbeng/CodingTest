X = int(input())
A = map(int, input().split())
A = sorted(A)
print(A[0], A[X-1])