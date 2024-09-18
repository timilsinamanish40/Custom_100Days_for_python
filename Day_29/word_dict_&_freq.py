def word_frequency(text):
    # Convert text to lowercase
    text = text.lower()
    
    # Remove punctuation manually
    cleaned_text = ""
    for char in text:
        if char.isalpha() or char.isspace():
            cleaned_text += char
    
    # Split the text into words
    words = cleaned_text.split()
    
    # Create an empty dictionary to store word frequencies
    frequency = {}
    
    # Count the frequency of each word
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    
    return frequency

# Example usage
text = "This is a sample text. This text is a simple example text."
frequencies = word_frequency(text)
print(frequencies)
