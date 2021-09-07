A = [3, 8, 9, 7, 6]
K = 3
"""
0 --> 1
1 --> 2 
2 --> 3 
3 --> 4 
4 --> 0 
"""

def solution(A, K=1):
    N = len(A)
    
    if len(A):
        if (0 <= N <= 100 or 0 <= K <= 100) and (max(A) != 1001 and min(A) != -1001):
    
            turn = 1
            while turn <= K:
                B =  [None] * N

                for index in range(N):

                    if (index != (N - 1)):
                        B[index+1] = A[index]

                    elif (index == (N - 1)):
                        B[0] = A[N - 1]
                # print("turn", turn,": ", B)
                A = B
                turn +=1
    else:
        return []

    return A