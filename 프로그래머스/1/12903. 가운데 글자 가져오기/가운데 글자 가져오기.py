def solution(s):
    length = len(s) // 2
    answer = s[length] if len(s) % 2 != 0 else s[length -1] + s[length]
    return answer