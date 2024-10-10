def solution(cards1, cards2, goal):
    answer = []
    n = len(cards1)
    m = len(cards2)
    temp = []
    i,j = 0,0
    
    for a in goal:
        if i < n and cards1[i] == a:
            answer.append(a)
            i += 1
        if j < m and cards2[j] == a:
            answer.append(a)
            j += 1
        
    return "Yes" if answer == goal else "No"