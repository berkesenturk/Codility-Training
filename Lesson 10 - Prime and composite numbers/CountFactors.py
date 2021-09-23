N=24

def solution(N):
    factor = 1
    count=0

    while factor != N+1:
        # print(factor)
        if (N%factor) == 0:

            count+=1
            factor += 1
        else:

            factor += 1
            continue

    return count

solution(N)


def solution(N):
    factor = 1
    count=0

    while factor * factor < N:
        # print(factor)
        if (N%factor) == 0:

            count+=2
        factor += 1
        
    if (factor * factor == N):


        factor += 1
        
    return count

solution(N)

def solution(N):
    count = 0
    for i in range(1, N+1):
        if i*i > N:
            break
        if N % i == 0:
            if i*i < N:
                count += 2
            elif i*i == N:
                count += 1
    return count

