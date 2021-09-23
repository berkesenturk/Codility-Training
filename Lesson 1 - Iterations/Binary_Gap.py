def solution(N):
    # write your code in Python 3.6
    # in binary
    binary_arg = format(N,"b")

    splitted_binary = [int(char) for char in binary_arg]

    # collect 0's for each squence
    # each count to be collected in here
    counts=[]
    # count_max = float('inf')

    counter=0
    for char in range(len(splitted_binary)):
        
        if (char == len(splitted_binary)-1) and (splitted_binary[char] == 0):
            counter += 1
            counts.append(counter)

        elif (splitted_binary[char]) == 0:
            counter += 1

        elif (splitted_binary[char]) == 1:
            counts.append(counter)
            counter=0


    return max(counts)

print(solution(200))