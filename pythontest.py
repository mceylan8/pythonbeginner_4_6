import random

print("-----------------------------------")
print("Welcome to ROCK, PAPER, SCISSORS!")
print("We'll play 3 rounds.")
print("Whoever has more points wins!")
print("\t[r] - rock\n\t[p] - paper\n\t[s] - scissors")
print("-----------------------------------")

choices = ["r", "p", "s"]
player_score = 0
computer_score = 0

for round_num in range(1, 4):
    print(f"\n--- Round {round_num} ---")

    computer_choice = random.choice(choices)

    while True:
        player_choice = input("Your choice (r/p/s): ")
        if player_choice in choices:
            break
        print("❌ Invalid input! Please enter 'r', 'p' or 's'.")

    print(f"Computer chose: {computer_choice}")

    if player_choice == computer_choice:
        print("It's a draw!")
    elif (player_choice == "r" and computer_choice == "s") or \
         (player_choice == "p" and computer_choice == "r") or \
         (player_choice == "s" and computer_choice == "p"):
        print("🎉 You win this round!")
        player_score += 1
    else:
        print("💻 The computer wins this round!")
        computer_score += 1

# Final result
print("\n==============================")
print("🎯 Game Over – Final Score:")
print(f"You: {player_score} point(s)")
print(f"Computer: {computer_score} point(s)")

if player_score > computer_score:
    print("🏆 Congratulations! You win the game!")
elif player_score < computer_score:
    print("😔 The computer wins the game.")
else:
    print("🤝 It's a tie!")
