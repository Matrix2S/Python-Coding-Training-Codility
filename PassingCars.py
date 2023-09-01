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