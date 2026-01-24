# question 3: Create a program that:

List = []
n = int(input("Enter the total count of numbers you want in list: "))      # Creates a List of numbers entered by the user

for i in range(n):                              # Loop to take input
    val = int(input(f"Enter Value {i + 1}: "))       
    List.append(val)                            # Add value to List

min = List[0]     # Assuming min value to be at index 0
max = List[0]     # Assuming Max value to be at index 0
sum = 0

for i in range(n):      # Display all elements
    print("Value ", i+1, ": ", List[i])                
    sum += List[i]           # Calculate the sum of elements
    if(min > List[i]):                                  
        min = List[i]        # Update min
    if (max < List[i]):  
        max = List[i]        # Update max

print("Sum: ", sum)
print("Minimum: ", min)
print("Maximum: ", max)

# Updates one element of the List based on user input

i = int(input(f"Enter index of the List to update (0-{n-1}): "))
updateVal = int(input("Enter Number: "))
List[i] = updateVal

print("Value Succesfully updated at List[",i,"]: ",List[i] )
