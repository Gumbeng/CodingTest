n = int(input())
arr = []
for i in range(n):
    age,name = input().split()
    age = int(age)
    arr.append((age,i,name))
arr.sort(key=lambda x: (x[0],x[1]))
for a,b,c in arr:
    print(a,c)