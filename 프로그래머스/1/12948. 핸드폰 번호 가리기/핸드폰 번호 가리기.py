def solution(a):
    answer = ''
    for i in range(len(a)):
        if i < len(a) -4:
            answer += '*'
        else:
            answer += a[i]
    return answer