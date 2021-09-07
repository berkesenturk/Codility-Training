# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


S = "(()(())())"
S_err =  "())"
S_a="(()(())()))))))"

def solution(S):


    count = 0

    for par in range(0, len(S)):
        if (len(S) != par):
            
            # if 1 append
            if ( S[par] == '(' ):
                count += 1

            # if -1 pop
            elif ( S[par] == ')' ):
                count -= 1
            
            if (count < 0):
                return 0
        
    if  (count == 0):

        return 1
        
    else:
        return 0


                    
solution(S)