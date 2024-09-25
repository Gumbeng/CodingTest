N = int(input())
arr =[[0] * 100 for v in range(100)] # 도화지의 범위 초기화 100 * 100
for v in range(N): # 입력 받은 도화지 개수만큼 돈다.
    y, x = map(int, input().split()) # 왼쪽,아래 x,y좌표를 받아준다.
    for i in range(x, x + 10): # 세로를 돈다
        for k in range(y, y + 10): # 가로를 돈다
            arr[i][k] = 1 # 해당 범위 값을 0에서 1로 바꿔준다
result = 0 # 넓이를 출력할 변수
for k in range(100): # 전체 도화지를 돈다
    result += arr[k].count(1) # 1의 개수만 세어준다
print(result)