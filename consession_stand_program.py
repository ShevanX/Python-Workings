menu = {"Popcorn":3.00,
          "Hot dog":4.00,
          "Giant pretzel":2.50,
          "Pizza":5.75,
          "Burger":7.49,
          "Coke":2.50,
          "Nachos":4.25,
          "Sprite":2.50}

cart = []
total = 0

print("Hi Welcome to the Concession Store\n\nPlease pick an item out of the menu")
for item,price in menu.items():
    print(f"{item:<15} : ${price:>5.2f}")
print()
while True:
    items = input("Enter the items (Press e to stop): ").capitalize()
    if items == "E":
        break
    elif menu.get(items) is not None:
        cart.append(items)
        total += menu.get(items)
    else:
        print(f"{items} is not available in the menu")

print()
print(f"Your total will be ${total:.2f}")



