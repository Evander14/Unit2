#Text Monster Game

#Dungeon map-variables/lists
dungeon = [
    ['reward','dungeon master', 'sword', 'sword', 'stairs down'], 
    ['magic stones', 'monster', 'stairs down', 'sword', 'stairs up'], 
    ['empty', 'sword', 'stairs up', 'monster', 'empty']
    ]
#player info
dead = False
inventory = []
current_room = 0
current_floor = 2
location = dungeon[current_floor][current_room]

#game loop
while True:

    #update location
    location = dungeon[current_floor][current_room]

    #describe where we are to the user
    if location == 'empty':
        print("You are in an empty room.")
    elif location == 'sword':
        print("You walk in and find a shiny sword.")
    elif location == 'stairs up':
        print('You see stairs leading up')
    elif location == 'monster':
        print("You see a scary monster")
    elif location == 'empty':
        print("You find another empty room")
    elif location =='magic stones':
        print("You find magic stones in a box on the floor")
    elif location == 'stairs down':
        print("You reach stairs that lead back down")
    elif location == 'prize':
        print("You find the dungeon's prize")
    elif location == 'dungeon master':
        print("The dungeon master won't let you leave with the prize so easily")
    elif location == 'reward':
        print("Past the beasts lair you see the dungeons reward. Type 'escape' to leave the dungeon with the reward.")
    
        
        
    
    #player choices
    player_choices = input("What would you like to do? (left, right, up, down, grab, fight, inventory) ")
    print(player_choices)

    if player_choices == 'right':
        current_room += 1
        if current_room == 5:
            print("You have reached a dead-end")
            current_room = 4
        #must fight monsters or player dies
        elif location == 'monster' or location == 'dungeon master':
            print("You attempted to move past the monster without fighting it and failed.")
            dead = True
            break 
    elif player_choices == 'left':
        current_room -= 1
        if current_room == -1:
            print("You have reached a dead-end")
            current_room = 0
        #must fight monsters or player dies
        elif location == 'monster' or location == 'dungeon master':
            print("You attempted to move past the monster without fighting it and failed.")
            dead = True
            break
    elif player_choices == 'up':
        if location == 'stairs up' :
            current_floor -= 1
            print("You walk up the stairs")
        else:
            print("How do you expect to go up without stairs?")
    elif player_choices == 'down':
        if location == 'stairs down':
            current_floor += 1
            print("You walk down the stairs")
        else:
            print("Go down where??")
    elif player_choices == 'grab':
        if location == 'sword' or location == 'magic stones': #grabs items
            inventory.append(location)
            dungeon[current_floor][current_room] = 'empty'
        elif location == 'monster' or location == 'dungeon master':
            print("You tried to grab THAT????")
            print("You go to pick up the abnormally large  monster for some reason.")
            dead = True
            break
        else:
            print("There is nothing to grab here.")
    elif player_choices == 'inventory':
        print("You have:")
        print(' '.join(inventory)) # joins every item with a space
    elif player_choices == 'fight':
        if location == 'monster':
            if 'sword' in inventory:
                print("Despite the monster catching you off guard, you defeated it. Good job.")
                dungeon[current_floor][current_room] = 'empty'
                inventory.remove('sword')
                print("However, your sword was lost in the battle.")
            else:
                print("You tried to fight the monster without a sword and lost.")
                dead = True
                break
        if location == 'dungeon master':
            if 'sword' and 'magic stones' in inventory:
                print("You valiantly fought and killed the beast, the dungeon's reward is now yours.")
                dungeon[current_floor][current_room] = 'empty'
                inventory.remove('sword')
                inventory.remove('magic stones')
                print('Unfortunately you sword was ripped to shreds by the beast and the magic stones were drained of their energy and have returned to dust.')
            else:
                print("Despite fighting valiantly, the beast cannot be killed unless you have his weakness.")
                dead = True
                break
    elif player_choices == 'escape':
        if location == 'reward':
            print("After fighting for your life you have reached the top of the dungeon.")
            break
        else:
            print("In order to escape you must reached the top of the dungeon.")

#Determine win loss
if dead == True:
    print("YOU DIED.")
else:
    print("You have escaped into freedom with the dungeon's reward.")