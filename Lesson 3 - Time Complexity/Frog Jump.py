# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, Y, D):
    if X <= Y:
        if X == Y:
            return 0
            
        else:
            if ((Y-X) % D == 0):
                return int(((Y-X) / D))

            else:
            
                return int(((Y-X) / D) + 1)
            
res = solution(4,7, 2)
print(res)
