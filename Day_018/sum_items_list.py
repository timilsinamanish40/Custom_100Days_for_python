# def sum_finder(lst):
#     total = 0
#     for item in lst:
#         total += item 
#     return total



def sum_finder(lst):
    return sum(lst)


numbers = [1, 2, 3, 4, 5]
result = sum_finder(numbers)
print("Sum of all elements:", result)