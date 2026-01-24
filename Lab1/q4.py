# question 4 : Create a function that: Takes purchase amount as parameter

def applyDiscount (amount):
    if (amount < 1000):
        discount = amount*5/100  # 5% if amount < 1000
    elif (amount < 5000):
        discount = amount*10/100 # 10% if amount  5000
    else:
        discount = amount*15/100 # 15% otherwise

    return (amount-discount)  # Returns the net payable amount

# Call the function and display the result

amount1 = applyDiscount(500)
print ("1. Amount (500) < 1000, net payable amount: ", amount1)

amount2 = applyDiscount(4000)
print ("2. Amount (4000) < 5000, net payable amount: ", amount2)

amount3 = applyDiscount(6000)
print ("3. Amount (6000) > 5000, net payable amount: ", amount3)
