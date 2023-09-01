# A small frog wants to get to the other side of the road. The frog is currently located at position X
# and wants to get to a position greater than or equal to Y. The small frog always jumps a fixed distance, D.

# Function that, given three integers X, Y and D, returns the minimal number of jumps from position X to a position equal to or greater than Y.

def solution(X,Y,Z):
    if (Y - X)%D == 0:
        return (Y - X)//D
    else:
        return ((Y - X)//D)+1



X = 10
Y = 85
D = 30
solution(X,Y,D)


