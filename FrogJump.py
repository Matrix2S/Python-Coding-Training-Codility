def solution(X,Y,Z):
    if (Y - X)%D == 0:
        return (Y - X)//D
    else:
        return ((Y - X)//D)+1



X = 10
Y = 85
D = 30
solution(X,Y,D)


