n, m = map(int, input().split())
arr = {}
arr_name = {}
for i in range(n):
    name = input()
    arr[i] = name
    arr_name[name] = i
for i in range(m):
    prog = input()
    if prog.isdecimal() == True:
        print(arr[int(prog) -1])
    else:
        print(int(arr_name[prog]) + 1)