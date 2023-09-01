A = [1,2,3,4,5,6]
K = 3

def solution(N,K):
    for j in range(K):
        a = A[-1]
        for i in range(1,len(A)):
            A[-i] = A[-i-1]
        A[0] = a
    return A
