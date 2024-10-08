def solution(s):
    answer = [-1 for i in range(len(s))]
    over = {}
    
    s = list(s)
    for i in range(len(s)):
        if s[i] not in over: # 처음 들어간다면
            over[s[i]] = i # 딕셔너리에 몇번째 자리인지 함께 넣어준다
        else: # 그렇지 않다면
            answer[i] = i - over[s[i]] # 중복되는 알파벳의 자릿수 에서 중복되는 알파벳 자릿수를 뺴준다 (몇번쨰만큼인지)
            over[s[i]] = i # 딕셔너리 자리수도 갱신 시켜준다
    return answer