def calculate_average(filename):
    try:
        with open(filename, 'r') as file:
            numbers = file.readlines()
            
            # Convert each line into a number (strip to remove newlines)
            numbers = [float(num.strip()) for num in numbers]
            
            # Calculate the average
            average = sum(numbers) / len(numbers) if numbers else 0
            
            return average
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
        return None
    except ValueError:
        print("Error: The file contains non-numeric data.")
        return None

## Example usage
# filename = 'numbers.txt'
# average = calculate_average(filename)
# if average is not None:
#     print(f"The average of the numbers in '{filename}' is: {average}")
