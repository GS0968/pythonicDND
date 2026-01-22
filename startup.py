import sys
import json
from entities import Character
from entities import Room
from entities import Monster

def start(): #not fully complete yet
    # Accept several user inputs and loop until a valid choice is provided
    while True:
        option=input("Do you want to start a new game or load a previous game? (new/load): ")
        option=option.strip().lower()
        if "load" in option:
            oldfile=input("Enter the loadfile name: ")
            try:
                return load_game(oldfile,option)
            except FileNotFoundError:
                print("Error: File Not Found")
                continue
        if "new" in option or "start" in option:
            newfile=input("Enter savefile name: ")
            new_name = input("Enter the name for your character: ")
            while True:
                classtype=input("Enter the class you want your hero to be [warrior | rouge | mage | paladin]: ")
                try:
                    try:
                        health,power, sattack, classtype,ihealth,croom= make_char(classtype)
                        rooms=make_room()
                        monsters=make_monsters()
                    except FileNotFoundError:
                        sys.exit("Error 404, File Not Found")
                    else:
                        player=[new_name, health, power, sattack, classtype, ihealth, croom]
                        break
                except ValueError:
                    print("invalid character type")
            save_game(newfile, player, rooms, monsters)
            return player, rooms, monsters, newfile, option

def load_game(filename,option):
    with open(filename, "r") as file:
        data = json.load(file)
    
    player = data["character"]
    rooms = data["rooms"]
    monsters= data["monster"]
    return player, rooms, monsters, filename,option

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
    try:
        with open("newgamefile", "r") as file:
            data=json.load(file)
    except FileNotFoundError:
        raise FileNotFoundError
    else:
        charinfo=data["character"]
        match classtype:
            case "warrior":
                playerlistinfo=charinfo[0]
            case "rouge":
                playerlistinfo=charinfo[1]
            case "mage":
                playerlistinfo=charinfo[2]
            case "paladin":
                playerlistinfo=charinfo[3]
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
    try:
        with open("newgamefile","r") as file:
            data=json.load(file)
    except FileNotFoundError:
        raise FileNotFoundError
    else:
        return data["rooms"]
    

def make_monsters():
    try:
        with open("newgamefile","r") as file:
            data=json.load(file)
    except FileNotFoundError:
        raise FileNotFoundError
    else:
        return data["monster"]

def resume(sfile):
    with open(sfile, "r") as file:
        data=json.load(file)
    playerdetails=data["character"]
    