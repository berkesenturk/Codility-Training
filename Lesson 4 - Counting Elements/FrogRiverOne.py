# X, A = 5, [1,3,1,4,2,3, 5, 4]
X, A = 5, [1,3,1,6,4,2,3,4]

def solution(X, A):
    uni=[]
    result=[]
    x_sum= X * (X+1)/2
    for i in A:

        if (i not in uni) and (i <= X):
            uni.append(i)
            
            if (x_sum == sum(uni)):

                result.append(A.index(i))
                return result[0]

    return -1
    

solution(X, A)

# stackover

def solution(X, A):
    i = 0
    dict_temp = {}
    while i < len(A):

        dict_temp[A[i]] = i
        if len(dict_temp) == X:
            return i
        i += 1
    return -1
solution(X, A)
