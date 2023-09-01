def solution(A):
    p = []
    for P in range(len(A)-1):
        p.append(abs(sum(A[:P+1]) - sum(A[P+1:])))
    return min(p)

A = [3,1,2,4,3]
solution(A)


