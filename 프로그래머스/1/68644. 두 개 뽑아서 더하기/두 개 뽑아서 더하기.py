def solution(numbers):
    answer = []
    for i in range(len(numbers) -1):
        for k in range(i+1, len(numbers)):
            answer.append(numbers[i]+numbers[k])
    s = set(answer)
    answer = sorted(list(s))
    
    return answer