def solution(s):
    temp = list(map(str, s))
    temp.sort(reverse = True)
    answer = ''
    for i in temp:
        answer += i
    return answer