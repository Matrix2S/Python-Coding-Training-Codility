

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