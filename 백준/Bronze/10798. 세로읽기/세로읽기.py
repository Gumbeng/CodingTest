arr = []
st = ""
max_len = 0
for i in range(5):
    temp = list(input())
    arr.append(temp)
    if len(temp) > max_len:
        max_len = len(temp)
cnt = 0
for i in range(max_len):
    for k in range(5):
        if i < len(arr[k]): # 인덱스가 배열의 길이를 넘지 않도록 체크
            st += arr[k][i]
print(st)