#question 1

dict = {}

dict['name'] = input("Enter Name:")  
dict['age'] = input("Enter Age:")    
dict['city'] = input("Enter City:")  

print('\n===== Created Dictionary ===== \n Dictionary Output: ', dict)
print("\n\nDisplaying Output: Name: ", dict['name'], ", Age:", dict ['age'], ", City:", dict ['city'])

# Check Eligibility criteria

if dict['age'] >= '18':                     
    print("Eligible For Vote")
else:
    print("Not Eligible For Vote")