# Function to convert a sentence into a word list and reverse it
def reverse_sentence(sentence):
    # Split the sentence into words
    words = sentence.split()

    # Reverse the word list
    reversed_words = words[::-1]

    return reversed_words


# Input sentence
input_sentence = "Studying at university of the people is one of the best thing ever."

# Call the function
reversed_word_list = reverse_sentence(input_sentence)

# Print the reversed word list
print(reversed_word_list)
