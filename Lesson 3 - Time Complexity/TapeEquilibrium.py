A=[3, 1, 2, 4, 3]


# berke O(n*n)
def solution(A):
    res=[]
    # first n
    for index in range(1,len(A)):

        L=A[:index]
        R=A[index:]
        l_sum = sum(L)
        r_sum = sum(R)
        print(L, R, "sum: ",abs(l_sum - r_sum))
        res.append(abs(l_sum - r_sum))
    # second n
    return min(res)
solution(A)

# stackoverflow :D
# O(n)
from itertools import accumulate

def solution(A):
    array_sum = sum(A)  # saving sum of all elements to have an O(n) complexity

    # accumulate returns accumulated sums
    # e.g. for input: [3, 1, 2, 4] it returns: [3, 4, 6, 10]
    # we are passing a copy of the array without the last element
    # including the last element doesn't make sense, becuase
    # accumulate[A][-1] == array_sum
    accumulated_list = accumulate(A[:-1])

    return min([abs(2*x - array_sum) for x in accumulated_list])