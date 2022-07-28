def knapsack(weights, profit, capacity, i=0):
    memo={}
    def max_profit(i, capacity):
        key = (i, capacity)
        if key in memo:
            return  memo[key]
        elif i == len(weights):
            memo[key] = 0
        elif ( weights[i] > capacity ):
            return max_profit( (i+1), capacity)
        else:
            option1 = max_profit( (i+1),  capacity)
            option2= profit[i] + max_profit((i+1),  capacity- weights[i])
            memo[key] = max(option1, option2)
        return memo[key]
    return max_profit(0, capacity)
    #
    # def recurse(idx, remaining):
    #     key = (idx, remaining)
    #     if key in memo:
    #         return memo[key]
    #     elif idx == len(weights):
    #         memo[key] = 0
    #     elif weights[idx] > remaining:
    #         memo[key] = recurse(idx + 1, remaining)
    #     else:
    #         memo[key] = max(recurse(idx + 1, remaining),
    #                         profits[idx] + recurse(idx + 1, remaining - weights[idx]))
    #     return memo[key]
    #
    # return recurse(0, capacity)

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
print(knapsack(weights, profit, capacity, i))
