def are_anagrams(str1, str2):
    
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Check if the sorted characters of both strings are the same
    return sorted(str1) == sorted(str2)


str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")
print("The stings are anagrams is :: ", are_anagrams(str1, str2)) 
