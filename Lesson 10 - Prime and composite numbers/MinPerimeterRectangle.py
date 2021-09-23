# area of some rectangle

# N=30
# A,B=0,0
# perimeter= 2*(A+B)

# min perimeter when A*B=N meets

N=30
"""
Task Score
50%
Correctness
100%
Performance
0%
"""
def solution(N):
    
    minimum_perimeter = float('inf')
    
    for i in range(N+1):
        for j in range(N+1):
            if i*j == N:
                minimum_perimeter = min(minimum_perimeter,
                                        2*(i+j))

                print("i: ", i , "j: ", j, minimum_perimeter)
            
    return minimum_perimeter

solution(N)

import math
# https://www.stumblingrobot.com/2015/10/01/prove-that-the-square-has-the-smallest-perimeter-of-all-rectangles-of-a-given-area/
def solution(N):
    minimum_perimeter = float('inf')
    i =round(math.sqrt(N))
    while i>0:
        if (N % i == 0) and (i<= math.sqrt(N)):
            if (2*(i+N/i) < minimum_perimeter):
                minimum_perimeter = 2*(i+N/i)
        
        i -= 1
    return int(minimum_perimeter)