import random

opt = ("rock", "paper", "scissors")
player = None
computer = random.choice(opt)
comp_score = 0
player_score = 0
round = 0

for i in range(5):
    round += 1
    print(f"\n-----Round {round}-----\n")
    player = input("Enter the input: ").lower()
    print(f"Player: {player:>3}")
    print(f"Computer: {computer:>3}")
    if player == "rock" and computer == "paper":
        comp_score += 1
    elif player == "paper" and computer == "scissors":
        comp_score += 1
    elif player == "scissors" and computer == "rock":
        comp_score += 1
    elif player == computer:
        pass
    else:
        player_score += 1

print(f"\nThe Computer won with {comp_score}/5") if comp_score > player_score \
    else print(f"\nThe player won with {player_score}/5")
if comp_score == player_score:
    print("\nits a tie")


