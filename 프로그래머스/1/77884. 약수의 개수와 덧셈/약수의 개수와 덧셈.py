def solution(left, right):
    answer = 0
    for i in range(left, right + 1):
        temp = sol(i)
        if temp % 2 == 0:
            answer += i
        else:
            answer -= i
    return answer

def sol(x): # 약수의 개수 return
    temp = []
    for i in range(1, x+1):
        if x % i == 0:
            temp.append(i)
    return len(temp)