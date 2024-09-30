a,b,c = map(int,input().split())
temp = [a,b,c]
temp.sort()
if temp[2] >= temp[0] + temp[1]:
    temp[2] = temp[0] + temp[1] - 1
    print(sum(temp))
elif a == b and a == c and b == c:
    print(sum(temp))
elif temp[2] < temp[0] + temp[1]:
    print(sum(temp))