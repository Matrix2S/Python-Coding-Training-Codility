# Function that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

def solution(A):
    A = set([x for x in A if x > 0])
    
    if len(A) == 0:
        return 1

    i = min(A)
    if i != 1:
        return 1
    else:
        while i in A:
            i = i+1
        return i

A = [1,3,6,4,1]



