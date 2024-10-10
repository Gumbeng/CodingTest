def solution(n, arr1, arr2):
    answer = []
    cnt = 0
    for a,b in zip(arr1,arr2):
        arr1[cnt] = bin(a)[2:].zfill(n)
        arr2[cnt] = bin(b)[2:].zfill(n)
        cnt += 1
    temp = []
    temp2 = []
    for a,b in zip(arr1,arr2):
        temp.append(list(a))
        temp2.append(list(b))
    rs = []
    for a in range(n):
        ts = []
        for b in range(n):
            if temp[a][b] == '1' or temp2[a][b] == '1':
               ts.append('#')
            else:
                ts.append(' ')
        rs.append(ts)
    for a in range(n):
        tems = ''
        for b in range(n):
            tems += rs[a][b]

        answer.append(tems)
    return answer