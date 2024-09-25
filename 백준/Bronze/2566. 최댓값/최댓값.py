n = []
temp_max = 0
temp_index = 0
temp_line = 0
for i in range(9):
    temp = list(map(int, input().split()))
    n.append(temp)
    if temp_max <= max(temp):
        temp_max = max(temp)
        temp_line = i + 1
        temp_index = n[i].index(temp_max) + 1
print(temp_max)
print(temp_line, temp_index)