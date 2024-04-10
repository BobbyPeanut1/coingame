import random
print("Welcome to the game!")

print(" Welcome to the game! \n call Heads or Tails: ")

player_input = input()
coin_flip = random.choice(["Heads", "Tails"])

if player_input == coin_flip:
    print("You won!")
else:
    print(f"Sorry it was {coin_flip}")