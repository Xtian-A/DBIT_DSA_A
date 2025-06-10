##Q5. Count character frequencies in a string "data structures and algorithms" using a dictionary.
from collections import defaultdict  # Optional, but makes it cleaner

def count_char_frequencies(text):
    # Initialize a dictionary to store frequencies
    freq = {}
    
    # Iterate through each character in the string
    for char in text:
        # Skip spaces if needed (uncomment next line to ignore spaces)
        # if char == ' ':
        #     continue
        
        # Update the frequency count
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    
    return freq

# Example usage
text = "data structures and algorithms"
frequency_dict = count_char_frequencies(text)

# Print the frequencies sorted alphabetically
print("Character frequencies:")
for char, count in sorted(frequency_dict.items()):
    print(f"'{char}': {count}")