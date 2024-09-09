def vowel_check(string):
    no_of_vowel = 0
    vowel_letters = "aeiouAEIOU"

    for char in string :
        if char in vowel_letters:
            no_of_vowel += 1
        
    return no_of_vowel

string = input ("Enter a string: ")

print("The vowel in given string is : ",vowel_check(string))
