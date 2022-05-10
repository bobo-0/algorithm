hour, minutes = map(int,(input().split()))
if minutes < 45:
    minutes += 60-45
    hour -= 1
    if hour == -1:
        hour = 23
else : 
    minutes -=45
print(hour, minutes)