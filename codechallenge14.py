game_list = []

while True:
    game = input("Enter the name of a video game (or type 'quit' to stop): ")

    if game.lower() == "quit":
        print("\nYou have exited the game entry program.")
        break
    else:
        game_list.append(game)
        print(f"'{game}' has been added to your game library.")

print("\nYour game library includes:")
for g in game_list:
    print("-", g)
