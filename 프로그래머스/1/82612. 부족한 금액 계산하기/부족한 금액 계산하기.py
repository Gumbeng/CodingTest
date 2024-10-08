def solution(price, money, count):
    temp = sum([price*i for i in range(count, 0, -1)])
    return temp - money if temp > money else 0