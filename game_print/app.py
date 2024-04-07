import random

print(" Welcome to my game \n call a flipped coin Heads or Tails?")

coin_input = input()
flip_coin = random.choice(["Heads", "Tails"])

if coin_input == flip_coin:
    print("You won!")
else:
    print(f"Sorry it was {flip_coin}")