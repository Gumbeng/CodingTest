def solution(name, yearning, photo):
    answer = []
    temp = {a:b for a,b in zip(name,yearning)}
    
    for i in photo:
        total = 0
        for k in range(len(i)):
            if i[k] in name:
                total += temp.get(i[k])
        answer.append(total)
        
    return answer