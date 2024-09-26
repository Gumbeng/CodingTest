N = int(input())
for i in range(2, N+1):
    while N % i == 0: # 같은 소인수로 나눌 수 있을 때가지 반복
        print(i)
        N //= i
    if N == 1: # N이 1이되면 더이상 나눌 필요가 없음
        break