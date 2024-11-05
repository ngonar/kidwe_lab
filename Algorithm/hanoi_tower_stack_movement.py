tower_a = [3,2,1]
tower_b = []
tower_c = []

max_move = 7
win = False

user_movement = 0

#Print all towers
print(tower_a)
print(tower_b)
print(tower_c)

while not win:

    user_movement += 1

    user_input = input("\n\nWhat's your next move, format [Tower origin] [Tower destination]\n")
    command = user_input.split()


    #Origin
    if command[0].lower() == "a":
        origin_tower = tower_a
    elif command[0].lower() == "b":
        origin_tower = tower_b
    elif command[0].lower() == "c":
        origin_tower = tower_c

    #Destination
    if command[1].lower() == "a":
        destination_tower = tower_a
    elif command[1].lower() == "b":
        destination_tower = tower_b
    elif command[1].lower() == "c":
        destination_tower = tower_c

    #Move the disc
    disc = origin_tower[len(origin_tower)-1]
    origin_tower.pop()
    destination_tower.append(disc)

    #Print all towers
    print("==== Towers ====")
    print(tower_a)
    print(tower_b)
    print(tower_c)
    print("================")

