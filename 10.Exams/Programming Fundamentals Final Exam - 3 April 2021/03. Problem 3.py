data = input()
players = {}

while not data == "Results":
    data = data.split(":")
    command = data[0]
    if command == "Add":
        person_name = data[1]
        health = data[2]
        energy = data[3]
        if person_name not in players:
            players[person_name] = {}

    elif command == "Attack":
        pass
    elif command == "Delete":
        pass


    data = input()