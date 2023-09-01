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