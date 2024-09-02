def solution(arr):
    answer = 0
    total = 0
    for a in arr:
        total = total+a
    answer = total/len(arr)
    return answer