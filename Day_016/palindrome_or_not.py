string = input("Enter a String :")
# var[from this index : to before this index : every this step] string[::-1]
def is_palindorome(string):
    string = string.replace(" ","").lower()

    if string == string [::-1]:
        print(f'{string} is Palindrome')
    else:
        print(f'{string} is not Palindrome')

is_palindorome(string)
