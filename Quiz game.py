questions = ("What is the smallest country in the world by land area?",
             "What element does “O” represent on the periodic table?",
             "Who was the first president of the United States?",
             "In the movie The Lion King, what kind of animal is Timon?",
             "What is the value of π (pi) rounded to two decimal places?")

options = (("A.Monaco", "B.Vatican City", "C.Nauru"),
           ("A.Oxygen", "B.Osmium", "C.Gold"),
           ("A.Thomas Jefferson", "B.Abraham Lincoln ", "C.George Washington"),
           ("A.Meerkat", "B.Warthog", "C.Lion"),
           ("A.3.12", "B.3.14", "C.3.16"))

answers = ("B","A","C","A","B")
guesses = []

score = 0
qNum = 0

for q in questions:
    for i in range(len(q)):
        print("-", end="")
    print(f"\n{q}")
    for o in options[qNum]:
        print(o)
    guess = input("Enter your answer: ").upper()
    guesses.append(guess)
    qNum += 1

for i in range(len(answers)):
    if guesses[i] == answers[i]:
        score += 1

feedback = ""
if score < 3:
    feedback = "Improve More!!!"
else:
    feedback = "WellDone!!!"
print(f"\nYour final score is {score}/5. {feedback}")