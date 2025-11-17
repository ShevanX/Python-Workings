foods = []
prices = []
total = 0

while True:
    food = input("Enter the food name (q to quit): ").lower()
    if food == "q":
        break
    else:
        price = float(input(f"Whats the price of {food}: "))
        foods.append(food)
        prices.append(price)

print("These are the food you have ordered")
for i in range(len(foods)):
    print(f"{foods[i]:<} - ${prices[i]:>}")

for i in range(len(prices)):
    total += prices[i]

print(f"\nYour total is ${total}")

