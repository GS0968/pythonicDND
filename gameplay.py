import json
from entities import Room
from entities import Monster
from entities import Character
import startup
import Getinfo


def main():
    player, rooms, monsters, newfile, option=startup.start()
    global sfile
    sfile= newfile
    croom=player[6]
    enterance=rooms[0]
    monsters=enterance[1]
    monstercount=len(monsters)
    if option=="new" or (croom=="Entrance Hall" and monstercount>0):
        with open("Openingtxt.txt","r") as file:
            for line in file:
                print(line.strip())
        firstfight(player,"Goblin")
        room=rooms[0]
    else:
        print("Hello hero... your journey awaits...")
        startup.resmue()

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
    playerhealth=player.gethealth()
    monsterhealth=monster.gethealth()
    while playerhealth>0 and monsterhealth>0:
        attacktype=input(f"Do you want to do a basic attack or the special attack? ")
        if "basic" in attacktype:
            player.attack(monsterinfo,sfile)
            monster.attack(sfile)
        elif "special" in attacktype:
            player.specialattack(monsterinfo,sfile)
            monster.attack(sfile)
        else:
            pass
        playerhealth=player.gethealth()
        monsterhealth=monster.gethealth()
        

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
    playerhealth=chealth
    monsterhealth=mhealth
    while playerhealth>0 and monsterhealth>0:
        attacktype=input(f"Do you want to do a basic attack or the special attack? ")
        if "basic" in attacktype:
            player.attack(monsterinfo,sfile)
            monster.attack(sfile)
        elif "special" in attacktype:
            player.specialattack(monsterinfo,sfile)
            monster.attack(sfile)
        else:
            pass
        playerhealth=player.gethealth()
        monsterhealth=monster.gethealth()

main()