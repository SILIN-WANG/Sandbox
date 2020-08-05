num_of_items = int(input("Number of items: "))

total_price = 0
for i in range(1, num_of_items+1):
    the_price_of_item = float(input("Price of items: "))
    total_price += the_price_of_item

if total_price < 0:
    print("Invalid number of items!")

elif total_price >= 100:
   total_price *= 0.9
   print("Total price for %.2f"%num_of_items, "items is", total_price)

else:
    print("Total price for %.2f"%num_of_items, "items is", total_price)

