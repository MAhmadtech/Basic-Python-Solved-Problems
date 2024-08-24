

# Write a program that will take user input of cost price and selling price and determines whether its a loss or a profit
cost_price = int(input("Enter your cost price: "))
seller_price = int(input("Enter your seller price:"))
profit = seller_price - cost_price
loss = cost_price - seller_price
if seller_price > cost_price:
    print(f"You are in profit of {profit} rupees")
elif seller_price < cost_price:
    print(f"You are in the loss {loss} rupess"  )
else:
    seller_price == cost_price
    print("You are not in loss or not in profit")            