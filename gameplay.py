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
                    player= make_char(new_name,classtype)
                    rooms=make_room()
                    break
                except ValueError:
                    print("invalid character type")
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
        "player": Character.to_dict(),
        "rooms": [Room.to_dict() for room in rooms]
    }
    with open(filename, "w") as file:
        json.dump(game_state, file, indent=4)

def make_char(name,classtype):
    classtype=str(classtype)
    classtype=classtype.strip().lower()
    with open("newgamefile", "r") as file:
        data=json.load(file)
    charinfo=data["character info"]
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
    health=playerlistinfo[1]
    power=playerlistinfo[2]
    type=playerlistinfo[3]
    #level=playelistinfo[4]
    player=Character(name,health,power,type)

def make_room():
    with open("newgamefile","r") as file:
        data=json.load(file)
    rooms=data["rooms"]
    return rooms

def removemonster(room,mname):
    with open("newgamefile","r") as file:
        data=json.load(file)
    rooms=data["rooms"]
    match room:
        case "Entrance Hall":
            roomdetail=rooms[1]
        case "Hall of Fame":
            roomdetail=rooms[2]
        case "Abandoned Armory":
            roomdetail=rooms[3]
        case "Dark Corridor":
            roomdetail=rooms[4]
        case "Poison Laboratory":
            roomdetail=rooms[5]
        case "Ancient Library":
            roomdetail=rooms[6]
        case "Chamber of Secrets":
            roomdetail=rooms[7]
        case _:
            raise ValueError
    rname=roomdetail[1]
    rmonsters=roomdetail[2]
    rtraps=roomdetail[3]
    r=Room(rname,rmonsters,rtraps,True)
    r.removemonster(mname)    