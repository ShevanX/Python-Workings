
for i in range(3):
    for x in range(1, 10):
        print(x, end=' ')
    print()

#Rectangle
rows = int(input("Enter the number or rows: "))
col = int(input("Enter the number or columns: "))
sym = input("Enter a symbol: ")

for x in range(rows):
    for y in range(col):
        print(sym, end=" ")
    print()

