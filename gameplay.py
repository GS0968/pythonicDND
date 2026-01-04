import sys
import json
from project import Character
from project import Room
from project import Monster

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
            new_name = input("Enter the name for your Character")
            player = Character(new_name,,,"")#add the starting values
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
        "rooms": [room.todict() for room in rooms]
    }
    with open(filename, "w") as file:
        json.dump(game_state, file, indent=4)

def make_character(name,classtype):
    details=json.load(newgamefile) #newgamefile is a json with preset characters types and rooms
    classtypes=
