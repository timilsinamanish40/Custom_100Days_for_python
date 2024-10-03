def reverse_words(sentence):
    # Split the sentence into words
    words = sentence.split()
    
    # Reverse the list of words
    reversed_words = words[::-1]
    
    # Join the reversed list back into a sentence
    reversed_sentence = ' '.join(reversed_words)
    
    return reversed_sentence

# Example usage
sentence = "Hello World this is Day 28"
reversed_sentence = reverse_words(sentence)
print(reversed_sentence)
