import json
from entities import Room
from entities import Monster
from entities import Character
import startup
import Getinfo

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
    r=Room(rname,rmonsters,True)
    r.removemonster(mname)

def main():
    player, rooms, monsters, filename=startup.start()
    global sfile
    sfile= filename
    with open("Openingtxt.txt","r") as file:
        for line in file:
            print(line.strip())
    firstfight(player,"Goblin")
    room=rooms[0]

    
    



    
def victory():
    with open("Victorytext.txt", "r") as file:
        for line in file:
            print(line)

def fight(playerinfo,mname,):
    monsterinfo=Getinfo.getmonster(mname)
    mname=monsterinfo[0]
    mhealth=monsterinfo[1]
    mpower=monsterinfo[2]
    mrooms=monsterinfo[3]
    mihealth=monsterinfo[4]
    monster=Monster(mname,mhealth,mpower,mrooms,mihealth)
    cname=playerinfo[0]
    chealth=playerinfo[1]
    cpower=playerinfo[2]
    sattack=playerinfo[3]
    ctype=playerinfo[4]
    cihealth=playerinfo[5]
    croom=playerinfo[6]
    player=Character(cname, chealth, cpower, sattack, ctype, cihealth, croom)
    while player.gethealth()>0 and monster.gethealth()>0:
        attacktype=input(f"Do you want to do a basic attack or the special attack? ")
        match attacktype:
            case "special":
                player.specialattack(monsterinfo)
            case "basic":
                player.attack(monsterinfo)

def firstfight(playerinfo,mname):
    monsterinfo=Getinfo.getmonster(mname,sfile)
    mname=monsterinfo[0]
    mhealth=monsterinfo[1]
    mpower=monsterinfo[2]
    mrooms=monsterinfo[3]
    mihealth=monsterinfo[4]
    monster=Monster(mname,mhealth,mpower,mrooms,mihealth)
    cname=playerinfo[0]
    chealth=playerinfo[1]
    cpower=playerinfo[2]
    sattack=playerinfo[3]
    ctype=playerinfo[4]
    cihealth=playerinfo[5]
    croom=playerinfo[6]
    player=Character(cname, chealth, cpower, sattack, ctype, cihealth, croom)
    sname=player.sattackname()
    with open("Firstfight.txt","r") as file:
        for line in file:
            print(line.strip())
    while player.gethealth()>0 and monster.gethealth()>0:
        attacktype=input(f"Do you want to do a basic attack or the special attack? ")
        match attacktype:
            case "special":
                player.specialattack(monsterinfo)
            case "basic":
                player.attack(monsterinfo)
        monster.attack(sfile)

main()