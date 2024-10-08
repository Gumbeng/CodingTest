def solution(food):
    left = ''
    right = ''
    # food[0] 을 뺀 [1] 인덱스 부터 각 음식의 절반을 left에 추가한다
    for i in range(1, len(food)):
        left += str(i) * (food[i]//2)
    # left 에 추가한 만큼 동일하게 역순으로 right에 넣어준다.
    right = left[::-1]
    # left 끝에 물의 양을 추가해준다 (물의 양은 1로 고정)
    left += '0'
    return left + right