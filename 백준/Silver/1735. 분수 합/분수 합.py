a = list(map(int, input().split()))
b = list(map(int, input().split()))
x = a[0] * b[1] + b[0] * a[1]
y = a[1] * b[1]
num_max = max(x,y)
num_min = min(x,y)
while num_max > 0:
    if num_max % num_min == 0:
        break
    temp = num_min
    num_min = int(num_max % num_min)
    num_max = temp
print(int(x//num_min),int(y//num_min))