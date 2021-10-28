money_owned = input("How much money do I have? ")
amount_of_money = int (money_owned)
price_of_apple = input("How much does an apple cost? ")
apple_price = int (price_of_apple)
maximum = amount_of_money // apple_price
change = amount_of_money % apple_price
print(f"You can buy {maximum} apples and your change is {change} pesos.")