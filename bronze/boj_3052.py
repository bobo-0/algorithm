datas = [int(input()) for i in range(0,10)]
rest = [0 for i in range(0,42)]
count = 0
for i in datas:
    rest[i%42] +=1
for i in rest:
    if i != 0:
        count +=1
print(count)
