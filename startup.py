import sys
import json
from entities import Character
from entities import Room
from entities import Monster

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
                classtype=input("Enter the class you want your hero to be [warrior | rouge | mage | paladin]: ")
                try:
                    health,power, sattack, type,ihealth,croom= make_char(classtype)
                    rooms=make_room()
                    monsters=make_monsters()
                    player=[new_name, health, power, sattack, type, ihealth, croom]
                    break
                except ValueError:
                    print("invalid character type")
            save_game(newfile, player, rooms, monsters)
            return player, rooms, monsters, newfile

def load_game(filename):
    with open(filename, "r") as file:
        data = json.load(file)
    
    player = data["character"]
    rooms = data["rooms"]
    monsters= data["monster"]
    return player, rooms, monsters, filename

def save_game(filename,player,rooms,monsters): #player, room, and mosnters are list
    game_state = {
        "rooms": rooms,
        "monster":monsters,
        "character": player
    }
    with open(filename, "w") as file:
        json.dump(game_state, file, indent=4)

def make_char(classtype):
    classtype=str(classtype)
    classtype=classtype.strip().lower()
    with open("newgamefile", "r") as file:
        data=json.load(file)
    charinfo=data["character"]
    match classtype:
        case "warrior":
            playerlistinfo=charinfo[1]
        case "rouge":
            playerlistinfo=charinfo[2]
        case "mage":
            playerlistinfo=charinfo[3]
        case "paladin":
            playerlistinfo=charinfo[4]
        case _:
            raise ValueError
    health=playerlistinfo[0]
    power=playerlistinfo[1]
    sattack=playerlistinfo[2]
    type=playerlistinfo[3]
    ihealth=playerlistinfo[4]
    croom=playerlistinfo[5]
    #level=playelistinfo[3]
    return health,power, sattack, type,ihealth,croom

def make_room():
    with open("newgamefile","r") as file:
        data=json.load(file)
    return data["rooms"]

def make_monsters():
    with open("newgamefile","r") as file:
        data=json.load(file)
    monsters=data["monster"]
    return monsters