
pi = 3.1415926535

def pow(x,y):
    return x ** y

def sqrt(x, y=1e-10):
    if x < 0:
        raise ValueError("Cannot take square root of a negative number")

    guess = x
    while True:
        new_guess = 0.5 * (guess + x / guess)
        if abs(new_guess - guess) < y:
            return new_guess
        guess = new_guess

def circumference(radius):
    c = 2 * pi * radius
    return round(c,2)

def area(radius):
    a = pow((pi*radius),2)
    return round(a,2)
