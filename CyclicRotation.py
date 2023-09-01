# An array A consisting of N integers is given. Rotation of the array means that each element
# is shifted right by one index, and the last element of the array is moved to the first place.

# Function that, given an array A consisting of N integers and an integer K, returns the array A rotated K times.

A = [1,2,3,4,5,6]
K = 3

def solution(N,K):
    for j in range(K):
        a = A[-1]
        for i in range(1,len(A)):
            A[-i] = A[-i-1]
        A[0] = a
    return A
