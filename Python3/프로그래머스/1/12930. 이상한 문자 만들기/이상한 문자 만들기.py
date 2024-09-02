def solution(s):
    answer = ''
    words = s.split(" ")
    # print(words)
    for i in range(0,len(words)):
        for j in range(0, len(words[i])):
            if j%2 == 0:
                answer += words[i][j].upper()
            else :
                answer += words[i][j].lower()
        answer += " "
    return answer[:-1]