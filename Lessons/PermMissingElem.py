# An array A consisting of N different integers is given. 
# The array contains integers in the range [1..(N + 1)], which means that exactly one element is missing.

# Function that, given an array A, returns the value of the missing element.

def solution(A):
    i = 1
    while i in A:
        i += 1
    return i

A = [1,2,3,5]
solution(A)






