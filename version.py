def count_vowels_and_consonants(string):
    vowels = 'aeiouAEIOU'
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    
    vowel_count = 0
    consonant_count = 0
    
    for char in string:
        if char in vowels:
            vowel_count += 1
        elif char in consonants:
            consonant_count += 1
            
    return {'vowels': vowel_count, 'consonants': consonant_count}

# Example usage:
input_string = "Hello World"
counts = count_vowels_and_consonants(input_string)
print(counts)