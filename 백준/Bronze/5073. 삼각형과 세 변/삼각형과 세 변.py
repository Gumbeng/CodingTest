while True:
    n = list(map(int, input().split()))  # 세 변 입력받음
    if n == [0, 0, 0]:  # 0 0 0 입력 시 종료
        break
    
    n.sort()  # 세 변을 오름차순으로 정렬 (n[2]가 가장 긴 변)
    
    # 삼각형의 조건: 가장 긴 변이 나머지 두 변의 합보다 작아야 한다
    if n[2] >= n[0] + n[1]:
        print("Invalid")
    else:
        if n[0] == n[1] == n[2]:  # 세 변이 모두 같은 경우
            print("Equilateral")
        elif n[0] == n[1] or n[1] == n[2]:  # 두 변만 같은 경우
            print("Isosceles")
        else:  # 세 변이 모두 다른 경우
            print("Scalene")