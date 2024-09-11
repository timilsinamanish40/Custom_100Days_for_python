def intersection(list1, list2):
    final_list = set(list1) & set(list2)
    return list(final_list)
   # The above lines of code  can be also written as : return list(set(list1) & set(list2))

list1 =  [1, 2, 3, 4]
list2 =  [3, 4, 5, 6]

print(intersection(list1, list2)) 
