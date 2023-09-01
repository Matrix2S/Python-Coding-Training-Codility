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