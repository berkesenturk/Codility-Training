H = [8, 8, 5, 7, 9, 8, 7, 4, 8]

def stone_wall(H):
    num_blocks=0
    S=[]
    last=0

    for i in range(len(H)):
        # inc trend
        if (H[i] > last):
            last = H[i]
            num_blocks += 1
            S.append(H[i])
        
        # dec trend

        elif (H[i] < last):
            while(len(S) > 0 and H[i] < S[-1]):
                S.pop()

            if (len(S) == 0 or H[i] != S[-1]):
                num_blocks += 1
                S.append(H[i])

            last = H[i]

    return num_blocks

stone_wall(H)