def solution(array, commands):
    answer = []
    temp = []
    for i in commands:
        temp.clear()
        for j in range(i[0],i[1]+1):
            temp.append(array[j-1])
        temp.sort()
        answer.append(temp[i[2]-1])
    return answer