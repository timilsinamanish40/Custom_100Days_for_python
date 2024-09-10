def fibonacci(limit):
    a,b = 0,1;
    fibonacci_list = []

    while a <= limit:
        fibonacci_list.append(a)
        a,b = b, a+b;
        #a = b
        #b = a+b
        #tuple unpacking

    return fibonacci_list


limit = int(input("Enter the limit: "))
lst =   fibonacci(limit)
print("Fibonacci Sequence: ",lst)