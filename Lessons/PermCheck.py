# A non-empty array A consisting of N integers is given.
# A permutation is a sequence containing each element from 1 to N once, and only once.

# Function that, given an array A, returns 1 if array A is a permutation and 0 if it is not.

def solution(A):
    a = 1
    while a in A:
        a = a + 1

    if a == len(A)+1:
        return 1
    else:
        return 0

A = [4,1,3,2]
solution(A)



### Discarded Solution ###
def solution(A):
    for i in A:
        if 0 < i < len(A)+1:
            continue
        else:
            break

    if A.index(i) == len(A)-1:
        return 1
    else:
        return -1

A = [4,1,3,2]
solution(A)
