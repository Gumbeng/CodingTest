n = int(input())
n_str = str(n)
arr = []
for i in range(len(n_str)):
    arr.append(int(n_str[i]))
arr.sort(reverse = True)
for i in range(len(arr)):
    print(arr[i], end="")
