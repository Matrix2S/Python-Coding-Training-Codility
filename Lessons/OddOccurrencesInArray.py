# A non-empty array A consisting of N integers is given.
# The array contains an odd number of elements, and each element of the array can be paired
# with another element that has the same value, except for one element that is left unpaired.

# Function that, given an array A consisting of N integers fulfilling the above conditions, returns the value of the unpaired element.



def solution(A):
    a = list(set(A))
    b = []
    for i in range(len(a)):
        b.append(A.count(a[i]))
    return a[b.index(1)]

A = [9,3,9,3,9,7,9]
solution(A)

 # SECOND SOLUTION
 
def solutoin(A):
    a = list(set(A))
    i = 0
    while A.count(a[i]) !=1:
        i +=1
    return a[i]
