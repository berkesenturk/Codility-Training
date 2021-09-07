A=[23171, 21011, 21123, 21366, 21013, 21367]


# % 66 performance, O(N**2)
def solution(A):
    # profit when A[i] < A[i+1]

    # return max profit for nth day buy nth day sold
    buy_day=0

    profits=[]

    if len(A) == 0:
        return 0

    for buy_day in range(len(A)):

        for day in range(buy_day+1, len(A)):
            if A[day] > A[buy_day]:
                profits.append(A[day] - A[buy_day]) 

            # if no profit
            # return 0

    if len(profits) == 0 :
        return 0
    else:
        return max(profits)


solution(A)

# % 100 perf, O(N)

def solution(A):
    minimum, maxprofit = float('inf'), 0
    for value in A:
        minimum = min(value, minimum)
        maxprofit = max(value - minimum, maxprofit)
    return maxprofit

solution(A)