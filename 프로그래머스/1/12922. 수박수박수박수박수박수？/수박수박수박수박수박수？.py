def solution(n):
    odd = "수"
    evn = "수박"
    answer = evn * (n//2) if n % 2 == 0 else evn * (n//2) + odd
    return answer