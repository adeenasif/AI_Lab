# question 5: Create a function that:

def functName (text):   
    count = {}  # Returns a dictionary containing:
    # Total characters, Total vowels, Total consonants

    total = 0
    vCount = 0
    cCount = 0

    for i in text:
        if (i in 'aeiouAEIOU'):
            vCount += 1
            total += 1
        elif (i.isalpha()):
            cCount += 1
            total += 1
        else:
            total += 1
    
    count['Total Characters'] = total
    count['Vowel Count'] = vCount
    count['Consonant Count'] = cCount

    return count

text = input("Enter a string: ") # Accepts a string
count = {}
count = functName(text)
print("Total Characters: ", count['Total Characters'] , ", Vowel Count:", count['Vowel Count'], ", Consonant Count:", count['Consonant Count'])
