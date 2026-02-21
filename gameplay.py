import json
from entities import Room
from entities import Monster
from entities import Character
import startup
import Getinfo
import time


def main():
    global sfile, character, rooms, monsters
    player, rooms, monsters, newfile, option=startup.start()
    cname=player[0]
    chealth=player[1]
    cpower=player[2]
    sattack=player[3]
    ctype=player[4]
    cihealth=player[5]
    croom=player[6]
    character=Character(cname, chealth, cpower, sattack, ctype, cihealth, croom)
    sfile= newfile
    croom=player[6]
    enterance=rooms[0]
    monsters=enterance[1]
    monstercount=len(monsters)
    if option=="new" or (croom=="Entrance Hall" and monstercount>0):
        with open("Openingtxt.txt","r") as file:
            for line in file:
                print(line)
                #for character in line:
                    #print(character, end='', flush=True)
                    #time.sleep(0.05)
        print()
                
        firstfight("Goblin")
        room=rooms[0]
    else:
        print(f"Hello hero... your journey awaits...\n You currently are in {croom}")
        startup.resmue()

def victory():
    with open("Victorytext.txt", "r") as file:
        for line in file:
            for character in line:
                print(character, end='', flush=True)
                time.sleep(0.1)
            

def fight(mname):
    global sfile,character
    player=character
    monsterinfo=Getinfo.getmonster(mname,sfile)
    mname=monsterinfo[0]
    mhealth=monsterinfo[1]
    mpower=monsterinfo[2]
    mrooms=monsterinfo[3]
    mihealth=monsterinfo[4]
    monster=Monster(mname,mhealth,mpower,mrooms,mihealth)
    while True:
        attacktype=input(f"Do you want to do a basic attack or the special attack? ")
        if "basic" in attacktype:
            player.attack(monsterinfo,sfile)
            monster.attack(sfile)
        elif "special" in attacktype:
            player.specialattack(monsterinfo,sfile)
            monster.attack(sfile)
        else:
            print(f"{attacktype} is not a valid input")
            pass
        

def firstfight(mname):
    global sfile,character
    monsterinfo=Getinfo.getmonster(mname,sfile)
    mname=monsterinfo[0]
    mhealth=monsterinfo[1]
    mpower=monsterinfo[2]
    mrooms=monsterinfo[3]
    mihealth=monsterinfo[4]
    monster=Monster(mname,mhealth,mpower,mrooms,mihealth)
    
    sname=character.sattackname()
    with open("Firstfight.txt","r") as file:
        for line in file:
            print(line)
            #for character in line:
                #print(character, end='', flush=True)
                #time.sleep(0.01)
    print()
    while True:
        attacktype=input("Do you want to do a basic attack or the special attack? ").lower()
        attacktype=attacktype.strip()
        if "basic" in attacktype:
            cattack=character.attack(monster,sfile)
            mhealth=monster.takedamage(cattack,sfile,character)
            if mhealth<=0:
                break
            mattack=monster.attack()
            chealth=character.takedamage(mattack)
            if chealth<=0:
                break
        elif "special" in attacktype:
            character.specialattack(monster,sfile)
            monster.attack(sfile)
        else:
            print(f"{attacktype} is not a valid input")
            pass
    startup.save_game(sfile,character.getinfo(),rooms,monsters)
main()