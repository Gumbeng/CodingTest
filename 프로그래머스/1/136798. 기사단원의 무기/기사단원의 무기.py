def solution(number, limit, power):
    answer = 0
    temp = []
    for i in range(1,number+1):
        temp.append(gsf(i))
        
    for i in temp:
        if i > limit:
            answer += power
        else:
            answer += i
    return answer


# 약수의 개수
def gsf(n):
    result = 0
    for i in range(1,int(n**0.5)+1):
        if n % i == 0:
            result += 1
            if i**2 != n:
                result += 1
    return result
