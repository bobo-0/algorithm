def solution(s):
    answer = []
    numbers = s.split(" ")
    for i in numbers:
        answer.append(int(i))
    answer = sorted(answer)
    #answer.sort()
    
    return str(answer[0]) +" "+str(answer[-1])