##Stack 사용
from pythonds.basic.stack import Stack
import sys
S = Stack()
n = int(input())
for i in range(0,n):
    S.push(int(sys.stdin.readline().strip()))
length = S.pop()
cnt = 1
for i in range(0,S.size()):
    if S.peek() > length : 
        length = S.pop()
        cnt+=1
    else : 
        S.pop()
print(cnt)

### list 와 for문 거꾸로 사용
import sys
n = int(input())
s = [int(sys.stdin.readline().strip()) for i in range(0,n)]
length = s[-1]
cnt = 1
for i in range(len(s)-1,-1,-1):
    if s[i] > length : 
        length = s[i]
        cnt+=1
print(cnt)

### list에서 pop() 사용
import sys
n = int(input())
s = [int(sys.stdin.readline().strip()) for i in range(0,n)]
length = s.pop()
cnt = 1
for _ in range(n-1):
    if s[-1] > length : 
        length = s.pop()
        cnt+=1
    else:
        s.pop()
    
print(cnt)
