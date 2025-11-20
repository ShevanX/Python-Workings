

doubles = [x for x in range(1,11)]
fruits = ["apple", "strawberry", "mango", "orange", "grapes"]
fruits = [i.capitalize() for i in fruits]
num = [1, -4, 3, -5, 7]
pos = [abs(x) for x in num]
grades = [65, 78, 82, 93, 88, 12, 34, 77, 100]
passing = [x for x in grades if x  >= 75]
passing.sort()

print(passing)
