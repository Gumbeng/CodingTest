arr = ["factor", "multiple", "neither"]

while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    factor = b / a
    s = b // a
    multiple = a % b
    if factor - s == 0:
        print(arr[0])
    elif multiple == 0:
        print(arr[1])
    else:
        print(arr[2])    