def solution(X, Y):
    answer = ''
    
    x_value=[0,0,0,0,0,0,0,0,0,0]
    y_value=[0,0,0,0,0,0,0,0,0,0]
    
    for i in X:
        x_value[int(i)]+=1
    for i in Y:
        y_value[int(i)]+=1
    
    for i in range(9,-1,-1):
        answer += str(i)*min(x_value[i],y_value[i])
    if(len(answer)==0):
        return '-1'
    if(answer[0]=='0'):
        return '0'
    
    return answer