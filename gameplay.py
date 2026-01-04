import sys
import json
from classes import Character
from classes import Room
from classes import Monster

def start(): #not fully complete yet
    option=input("Do you want to start a new game or load a previous game?: ")
    option=option.strip().lower()
    
    match option:
        case "load":
            oldfile=input("Enter the loadfile name: ")
            try:
                return load_game(oldfile)
            except FileNotFoundError:
                sys.exit("Error: File Not Found")

        case "new" | "new game":
            newfile=input("Enter savefile name: ")
            new_name = input("Enter the name for your character: ")
            while True:
                classtype=input("Enter the class you want your hero to be: ")
                try:
                    player = make_char(new_name,classtype)#add the starting values
                    break
                except ValueError:
                    print("invalid character type")
            rooms = []
            save_game(newfile, player, rooms)
            return player, rooms

def load_game(filename):
    with open(filename, "r") as file:
        data = json.load(file)
    player = Character.from_dict(data["player"])
    rooms = [Room.from_dict(r) for r in data["rooms"]]
    return player, rooms

def save_game(filename,player,rooms):
    game_state = {
        "player": player.to_dict(),
        "rooms": [room.to_dict() for room in rooms]
    }
    with open(filename, "w") as file:
        json.dump(game_state, file, indent=4)

def make_char(name,classtype):
    with open("newgamefile", "r") as file:
        data=json.load(file)
        classes= #newgamefile is a json with preset characters types and rooms
    #classtypes(a list) gets all the class of the heros available
    #then search if the classtype given matches one of them in the list
    #if match assign to character if not give ValueError saying "not valid class"
