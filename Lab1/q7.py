# question 7: Write a Python function that returns the numbers:
# that are repeated more than once in a given list.

List = []
n = int(input("Enter the total count of numbers you want in list: "))      # Creates a List of numbers entered by the user

for i in range(n):                              # Loop to take input
    val = int(input(f"Enter Value {i + 1}: "))       
    List.append(val)                            # Add value to List

def find_repeated_numbers(numbers):
    repeated = []  # List to store numbers that appear more than once
    for i in numbers:
        count = 0
        
        for j in numbers: # Count how many times i appears in the list
            if i == j:
                count += 1
        
        # If count > 1 and i not already in repeated, add it
        if count > 1 and i not in repeated:
            repeated.append(i)
    return repeated

nums = [1, 2, 3, 2, 4, 5, 1, 6, 3, 3]
result = find_repeated_numbers(nums)
print("Numbers repeated more than once:", result) # Return the repeated numbers only once (no duplicates in output)
