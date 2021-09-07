S = "{[()()]}"
S_err = "([)()]"

def solution(S):
    c = {
        '{':+1,'[':+2,'(':+3,
        '}':-1,']':-2,')':-3
    }
    v=[]
    if (len(S))==0:
        return 1

    for i in range(0, len(S)):
            
            # if index is 0 and bracket is closing one
            if ( i == 0 and c[S[i]] < 0 ):
                return 0
            
            # if bracket is a closing one and vector list is empty which is not correct so, 0
            elif ( c[S[i]] < 0 and len(v) == 0 ):
                return 0
            
            # if bracket is a closing one and last item which added to the vector list is the opening bracket 
            elif ( c[S[i]] < 0 and c[S[i]] != -v[-1] ):
                return 0
            
            elif ( c[S[i]] < 0 ):
                v.pop()
            else:
                v.append(c[S[i]])

    if ( len(v) == 0 ):
        return 1
    else: 
        return 0



solution(S_err)