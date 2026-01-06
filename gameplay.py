import json
from classes import Room
import startup

def main():
    startup.start()
    

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

def getcharacterinfo():
