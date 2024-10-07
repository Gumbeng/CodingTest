def solution(x):
    temp = list(map(int,str(x)))
    answer = True if x % sum(temp) == 0 else False
    return answer