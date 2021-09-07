# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
# P east 0
# Q west 1

import itertools
A = [0,1,0,1,1]

"""
1-- zeros = 1
2-- passing = 1
3-- zeros = 2
4-- passings = 3
5-- passing = 5
"""

# brutal
def solution(A):
    east_cars={}
    west_cars={}
    
    for index in range(0, len(A)):
    
        if A[index] == 0: 
            east_cars.update({index:A[index]})
            index += 1
    
        elif A[index] == 1: 
            west_cars.update({index:A[index]})
            index += 1

    list_east = list(east_cars.keys())
    list_west = list(west_cars.keys())

    product = list(itertools.product(list_east, list_west))
    
    final_product=[]

    for item in product:
        if item[0] <= item[1]:
          final_product.append(item)
    
    if len(final_product) > 1000000000:
        return -1 
    
    else:
        return len(final_product)


# efficient

def solution(A):
    car_east=0
    encountered_cars=0

    for i in A:
        if i == 0:
            car_east+=1
        
        elif i == 1:
            encountered_cars+=car_east

            continue
    if encountered_cars > 1000000000:
        return -1
    
    else:
        return encountered_cars
            
        

        