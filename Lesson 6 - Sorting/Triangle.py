# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
A=[10, 2, 5, 1, 8, 20]
def solution(A):
    # if sorted
    # A[Q] + A[R] > A[P]
    # A[P] + A[R] > A[Q]
    # only needed to check
    # A[P] + A[Q] > A[R]
    A.sort()

    if (len(A) < 3):
        return 0
    
    for i in range(len(A)-2):
        if (A[i] > A[i+2] - A[i+1]):
            return 1
    return 0