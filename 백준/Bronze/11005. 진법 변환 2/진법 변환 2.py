a,b = map(int,input().split())

num_list = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
s = ""
while a:
    s += str(num_list[a%b])
    a //= b
11
print(s[::-1])