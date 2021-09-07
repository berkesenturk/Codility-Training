A = [9, 3, 9, 3, 9, 9,7]


def solution(A):


    count=0

    unique_A=[]

    for item in A:
        if item not in unique_A:
            unique_A.append(item)

    for number in unique_A:
        for item in A:
            
            if (item == number):
                count += 1

    if (count % 2 != 0):
        return number

def solution(A):     
    if len(A) == 1:
         return A[0]
    # sorting list
    A = sorted(A)

    # values evenly increasing in for loop
    for i in range(0 , len (A) , 2):
        # checking even val equal to len of list
        if i+1 == len(A):
            return A[i]

        # checking if val of ith item equals to next item. if it isn't, ith item is the odd val 
        if A[i] != A[i+1]:
            return A[i]

def solution(A):
   result = 0
   for number in A:
     result ^= number
   return result