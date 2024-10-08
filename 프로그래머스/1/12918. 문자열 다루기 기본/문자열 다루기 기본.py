def solution(s):
    if len(s) == 4 or len(s) == 6:
        answer = True
        arr = list(s)
        number = [0,1,2,3,4,5,6,7,8,9]
        num_cnt = 0
        for i in arr:
            if i in str(number):
                num_cnt += 1
        return True if num_cnt == len(arr) else False
    else:
        return False