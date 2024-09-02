def solution(s):
    answer = True
    stack =[]
    for i in s:
        if len(stack)==0:
            stack.append(i)
            continue
        if stack[-1]=='(' and stack[-1]!=i:
            stack.pop()
        else:
            stack.append(i)
        
    if len(stack)==0:
        answer = True
    else:
        answer = False
    return answer