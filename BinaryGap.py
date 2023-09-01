import re


def solution(N):
    B = format(N, "b")
    x = re.finditer("(?<=1)0+(?=1)", B)
    A = []
    for i in x:
        A.append(i.group())
    for i in range(len(A)):
        A[i] = len(A[i])

    if len(A) == 0:
        return 0
    else :
        return max(A)

N = 1041
solution(N)