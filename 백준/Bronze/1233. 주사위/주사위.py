s1, s2, s3 = map(int, input().split())
result = [0] * (s1 + s2 + s3 + 1)  # 가능한 합의 범위를 고려한 리스트 생성

# 주사위 눈의 합을 구하고 빈도수를 저장
for i in range(1, s1 + 1):
    for b in range(1, s2 + 1):
        for c in range(1, s3 + 1):
            result[i + b + c] += 1  # 각 합에 해당하는 빈도 증가

# 가장 빈도가 높은 합을 찾음
max_frequency = max(result)  # 최대 빈도 찾기
most_frequent_sum = result.index(max_frequency)  # 최대 빈도가 처음 나오는 합을 찾음

print(most_frequent_sum)
