a = []
for i in range(3):
    a.append(int(input()))
temp = list(set(a)) # 중복확인을 위한 set
if sum(a) == 180: # 3개의 각이 180인지 아닌지
    if len(temp) == 1:
        if temp[0] == 60:
            print("Equilateral")
    else:
        print("Isosceles" if len(temp) != 3 and len(temp) > 1 else "Scalene")
else:
    print("Error")
