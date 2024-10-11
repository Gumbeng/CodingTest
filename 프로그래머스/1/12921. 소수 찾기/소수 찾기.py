def solution(n):
    answer = 0
    for i in range(2, n+1):
        if sosu(i) == True:
            answer += 1
    return answer

def sosu(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True