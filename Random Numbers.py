import random

low = 1
high = 100
answer = random.randint(low, high)

print("--------Number Guessing Games--------")

is_running = True

correct = False
while is_running:
    guess = int(input("Enter your guess: "))
    diff = guess - answer
    if guess == answer:
        correct = True
        is_running = False
        break

    elif diff >= 30:
        print("Too High. Try again")
    elif diff >= 20:
        print("A little high")
    elif diff >= 10:
        print("A bit high. You're close")
    elif diff > 0:
        if diff <= 5:
            print("You're VERY close and high! Just a tiny bit off.")
        else:
            print("You're close and high! Just a bit off.")


    elif diff <= -30:
        print("Too Low")
    elif diff <= -20:
        print("A little Low")
    elif diff <= -10:
        print("A bit Low. You're close")
    elif diff < 0:
        if diff >= -5:
            print("You're VERY close and low! Just a tiny bit off.")
        else:
            print("You're close and low! Just a bit off.")

if correct:
    print("Correct. Well Done")



