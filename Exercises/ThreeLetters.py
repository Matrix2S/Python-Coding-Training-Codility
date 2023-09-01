# Write a function solution that, given two integers A and B, returns a string containing exactly A letters 'a' and exactly B letters 'b'
# with no three consecutive letters being the same (in other words, neither "aaa" nor "bbb" may occur in the returned string).

def solution(A,B):
    
    k = ""

    if B > A:
        C = B
        B = A
        A = C

    while (A,B) != (0,0):
        if A%2 == 0 and A == 2*B:
            k += B*"aab"
            A -= 2*B
            B -= 1*B
        elif A == B:
            k += A*"ab"
            A -= A*1
            B -= B*1
        elif A == 2 and B == 0:
            k += "aa"
            A -= 2
        elif A == 1 and B == 0:
            k += "a"
            A -= 1
        else:
            k += "aab"
            A -= 2
            B -= 1

    import re

    try:
        C
        k=re.sub("a", "c", k)
        k=re.sub("b", "a", k)
        k=re.sub("c", "b", k)
    except NameError:
        pass
    
    return k

solution(3,5)
