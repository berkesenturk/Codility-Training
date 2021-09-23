A=[-5,-3,-1,0,3,6]
# with caterpillar method
def solution(A):
    distinct=set()
    for item in A:
        # if abs(item) not in distinct:
        distinct.add(abs(item))

    return len(distinct)
        