def solution(N):
    # write your code in Python 3.6
    # in binary
    binary_arg = format(N,"b")

    splitted_binary = [int(char) for char in binary_arg]

    # collect 0's for each squence
    # each count to be collected in here
    counts=[]

    counter=0
    for char in splitted_binary:
        if char == 0:
            counter += 1

        else:
            
            counts.append(counter)
            counter=0
    return max(counts)