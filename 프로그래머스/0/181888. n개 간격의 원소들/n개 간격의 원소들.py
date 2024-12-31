def solution(num_list, n):
    answer = []
    cnt = 0
    answer.append(num_list[0])
    for i in num_list:
        if cnt == n:
            answer.append(i)
            cnt = 0
        cnt += 1
    
    return answer