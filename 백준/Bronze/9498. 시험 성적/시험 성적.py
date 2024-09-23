result = int(input())

if 0 <= result <= 100:
    if 90 <= result:
        print("A")
    elif 80 <= result:
        print("B")
    elif 70 <= result:
        print("C")
    elif 60 <= result:
        print("D")
    else:
        print("F")