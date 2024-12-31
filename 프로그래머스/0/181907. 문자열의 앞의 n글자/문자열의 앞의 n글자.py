def solution(my_string, n):
    answer = ''
    cnt = 0
    for i in my_string:
        cnt += 1
        answer += i
        if cnt == n:
            break
    return answer