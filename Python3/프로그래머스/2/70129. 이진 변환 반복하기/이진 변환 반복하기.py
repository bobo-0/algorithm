def solution(s):    
    cnt_binary = 0
    cnt_zero = 0
    
    while 1:
        if s=='1':
            break
        cnt_binary +=1
        cnt_zero += s.count("0")
        s = s.replace("0", "")
        len_s = len(s)
        
        s = bin(len_s)[2:]
    return [cnt_binary,cnt_zero]