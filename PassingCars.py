# A non-empty array A consisting of N integers is given. The consecutive elements of array A represent consecutive cars on a road.
# Array A contains only 0s and/or 1s:

        # - 0 represents a car traveling east,
        # - 1 represents a car traveling west.


# Function that, given a non-empty array A of N integers, returns the number of pairs of passing cars.

A = [1, 1, 1, 1, 1]

def solution(A):
    try:
        ind = A.index(0,0)
    except ValueError:
        return 0


    a=0
    while a <= 1000000000:
        a += len([x for x in A[ind:] if x==1])
        try:
            ind = A.index(0, ind+1)
        except ValueError:
            break

    if a <= 1000000000:
        return a
    else:
        return -1

A = [0, 1, 0, 1, 1]
