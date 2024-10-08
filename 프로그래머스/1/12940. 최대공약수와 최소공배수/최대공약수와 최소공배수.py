def solution(n, m):
    answer = [s(n,m), int((n*m) / s(n,m))]
    return answer

def s(x,y):
    if y == 0:
        return x
    if x % y == 0:
        return y
    else:
        return s(y, x%y)