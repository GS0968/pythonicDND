import json
from entities import Room
from entities import Monster
from entities import Character
import startup
import Getinfo
import time
import random


def main():
    global sfile, player, rooms, monsters, croom
    player, rooms, monsters, newfile, option=startup.start()
    cname=player[0]
    chealth=player[1]
    cpower=player[2]
    sattack=player[3]
    ctype=player[4]
    cihealth=player[5]
    croom=player[6]
    player=Character(cname, chealth, cpower, sattack, ctype, cihealth, croom)
    sfile= newfile
    enterance=rooms[0]
    monsters=enterance[1]
    monstercount=len(monsters)
    if option=="new" or (croom=="Entrance Hall" and monstercount>0):
        try:
            opening()
            update()
            move()
            resume()
        except KeyboardInterrupt:
            startup.save_game(sfile, player, rooms, monsters)
    else:
        print(f"Hello hero... your journey awaits...\nYou currently are in {croom}")
        resume()

def opening():
        with open("Openingtxt.txt","r") as file:
            for line in file:
                for character in line:
                    print(character, end='', flush=True)
                    time.sleep(0.05)
        if firstfight("Goblin")==0:
            defeat()
        else:
            firstvictory()

def firstfight(mname):

    with open("Firstfight.txt","r") as file:
        for line in file:
            for character in line:
                print(character, end='', flush=True)
                time.sleep(0.01)
    print()

    global sfile,player
    player=player
    monsterinfo=Getinfo.getmonster(mname,sfile)
    mname=monsterinfo[0]
    mhealth=monsterinfo[1]
    mpower=monsterinfo[2]
    mrooms=monsterinfo[3]
    mihealth=monsterinfo[4]
    monster=Monster(mname,mhealth,mpower,mrooms,mihealth)
    while True:
        attacktype=input("Do you want to do a basic attack or the special attack? ").lower()
        attacktype=attacktype.strip()
        if "basic" in attacktype:
            cattack=player.attack(monster,sfile)
            mhealth=monster.takedamage(cattack,sfile,player)
            if mhealth<=0:
                match random.randint(0,1):
                    case 0:
                        pass
                    case 1:
                        player.heal(100)
                        print(f"The {mname} has dropped a healing potion after it died.\n{player.getname()} gained 100 life points", end='', flush=True)
                        time.sleep(0.01)
                        player.update(sfile)
                return 1
            mattack=monster.attack()
            chealth=player.takedamage(mattack,sfile)
            if chealth<=0:
                return 0
        elif "special" in attacktype:
            cattack=player.specialattack(monster,sfile)
            mhealth=monster.takedamage(cattack,sfile,player)
            if mhealth<=0:
                match random.randint(0,1):
                    case 0:
                        pass
                    case 1:
                        player.heal(100)
                        print(f"The {mname} has dropped a healing potion after it died.\n{player.getname()} gained 100 life points", end='', flush=True)
                        time.sleep(0.01)
                        player.update(sfile)
                return 1
            mattack=monster.attack()
            chealth=player.takedamage(mattack,sfile)
            if chealth<=0:
                return 0
        else:
            print(f"{attacktype} is not a valid input")
            pass

def move():
    global sfile, player, rooms, monsters, croom
    print(f"You are currently in {croom}")
    newrooms=Getinfo.getnewrooms(croom)
    found=bool(False)
    newroomoption=str("You can go to the following rooms: ")
    if len(newrooms)>1:
        for i in range(len(newrooms)-1):
            newroomoption=newroomoption+str(newrooms[i])+", "
        i+=1
        newroomoption=newroomoption+str(newrooms[i])
        print(newroomoption)
    elif len(newrooms)==1:
        newroomoption=newroomoption+str(newrooms[0])
        print(newroomoption)
    
    while found==False:
        newroominput=input("Enter the room you want to go to: ")
        for i in range(len(newrooms)):
            if newrooms[i]==newroominput:
                found=True
                break
    player.move(newroominput,sfile)
    player.update(sfile)

def selectmonster():
    global sfile, rooms, croom
    print(f"You are currently in {croom}")
    monsterlist=Getinfo.getroommonster(croom,sfile)
    monsteroptions=str("You can fight the following monsters: ")
    if len(monsterlist)>1:
        for i in range(len(monsterlist)-1):
            monsteroptions=monsteroptions+str(monsterlist[i])+", "
        i+=1
        monsteroptions=monsteroptions+str(monsterlist[i])
        print(monsteroptions)
    elif len(monsterlist)==1:
        monsteroptions=monsteroptions+str(monsterlist[0])
        print (monsteroptions)
    while True:
        monsterfightinput=input("Which monster do you want to fight: ")
        for i in range(len(monsterlist)):
            if monsterlist[i]==monsterfightinput:
                return monsterfightinput
        print(f"The monster {monsterfightinput} is not in the room or has been defeated")

def update():
    global sfile, player, rooms, monsters
    with open(sfile, "r") as file:
        data = json.load(file)
    
    player = data["character"]
    rooms = data["rooms"]
    monsters= data["monster"]

def defeat():
    with open("Defeattxt.txt","r") as file:
        for line in file:
            print(line, end='', flush=True)
            time.sleep(0.1)

def firstvictory():
    with open("Firstfightvictory.txt","r") as file:
        for line in file:
            print(line, end='', flush=True)
            time.sleep(0.1)

def victory():
    with open("Victorytext.txt", "r") as file:
        for line in file:
            for player in line:
                print(player, end='', flush=True)
                time.sleep(0.1)

def fight(mname):
    global sfile,player
    player=player
    monsterinfo=Getinfo.getmonster(mname,sfile)
    mname=monsterinfo[0]
    mhealth=monsterinfo[1]
    mpower=monsterinfo[2]
    mrooms=monsterinfo[3]
    mihealth=monsterinfo[4]
    monster=Monster(mname,mhealth,mpower,mrooms,mihealth)
    while True:
        attacktype=input("Do you want to do a basic attack or the special attack? ").lower()
        attacktype=attacktype.strip()
        if "basic" in attacktype:
            cattack=player.attack(monster,sfile)
            mhealth=monster.takedamage(cattack,sfile,player)
            if mhealth<=0:
                match random.randint(0,1):
                    case 0:
                        pass
                    case 1:
                        player.heal(100)
                        print(f"The {mname} has dropped a healing potion after it died.\n{player.getname()} gained 100 life points", end='', flush=True)
                        time.sleep(0.01)
                        player.update(sfile)
                return 1
            mattack=monster.attack()
            chealth=player.takedamage(mattack,sfile)
            if chealth<=0:
                return 0
        elif "special" in attacktype:
            cattack=player.specialattack(monster,sfile)
            mhealth=monster.takedamage(cattack,sfile,player)
            if mhealth<=0:
                match random.randint(0,1):
                    case 0:
                        pass
                    case 1:
                        player.heal(100)
                        print(f"The {mname} has dropped a healing potion after it died.\n{player.getname()} gained 100 life points", end='', flush=True)
                        time.sleep(0.01)
                        player.update(sfile)
                return 1
            mattack=monster.attack()
            chealth=player.takedamage(mattack,sfile)
            if chealth<=0:
                return 0
        else:
            print(f"{attacktype} is not a valid input")
            pass

def resume():
    global croom,sfile
    while True:
        try:
            if Getinfo.getroommonster(croom,sfile)!=None:
                mname=selectmonster()
                if fight(mname)==0:
                    defeat()
                else:
                    move()
                    update()
            else:
                print("You have defeated all the monsters in this room")
                move()
                update()
        except KeyboardInterrupt:
            break 


main()