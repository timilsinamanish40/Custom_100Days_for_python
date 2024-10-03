def find_max(lst):
    if len(lst) == 0:
        return None  # Handling empty list

    max_element = lst[0]  # Assuming the first element is the largest in the list
    for item in lst:
        if item > max_element:
            max_element = item
    return max_element


lst = [10, 20, 4, 45, 99, 89, 599]
result = find_max(lst)
print("Maximum element:", result)
