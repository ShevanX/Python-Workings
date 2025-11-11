def main():
    weight = input("Enter your weight in kg or lbs (no spaces): ")
    conv = input("gram(g)\npounds(lbs)\nkilograms(kg)\nWhat do u want it converted to ?: ")
    if weight[-2:] == "kg":
        digit = float(weight[:-2])
        result = convkg(digit, conv)
    elif weight[-3:] == "lbs":
        digit = float(weight[:-3])
        result = convlbs(digit, conv)

    if conv == "g":
        print(f"The converted value is {result} g")
    elif conv == "lbs":
        print(f"The converted value is {result} lbs")
    else:
        print(f"The converted value is {result} kg")


def convkg(digit, conv):
    if conv == "g":
        converted = digit * 1000
    else:
        converted = digit * 2.20462

    return round(converted, 2)

def convlbs(digit, conv):
    if conv == "g":
        converted = digit * 453.592
    else:
        converted =  digit * 0.453592

    return round(converted, 2)

main()

