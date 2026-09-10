price=float(input("Enter the price of the item:"))
if(price>1000):
    discount=(25/100)*price
    final_amount=price-discount
    print("The final amount after 25% discount is:", final_amount)
else:
    discount=(10/100)*price
    final_amount=price-discount
    print("The final amount after 10% percent discount is:", final_amount)
    
    