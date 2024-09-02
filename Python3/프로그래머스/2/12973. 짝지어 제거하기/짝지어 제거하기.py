def solution(s):
    stack = []
    for i in range(0,len(s)):
        if len(stack) ==0 : 
            stack.append(s[i])
            continue
        if stack[-1]==s[i]:
            stack.pop()
        else:
            stack.append(s[i])
    if len(stack)==0:
        return 1
    else:
        return 0
