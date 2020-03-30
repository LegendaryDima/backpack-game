players = []

for profile in range(2):
    players.append({
        "name": "",
        "score": 0,
        "backpack": []
    })
    
    players[profile]["name"] = input("Enter name for player " + str(profile + 1) + ": ")
    print("Enter four items to put in your backpack.")
    for item in range(4):
        backpack_item = input("Item name: ")
        players[profile]["backpack"].append(backpack_item)
    print(players[profile]["backpack"])

game_on = True

while game_on:
    for i in range(2):
        player_choice = input(players[i]["name"] + ", Guess an item from the other backpack: ")
        other_player = players[(i+1) % 2]
        if player_choice in other_player["backpack"]:
            print('You guessed an item from the other backpack!')
            players[i]["score"] += 1
            if players[i]["score"] == 4:
                print('You won! :)')
                game_on = False
                break
        else:
            print('You did not guess an item from the other backpack. :( ')
    
    if game_on == True:
        play_again = input('Do you want to continue playing? Type YES or NO: ')
        if play_again == 'NO':
            game_on = False

for player in players:
    print(player["name"] + " score: " + str(player["score"]))