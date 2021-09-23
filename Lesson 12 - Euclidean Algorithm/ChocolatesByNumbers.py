N=10
M=4
# 0, 4, 8, 2, 6, 0
# 0, 3, 6, 9, 2, 5, 8, 1, 4, 7, 0
# 0, 2, 4, 6, 8, 0
# 0, 4, 8, 2, 6, 0
# 0, 5, 0
# 0, 6, 2, 8, 4, 0
# 0, 7, 4, 1, 8, 5, 2, 9, 6, 3, 0

def solution(N, M):
    
    dict_iterations={}
    i=0
    while True:
        i += M
        # print(dict_iterations)

        if i > N:

            i = i % N 
            try:
                if dict_iterations[f"{i}"] == True:
                    return len(dict_iterations)
            except:
                dict_iterations.update( {f"{i}": True} )
            
        elif i == N and len(dict_iterations) == 0:
            return len(dict_iterations)+1

        else:
            
            dict_iterations.update( {f"{i}": True} )

# % 100 solution

def gcd(a, b):
    # Get the greatest common divisor
    if (a % b == 0):
        return b
    else:
        return gcd(b, a % b)

def solution(N, M):

    lcm = N * M / gcd(N, M) # Least common multiple
    return int(lcm / M)