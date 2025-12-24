import sys
import random

def start(): #not fully complete yet
    option=input("Do you want to start a new game or load a previous game?: ")
    option=option.strip()
    option=option.lower()
    match option:
        case "load":
            oldfile=input("Enter the loadfile name: ")
            try:
                open(oldfile, "r") # have to set a format in how the data will be stored and then do th rest
            except FileNotFoundError:
                sys.exit("Error: File Not Found")

        case "new" | "new game":
            newfile=input("Enter savefile name: ")

class Character:
    def __init__(self, name):
        self.cname=name

class Room:
    def __init__(self,name, items, monster, trap, visit=False):
        self.rname=name 
        self.loot=items #will get a list of each loot in the room
        self.monsters=monster #will get a list of each monster(if visted the defeated mosters wont be seen) in the room
        self.visited=visit
        self._traps=trap #will show the number of traps present in the room (shouldnt be visible to characters/players)
    
    def showinfo(self):
        name=self.rname
        if self._traps>5:
            traps= "multiple traps"
        elif 0<self._traps<=5:
            traps= "a few traps"
        else:
            traps= "no traps"
        if self.visited==True:
            string=f"You have already visited this place. There are currently {len(self.monsters)} undefeated, {traps} armed, and {len(self.loot)} not looted in this place"

        else:
            visit=f"You haven't opened this room. There are currently {len(self.monsters)} undefeated, {traps} armed, and {len(self.loot)} not looted in this place"
        if len(self.monsters)>0:
            monsters=self.monsters
            for i in range(len(monsters)):
                monsterinfo=str()
                monster=Monster(monsters[i])
                monsterinfo=monsterinfo+monster.getinfo()

class Monster: 
    def __init__(self, name, health, power, room):
        self.mname=name
        self.health=health
        self.power=power
        self.room=room
    
    def attack(self):
        characters=getcharacters()
        character=random.choice(characters)
        characterinfo=gentinfo(character)
        c=Character(character, characterinfo)
        c.takedamage(self.power)

    def takedamage(self, damage):
        health=self.health-damage
        if health>0:
            self.health=health
        else:
            print("You have defeated the monster")
            removemonster(self.room)



class Character:
    def __init__(self, name, health, power, type):
        self.name=name
        self.health=health
        self.power=power
        self.type=type

    def attack(self,monster):
        dice=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]