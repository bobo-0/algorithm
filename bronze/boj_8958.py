n = int(input())
for i in range(n):
    b = input()
    s = list(b)
    total = 0
    score = 1
    for i in s:
        if i =="O":
            total += score
            score +=1
        else:
            score = 1
    print(total)
