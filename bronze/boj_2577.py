a = int(input())
b = int(input())
c = int(input())
nums = [0 for i in range(0,10)]
res = str(a*b*c)
for i in range(0, len(res)):
    nums[int(res[i])] +=1
for i in nums:
    print(i)
