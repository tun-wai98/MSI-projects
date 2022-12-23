price = int(input("Enter the price: "))
quantity = int(input("Enter the quantity: "))
amount = price * quantity

if amount > 1000 :
    print("You can get 10% discount!")
    discount = amount * 10/100
    amount = amount - discount
    print("Your payable amount is", amount)

elif amount == 1000 :
    print("Your payable amount is", amount)

else :
    print("Your payable amount is", amount)
