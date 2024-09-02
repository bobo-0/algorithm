def solution(n, words):
    words_list=[]
    answer = [0,0]
    words_list.append(words[0])
    for i in range(1,len(words)):
        if words_list[i-1][-1] != words[i][0]:
            answer[0]=(i%n)+1
            answer[1]=(i//n)+1
            break
        elif words[i] in words_list:
            answer[0]=(i%n)+1
            answer[1]=(i//n)+1
            break
        else:
            words_list.append(words[i])
            
    

    return answer