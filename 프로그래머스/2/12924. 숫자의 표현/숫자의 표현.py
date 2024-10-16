def solution(n):
    answer = 0
    cnt = 0
    for i in range(1,n+1):
        answer = i
        for k in range(i+1, n+1):
            if answer == n:
                cnt += 1
                break
            if answer > n:
                break
            answer += k
    return cnt +1