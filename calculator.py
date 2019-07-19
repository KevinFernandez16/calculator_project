import definitions
# The line above will let you separate your concerns by defining functions your calculator might use in a separate file.

print("Welcome to the Python Calculator\n")
print("Hello Welcome to our restaurant!\n" "This is a calculator that helps calculate how much you need to tip.")
meal_price = input("What is the price for your meal today?: $")
meal_price = float(meal_price)
tip1 = float(0.05)
tip2 = float(0.10)
tip3 = float(0.15)
tip4 = float(0.20)
tip5 = float(0.30)
if meal_price <= float(25.00) or meal_price <float(50.00):
    print("You owe a 5% tip which comes to the amount of $" + str(meal_price*tip1))
elif meal_price >= float(50.00) and meal_price <=float(100.00):
    print("You owe a 10% tip which comes to the amount of $" + str(meal_price*tip2))
elif meal_price >= float(100.00) and meal_price <=float(150.00):
    print("You owe a 15% tip which comes to the amount of $" + str(meal_price*tip3))
elif meal_price >= float(150.00) and meal_price <=float(200.00):
    print("You owe a 20% tip which comes to the amount of $" + str(meal_price*tip4))
elif meal_price >= float(200.00):
    print("You owe a 30% tip which comes to the amount of $" + str(meal_price*tip5))
