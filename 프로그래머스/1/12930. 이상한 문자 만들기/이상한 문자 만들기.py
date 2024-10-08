def solution(s):
    temp = list(s.split(" "))
    answer = ''
    for i in temp:
        cnt = 0
        while cnt <= len(i) -1:
            if cnt % 2 == 0:
                answer += i[cnt].upper()
            else:
                answer += i[cnt].lower()
            cnt += 1
        answer += ' '
    return answer[:-1]