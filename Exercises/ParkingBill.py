def solution(E,L):
    h = int(L[0:2]) - int(E[0:2])
    m = int(L[3:5]) - int(E[3:5])

    if m > 0:
        h = h+1

    if h == 0:
        return 2
    elif h == 1:
        return 2+3
    elif h > 1:
        return 2+3+(h-1)*4

E = "10:43" 
L = "15:42" 
solution(E,L)


