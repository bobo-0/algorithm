import sys
from collections import Counter
n = int(sys.stdin.readline())
nums=[]
for _ in range(n):
    nums.append(int(sys.stdin.readline()))
#average
print(round(sum(nums)/n))

#median
nums.sort()
print(nums[int((n-1)/2)])

#max
count = Counter(nums).most_common(2)
if len(count)==1:
    print(count[0][0])
else:
    if count[0][1] == count[1][1]:
	    print(count[1][0])
    else:
	    print(count[0][0])

#range
print(nums[-1]-nums[0])