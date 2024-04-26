def longest_substring(s: str) -> int:
    if not s:
        return 0
    
    # Initialize a dictionary to store the index of the last occurrence of each character
    char_index = {}
    max_length = 0
    start = 0
    
    for i, char in enumerate(s):
        # If the character is already in the dictionary and its index is after the start of the current substring
        if char in char_index and char_index[char] >= start:
            # Update the start index of the substring
            start = char_index[char] + 1
        # Update the index of the current character
        char_index[char] = i
        # Update the maximum length of the substring
        max_length = max(max_length, i - start + 1)
    
    return max_length
 #program completed
 