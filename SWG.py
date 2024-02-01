import random

options = ["Snake", "Water", "Gun"]

player_name = input("Enter your name: ")

player_score = 0
computer_score = 0
round_count = 0

game_start = True

while game_start:
    computer_choice = random.choice(options)

    player_choice = input("Choose Snake, Water, or Gun: ").capitalize()

    round_count += 1

    print(f"\nRound {round_count}: {player_name} chose {player_choice}, Computer chose {computer_choice}")

    if player_choice == computer_choice:
        print("It's a tie! Next round.\n")
        continue

    if (
        (player_choice == "Snake" and computer_choice == "Water") or
        (player_choice == "Water" and computer_choice == "Gun") or
        (player_choice == "Gun" and computer_choice == "Snake")
    ):
        player_score += 1
        print(f"{player_name} wins this round!\n")
    else:
        computer_score += 1
        print("Computer wins this round!\n")

    print(f"Scores - {player_name}: {player_score}, Computer: {computer_score}\n")

    if round_count >= 6:
        game_start = False

print("Game Over!")
print(f"Final Scores - {player_name}: {player_score}, Computer: {computer_score}")

if player_score > computer_score:
    print(f"{player_name} is the overall winner!")
elif player_score < computer_score:
    print("Computer is the overall winner!")
else:
    print("It's a tie!")
