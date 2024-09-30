n, m = map(int, input().split())
arr = list(map(int,input().split()))
total = []
for i in range(n):
    for k in range(i+1, n):
        for j in range(k+1, n):
            if arr[i] + arr[k] + arr[j] <= m:
                total.append(arr[i] + arr[k] + arr[j])
print(max(total))