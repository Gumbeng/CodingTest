def solution(s):
    stack = []
    cnt = 0
    for i in range(len(s)):
        if s[i] == ")" and i == 0:
            return False
        else:
            if cnt == -1:
                return False
            if s[i] == "(":
                cnt += 1
            elif s[i] == ")":
                cnt -= 1
            stack.append(s[i])
    answer = True if stack.count(")") == stack.count("(") else False
    return answer