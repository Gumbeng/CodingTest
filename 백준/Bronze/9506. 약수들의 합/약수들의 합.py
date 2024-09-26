while True:
    n = int(input())
    if n == -1:
        break
    arr = [v for v in range(1, n+1) if n % v == 0]
    result = ''
    if sum(arr) - n == n:
        for i in range(len(arr) -1):
            result += str(arr[i]) + " + "
        print(n, "=",result[0:len(result)-2])
    else:
        result = "is NOT perfect."
        print(n,result)
