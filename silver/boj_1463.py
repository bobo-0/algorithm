n = int(input())
dp = [0]*(n+1)
for i in range(2,n+1):
    dp[i] = dp[i-1]+1
    if i%3 == 0:
        dp[i] = min(dp[i],dp[i//3]+1)
    if i%2 == 0:
        dp[i] = min(dp[i],dp[i//2]+1)
print(dp[n])


####이러게 풀면 안됨####
"""
n = int(input())
count = 0
while n>1:
    if n%3 !=0 and n%2!=0:
        print("A")
        n=n-1
        count+=1
    if n%3 ==0:
        print("B")
        n = n//3
        count+=1
    if n%2 ==0:
        print("C")
        n = n//2
        count+=1
print(count)
"""
