A=[3,2,-6,4,0]

def solution(A):
    # 0 ≤ P ≤ Q < N
    # The sum of a slice (P, Q) is the total of A[P] + A[P+1] + ... + A[Q]

    maximum= -float('inf')

    if len(A) == 1:
        return sum(A)

    pivot_index=0
    init=0



    while pivot_index < len(A):

        if pivot_index == init:

            slice=A[pivot_index : init]
            
            if slice!=[]:
                
                
                maximum = max(maximum, slice[0])

                # print(slice, maximum)

            init +=1
        
        else:
    
            slice=A[pivot_index : init]
    
            if slice!=[]:
            
                maximum = max(maximum, sum(slice))

                # print(slice, maximum)
            init +=1

        if init == len(A) + 1:
            pivot_index += 1
            init=0

    return maximum
        
solution(A)

# another

def solution(A):
    max_ending = max_slice = -float('inf')
    for a in A:

        max_ending = max(a, max_ending +a)
        max_slice = max(max_slice, max_ending)
        print("a: ", a, "max_ending: ", max_ending, "max_slice: ",max_slice) 
    return max_slice