# A positive integer N is given. The goal is to find the highest power of 2 that divides N. 
# In other words, we have to find the maximum K for which N modulo 2^K is 0.

# Function that, given a positive integer N, returns the highest power of 2 that divides N.

def solution(N):
    i = 0
    while N % 2 == 0:
        i += 1
        N = N/2
    return i

A = 2**13
solution(A)



