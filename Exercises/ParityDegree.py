def solution(N):
    i = 0
    while N % 2 == 0:
        i += 1
        N = N/2
    return i

A = 2**13
solution(A)



