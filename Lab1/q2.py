#question 2

text = input("Enter a string: ")  # Takes a string as input

print("First Character: ", text[0])    # First character
print("Last Character: ", text[len(text)-1])    # Last character
print("Length of Character: ", len(text))    # Length of string

count = 0

# String repeated twice
print("Repeated Twice String: ", *text * 2)   

# Counts and prints the number of characters excluding spaces
for x in text:
    if (x != ' '):
        count += 1
    
print(count)
