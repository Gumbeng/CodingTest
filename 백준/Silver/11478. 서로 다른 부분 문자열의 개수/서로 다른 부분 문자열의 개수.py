a = input()
arr = []
count = 1
while count < len(a) + 1:
    for i in range(len(a)):
        if a[i:count] != '':
            arr.append(a[i:count])
    count += 1
print(len(set(arr)))