A=[2, 3, 1, 5]
# berke
def solution(A):

    if (A != []):

        sorted_arr = sorted(A)
        
        uniq = []
        for element in sorted_arr:
            if element not in uniq:
                uniq.append(element)
        # checking if only one element is missing
        if (len(uniq) <= len(sorted_arr)):
            whole_array= [None] * (len(sorted_arr)+1)

            for n in range(len(sorted_arr)+1):
                whole_array[n] = n+1

            res =  [item for item in whole_array if item not in sorted_arr][0]   
            
            return res

# stackover :D

def solution(A):

    n = len(A)+1
    result = n * (n + 1)//2

    return result - sum(A)

res = solution(A)
print(res)