def solution(A,B):
    answer = 0
    print(A)
    print(B)
    A.sort()
    B.sort(reverse=True)
    for i in range(0,len(A)):
        answer += A[i]*B[i]

    return answer