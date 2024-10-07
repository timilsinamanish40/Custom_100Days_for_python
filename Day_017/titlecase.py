s = input("Enter the string : ")

l = []
for word in s.split():
    l.append(word[0].upper() + word[1:].lower())
print(" ".join(l))
