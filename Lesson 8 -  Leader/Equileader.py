A=[4,3,4,4,4,2]

def retrieve_dominant(slice):
    count={}
    for i in set(slice):
        count[f"{i}"] = slice.count(i)

    return count


def solution(A):
    total_equileader=0
    
    for S in range(1, len(A)):
        first_slice=A[:S]        
        second_slice=A[S:]

        first_dom = retrieve_dominant(first_slice)
        second_dom = retrieve_dominant(second_slice)
        
        if (max(first_dom) == max(second_dom)) and (len(first_slice) == 1 or len(second_slice) == 1):
            total_equileader +=1

        elif (max(first_dom) == max(second_dom)) and (list(first_dom.values()) != [1]*len(first_slice) and list(second_dom.values()) != [1]*len(second_slice)):
            # print(first_dom, second_dom)  
            
            total_equileader += 1
        
        else:
            continue
    return total_equileader

from collections import defaultdict

solution(A)

def solution(A): 
    marker_l = defaultdict(lambda : 0)
    marker_r = defaultdict(lambda : 0)
    
    for i in range(len(A)): 
        marker_r[ A[i] ] += 1
    
    n_equi_leader = 0
    leader = A[0]

    for i in range(len(A)):
        marker_r[A[i]] -= 1
        marker_l[A[i]] += 1
        

        if i == 0 or marker_l[ leader ] < marker_l[ A[i] ]:
            leader = A[i]
            
        # burada iki elementli listeden kurtuluyo
        if (i+1) // 2 < marker_l[leader] and (len(A) - (i+1)) // 2 < marker_r[leader]:
            print("marker_l: ", (i+1) // 2, marker_l[leader], 
                  "marker_r: ", ((len(A) - (i+1)) // 2), marker_r[leader])
            n_equi_leader += 1

    return n_equi_leader

solution(A)