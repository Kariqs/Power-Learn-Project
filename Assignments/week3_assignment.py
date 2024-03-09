def calculate_price(price,discount_percent):
    if discount_percent >=20:
        return price - ((discount_percent/100)*price)
    else:
        return price


entered_price = int(input("Enter original price:"))
entered_discount=int(input("Enter discount percentage:"))

final_price = calculate_price(entered_price,entered_discount)

if final_price == entered_price:
    print("No discount given. The price is therefore",final_price)
else:
    print("Final price after discount is",final_price)   
    