len = int(input()) #input은 str 값으로 받아지니까 int로 형변환
str = input()
result = 0
for i in range(len):
    result+=int(str[i]) #string 하나씩 result에 저장
print(result)