# You are given N counters, initially set to 0, and you have two possible operations on them:

        # - increase(X) − counter X is increased by 1,
        # - max counter − all counters are set to the maximum value of any counter.

# A non-empty array A of M integers is given. This array represents consecutive operations:

        # - if A[K] = X, such that 1 ≤ X ≤ N, then operation K is increase(X),
        # - if A[K] = N + 1 then operation K is max counter.


# Function that, given an integer N and a non-empty array A consisting of M integers, returns a sequence of integers representing the values of the counters.

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




