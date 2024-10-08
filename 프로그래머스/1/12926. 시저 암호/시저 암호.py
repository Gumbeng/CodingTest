def solution(s, n):
    s = list(s)
    answer = ''
    for i in s:
        if i == ' ':
            answer += ' '
            continue
        if ord(i) in range(65,90+1):
            #대문자
            if ord(i) +n > 90:
                answer += chr((ord(i) +n) - 90 + 64)
            else:
                answer += chr(ord(i) +n)
        else:
            #소문자
            if ord(i) +n > 122:
                answer += chr((ord(i) +n) - 122 + 96)
            else:
                answer += chr(ord(i)+n)
    return answer