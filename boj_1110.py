n = int(input())
a = n//10
b = n%10
result = 0
cnt = 0
while True:
    result = a+b
    result = result%10 + b*10
    cnt +=1
    a = result//10
    b = result%10 
    if result == n:
        break
print(cnt)
