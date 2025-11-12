def main():
    principle = 0
    rate = 0
    time = 0

    while principle <= 0:
        principle = float(input("What's your principle amount: "))
        if principle <= 0:
            print("A principle cannot be 0 or negative")

    while rate <= 0:
        rate = float(input("What's your rate: "))
        if rate <= 0:
            print("A rate cannot be 0 or negative")

    while time <= 0:
        time = float(input("For how long: "))
        if time <= 0:
            print("A time(years) cannot be 0 or negative")

    ratio = input("How do you like to pay (monthly/annual/quarterly/bi-weekly/weekly): ").lower()

    fAmount = calCompInt(principle, (rate/100), time, ratio)
    interest = fAmount - principle

    print(f"\nThe {ratio} compound interest is {interest:,.2f}\n& the total amount you have to pay is {fAmount:,.2f}")

def calCompInt(p, r, t, n):

    total = 0
    if n == "monthly":
        total = p*((1 + (r/12))**(12*t))
    elif n == "annual":
        total = p*((1 + (r/1))**(t))
    elif n == "quarterly":
        total = p*((1 + (r/4))**(4*t))
    elif n == "bi-weekly":
        total = p*((1 + (r/26))**(26*t))
    elif n == "weekly":
        total = p*((1 + (r/52))**(52*t))

    return total

main()

