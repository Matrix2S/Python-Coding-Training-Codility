# A non-empty array A consisting of N integers is given. Array A represents numbers on a tape.
# Any integer P, such that 0 < P < N, splits this tape into two non-empty parts: A[0], A[1], ..., A[P − 1] and A[P], A[P + 1], ..., A[N − 1].
# The difference between the two parts is the absolute difference between the sum of the first part and the sum of the second part.

# Function that, given a non-empty array A of N integers, returns the minimal difference that can be achieved.

def solution(A):
    p = []
    for P in range(len(A)-1):
        p.append(abs(sum(A[:P+1]) - sum(A[P+1:])))
    return min(p)

A = [3,1,2,4,3]
solution(A)


