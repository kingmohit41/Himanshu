def capitalize_words(sentence):
    words = sentence.split()
    capitalized_words = [word.capitalize() for word in words]
    return ' '.join(capitalized_words)

def reverse_string(input_string):
    return input_string[::-1]

def count_vowels(input_string):
    vowels = "aeiouAEIOU"
    vowel_count = sum(1 for char in input_string if char in vowels)
    return vowel_count