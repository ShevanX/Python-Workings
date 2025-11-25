#Lists
# Cars = ["Toyota", "Honda", "Mazda", "Benz"]
#
# Cars.append("BMW")
#
# Cars[2] = "Porsche"
# Cars.insert(0, "Bentley")
# Cars.sort()
# Cars.reverse()
#
# for x in Cars:
#     print(x)


#Sets
# Cars = {"Toyota", "Honda", "Mazda", "Benz"}
#
# Cars.add("BMW")
# Cars.pop()
#
# for car in Cars:
#     print(car, end=" ")

#Tuples

# Cars = ("Toyota", "Honda", "Mazda", "Benz", "Toyota")
# print(Cars.index("Benz"))
# print(Cars.count("Toyota"))

# fruits =     ["apple", "orange", "banana", "mango", "grapes"]
# vegetables = ["carrot", "onion", "beet", "potato", "cabbage"]
# bakery =     ["bagel", "donut", "sliced bread", "naan", "tortilla"]
#
# foods = [fruits, vegetables, bakery]
#
# for food in foods:
#     for i in food:
#         print(i, end=" ")
#     print()

numPad = ((1, 2, 3),
          (4, 5, 6),
          (7, 8, 9),
          ("*", 0, "#"))

for row in numPad:
    for num in row:
        print(num, end=" ")
    print()



