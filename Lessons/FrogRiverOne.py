# A small frog wants to get to the other side of a river. The frog is initially located on one bank of the river (position 0) 
# and wants to get to the opposite bank (position X+1). Leaves fall from a tree onto the surface of the river.

# You are given an array A consisting of N integers representing the falling leaves. 
# A[K] represents the position where one leaf falls at time K, measured in seconds.

# Function that, given a non-empty array A consisting of N integers and integer X, returns the earliest time when the frog can jump to the other side of the river.

def solution(X,A):
    if list(range(1,X+1)) == list(set(A))[:X]:
        a = set()
        i = 0
        while len(a) != len(list(set(A))[:X+1]):
            i += 1
            a = set(A[:i])
        print(i-1)
    else:
        return -1

X = 1
A = [1]
solution(X, A)






































a = set()
i = X
while len(a) != len(set(A)):
    i += 1
    a = set(A[:i])
i-1
