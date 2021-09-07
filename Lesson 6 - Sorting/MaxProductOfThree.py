A=[-3, 1, 2, -2, 5, 6]
arr= [-5,5,-5,4]
import itertools

result_of_algorithm={
                    "correctness":100,
                    "performance":0,
                    "overall":44,
                    "time complexity": "O(N^3)"
                    }
def solution(A):
    combs=[]

    for pivot_element in A:
        to_comb=A[A.index(pivot_element):]

        for comb in itertools.combinations(to_comb, 3):
           mul_comb= comb[0] * comb[1] * comb[2]
           combs.append(mul_comb) 

    return max(combs)

solution(A)

def solution(A):
    A.sort()
    N=len(A)

    P1 = A[N-1] * A[0] * A[1]
    P2 = A[N-1] * A[N-2] * A[N-3]

    return max(P1,P2)

    