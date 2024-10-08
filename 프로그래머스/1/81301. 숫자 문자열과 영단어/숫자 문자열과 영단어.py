def solution(s):
    answer = ''
    temp = ''
    number = '0123456789'
    dit = {'zero':0, 'one':1, 'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9}
    for i in list(s):
        if i in number:
            answer += i
            continue
        else:
            temp += i
        if temp in dit:
            answer += str(dit.get(temp))
            temp = ''
    return int(answer)