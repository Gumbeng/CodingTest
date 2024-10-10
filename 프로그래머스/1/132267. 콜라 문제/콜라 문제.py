def solution(a, b, n):
    # 빈병 a
    # a병 주면 콜라 b받음
    # 빈병 = n
    answer = 0
    while n >= a:
        temp = n % a # 교환 후 남은 병
        n = (n // a) * b # 마트에서 받은 콜라의 수 
        answer += n # answer에 넣어준다
        n += temp #  교환 후 남은 병을 담아준다.
    return answer

6
