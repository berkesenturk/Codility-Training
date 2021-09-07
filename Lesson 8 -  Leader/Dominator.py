A=[3,4,3,2,3,-1,3,3]
from collections import defaultdict
def solution(A):
    # most freq
    # count more than half of len A
    elements_and_indices = defaultdict(list)

    if len(A) == 0:
        return -1

    else:
        for i in range(len(A)):

            elements_and_indices[f"{A[i]}"].append(i)

        longest = max(len(item) for item in elements_and_indices.values()) 

        if (longest > len(A) / 2):

            return [item for item in elements_and_indices.values() if len(item) == longest][0][0] 
        # if no dominator or empty list
        else:
            return -1

solution(A)