A = [4,1,1,4]
A_true= [4,1,3,2]

from math import perm
def solution(A):
    if A == [0]:
        return 1
    elif A == [1]:
        return 1

    # elif (len(A) * (len(A) +1))/2 == sum(A):
    #     return 1
    elif perm(len(A)) == math.prod(A):
        return 1
    else:
        return 0

solution(A)

