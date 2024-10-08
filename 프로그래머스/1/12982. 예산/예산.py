def solution(d, budget):
    answer = 0
    while True:
        if sum(d) <= budget:
            answer = len(d)
            break
        else:
            d.remove(max(d))
    
    return answer