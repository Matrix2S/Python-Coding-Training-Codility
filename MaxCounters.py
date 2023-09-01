def solution(N, A):
    counter = [0]*N
    for i in range(len(A)):
        if 1 <= A[i] <= N:
            counter[A[i]-1] += 1
        
        elif A[i] == N+1:
            counter = [max(counter)]*N
    return counter

A = [3,4,4,6,1,4,4]
N = 5




