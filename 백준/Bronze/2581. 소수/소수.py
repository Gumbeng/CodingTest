M = int(input())
N = int(input())
arr = []
for num in range(M, N+1): # M 이상 N 이하의 수
    count = 0 # 나눠지는 수 있으면 카운트
    if num > 1: # 2 이상의 수 중 소수 찾기
        for i in range(2, num): # 2 부터 num 나눠지는 수
            if num % i == 0: # 나눠진다면
                count += 1 # 소수가 아님 : 카운트
                break # 종료
        if count == 0: # 나눠지는 수가 없었다면 소수
            arr.append(num) # 소수를 배열에 넣어준다
if len(arr) > 0:
    print(sum(arr))
    print(min(arr))
else:
    print(-1)