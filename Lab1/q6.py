# question 6: Write a program that finds the maximum length substring 
# without repeating characters from a given input string.

s = input("Enter a string: ") # Take a string input from the user.

max_length = 0       # Length of the longest substring
longest_sub = ""     # The longest substring without repeating characters

# Determine the longest substring that contains no repeated characters.

for i in range(len(s)):
    temp_sub = ""                # Temporary substring starting at index i
    for j in range(i, len(s)):
        if s[j] not in temp_sub:
            temp_sub += s[j]     # Add character if not already in substring
        else:
            break                # Stop when a repeated character is found

    # Update max_length and longest_sub if a longer substring is found
    if len(temp_sub) > max_length:
        max_length = len(temp_sub)
        longest_sub = temp_sub

print("Longest substring without repeating characters:", longest_sub) # Print: The longest substring
