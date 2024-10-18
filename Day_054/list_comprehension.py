def main():
    numbers = [1,2,3,4,5,6,7,8,9,10]

    # 1. Filtering even numbers

    even_numbers = [num for num in numbers if num %2 == 0 ]

    # 2. Transforming values : Squaring each numbers
    squares = [x**2 for x in numbers]

    # 3. Combining filtering and transformation: squares of even numbers
    even_squares = [x**2 for x in numbers if x % 2 == 0]

    # 4. Using if-else statements
    transformed = ['positive' if num > 0 else 'negative' for num in numbers]

    # 5. Flattening a list of lists
    list_of_lists = [[1, 2], [3, 4]]
    flattened_list = [element for sublist in list_of_lists for element in sublist]
    
   # Print all results
    print(f'Even Numbers: {even_numbers}')
    print(f'Squares: {squares}')
    print(f'Even Squares: {even_squares}')
    print(f'Transformed: {transformed}')
    print(f'Flattened List: {flattened_list}')

# Run the main function
main()