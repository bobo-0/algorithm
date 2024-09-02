def solution(n):
    answer = list(str(n))
    answer = reversed(answer)
    answer = [int(x) for x in answer]
    return answer