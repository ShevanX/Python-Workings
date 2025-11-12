userName = ""
isFine = False
while not isFine:
    name = input("Enter your userName: ").strip()
    if len(name) > 12 or " " in name or not name.isalpha():
        isFine = False
        print("Please enter a valid username")
    else:
        isFine = True
        userName = name


print(f"Your new userName is {userName}")


