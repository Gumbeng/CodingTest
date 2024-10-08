def solution(arr1, arr2):
    answer = []
    for a,b in zip(arr1, arr2):
        temp = []
        for i in range(len(arr1[0])):
            temp.append(a[i]+b[i])
        answer.append(temp)
    return answer