def remove_duplicates(input_list):
    return list(set(input_list))  # Convert list to a set to remove duplicates, then back to a list

# Example usage:
my_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = remove_duplicates(my_list)
print(unique_list)  # Output: [1, 2, 3, 4, 5]
