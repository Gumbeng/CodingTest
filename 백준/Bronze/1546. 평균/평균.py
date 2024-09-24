N = int(input())
maxNum = 0;
score = list(map(int, input().split()))
print(sum(score) / max(score) * 100 / N)