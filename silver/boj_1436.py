"""
n = int(input())
shom = []
for i in range(666,100000000):
    if '666' in str(i):
        shom.append(i)
print(shom[n-1])
"""

n = int(input())
cnt = 0
shom_num=666
while True:
    if '666' in str(shom_num):
        cnt+=1
    if cnt == n:
        print(shom_num)
        break
    shom_num +=1