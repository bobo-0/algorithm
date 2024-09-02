def solution(s):
    answer = True
    p_count = 0
    y_count = 0
    for i in s:
        if i =="P" or i=="p":
            p_count+=1
        elif i =="Y" or i=="y":
            y_count+=1
    if p_count == y_count:
        answer = True
    else:
        answer = False
    # print('Hello Python')

    return answer