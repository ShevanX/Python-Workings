import random

# ● ┌ ┐ ─ └ │ ┘

sides ={1:("┌─────────┐",
           "│         │",
           "│    ●    │",
           "│         │",
           "└─────────┘"),
        2:("┌─────────┐",
           "│         │",
           "│   ● ●   │",
           "│         │",
           "└─────────┘"),
        3:("┌─────────┐",
           "│         │",
           "│  ● ● ●  │",
           "│         │",
           "└─────────┘"),
        4:("┌─────────┐",
           "│  ●   ●  │",
           "│         │",
           "│  ●   ●  │",
           "└─────────┘"),
        5:("┌─────────┐",
           "│  ●   ●  │",
           "│    ●    │",
           "│  ●   ●  │",
           "└─────────┘"),
        6:("┌─────────┐",
           "│  ● ● ●  │",
           "│         │",
           "│  ● ● ●  │",
           "└─────────┘")
        }

dice = []
total = 0
num_of_dice = int(input("How many dice: "))

for i in range(num_of_dice):
    dice.append(random.randint(1, 6))

# for i in range(num_of_dice):
#     for j in sides.get(dice[i]):
#         print(j)

for line in range(5):
    for die in dice:
        print(sides.get(die)[line],end=" ")
    print()

for i in range(len(dice)):
    total += dice[i]

print(f"Total : {total}")
