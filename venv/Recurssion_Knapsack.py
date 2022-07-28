def max_profit(weights, profit, capacity, i=0):
    if i == len(weights):
        return 0
    elif ( weights[i] > capacity ):
        return max_profit(weights, profit, capacity, (i+1))
    else:
        option1 = max_profit(weights, profit, capacity, (i+1))
        option2= profit[i] + max_profit(weights, profit, capacity- weights[i], (i + 1))
    return max(option1, option2)

# test0 = {
#     'input' : {
#     'capacity': 165,
#     'weights' : [23, 31, 29, 44, 53, 38, 63, 85, 89, 82],
#     'profit' : [92, 57, 49, 68, 60, 43, 67, 84, 87, 72],
#     },
#     'output' : 309
# }

#
# max_profit(test0 ['input' ]['weights'], ['profit'], ['capacity'], i=0)

weights =  [23, 31, 29, 44, 53, 38, 63, 85, 89, 82]
profit = [92, 57, 49, 68, 60, 43, 67, 84, 87, 72]
capacity= 165
i =0
print(max_profit(weights, profit, capacity, i))
