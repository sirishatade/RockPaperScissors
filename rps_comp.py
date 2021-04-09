from random import choice
"""
This program allows a user to play Rock Paper Scissors with the computer, best 2 out of 3

"""

print("...rock...")
print("...paper...")
print("...scissors...")

player_wins = 0
comp_wins = 0
while player_wins < 2 and comp_wins < 2:
	
	options = ["rock", "paper", "scissors"]
	computer = choice(options)
	player = input("Enter your choice: ").lower()

	if player == "quit" or player == "q":
		break

	print("Computer chose: " + computer)
	if player == computer:
		print("You tied!")
	elif player == "rock" and computer == "scissors":
		print("You win!")
		player_wins += 1
	elif player == "scissors" and computer == "paper":
		print("You win!")
		player_wins += 1
	elif player == "paper" and computer == "rock":
		print ("You win!")
		player_wins += 1
	else:
		print("Computer wins, sorry :(")
		comp_wins +=1

if comp_wins > player_wins:
	print("Comp won, sorry!")
elif comp_wins < player_wins:
	print("You won the game! great job!")
elif comp_wins == player_wins:
	print("It's a tie")
else:
	print("Goodbye!")