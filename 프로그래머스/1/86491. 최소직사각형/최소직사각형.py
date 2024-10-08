def solution(sizes):
    for i in sizes:
        i.sort()
    print(sizes)
    x=[]
    y=[]
    for i,k in sizes:
        x.append(i)
        y.append(k)
    answer = max(x) * max(y)
    return answer