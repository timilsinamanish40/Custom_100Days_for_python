def add_word(list_words, new_words):
    return ' '.join(list_words + new_words).capitalize() + '.'


list_words = input("Enter a list of words: ").split()
new_words = input("Enter new words: ").split()
# convert the list to a sentence
sentence = add_word(list_words, new_words)
print("Converted sentence:", sentence)
