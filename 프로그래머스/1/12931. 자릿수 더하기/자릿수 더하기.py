def solution(n):
    n = str(n)
    answer = sum([int(n[i]) for i in range(len(n))])
    return answer