A=[4,3,2,1,5] #2 kalcak
B=[0,1,0,0,0]



def solution(A, B):
    ds=[]
    count=0

    for i in range(0, len(B)):

        if (B[i] == 1):
        
            ds.append(A[i])
        
        else:
        
            while (len(ds) != 0):
                
                if (ds[-1] > A[i]):
                    count += 1
                    break

                elif (ds[-1] < A[i]):
                    ds.pop()
                    count += 1 

    return len(A) - count

                
solution(A, B)