def find_longest_word(string):
    words = string.split()
    longest_word = max(words , key = len)

    return longest_word

string =  input("Enter a string: ")
print("The longest word is: ",find_longest_word(string))