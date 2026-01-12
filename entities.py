import sys
import random
import json
import Getinfo
from gameplay import removemonster

class Room:
    def __init__(self,name, monster, visit="False"):
        self.rname=name 
        #self.loot=items #will get a list of each loot in the room (added later)
        self.monsters=monster #will get a list of each monster(if visted the defeated mosters wont be seen) in the room
        self.visited=visit
        #self._traps=trap #will show the number of traps present in the room (shouldnt be visible to characters/players) #will add later

    def to_dict(self): #needs to be edited to fit format
        return [
            self.rname,
            #"loot": self.loot,
            self.monsters,
            self._traps,
            self.visited
        ]

    @classmethod
    def from_dict(cls, data):  #needs to be edited to fit format
        monsters = [Monster.from_dict(m) for m in data["monsters"]]
        return cls(
            data["name"],
            #data["loot"],
            data["monsters"],
            data["traps"],
            data["visited"]
        )
    
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
            monsterinfo=str()
            for i in range(len(monsters)):
                monster=Monster(monsters[i])
                monsterinfo=monsterinfo+monster.getinfo()
    
    def removemonster(self,mname):
        monster=[]
        monsters=self.monsters
        for i in range(len(monsters)-1):
            if mname==monsters[i]:
                pass
            else:
                monster.append(monsters[i])
        self.monsters=monster

class Monster: 
    def __init__(self, name, health, power, room, ihealth):
        self.mname=name
        self.health=health
        self.power=power
        self.room=room
        self.ihealth=ihealth

    def to_dict(self):  #needs to be edited to fit format
        return {
            "name": self.mname,
            "health": self.health,
            "power": self.power,
            "room": self.room
        }

    @classmethod
    def from_dict(cls, data):  #needs to be edited to fit format
        return cls(
            data["name"],
            data["health"],
            data["power"],
            data["room"]
        )
    
    def attack(self,sfile):
        characterinfo=str(Getinfo.getcharacterinfo(sfile))
        name, health, power, type, initialhealth, room=characterinfo.split(" , ")
        user=Character(name, health, power, type, initialhealth, room)
        user.takedamage(self.power)
        print(f"The {self.mname} hits and deals {self.power}.")

    def takedamage(self, damage):
        health=int(self.health)-int(damage)
        if health>0:
            self.health=health
            print(f"The {self.mname} is at {self.health} health")
        else:
            print("You have defeated the monster")
            
            self.removeroom()
    
    def getinfo(self):
        details=[f"monster name: {self.mname}, intial health: {self.ihealth}, current health:{self.health}, attacking power:{self.power}"]
        return details
    
    def removeroom(self):
        characterinfo=Getinfo.getcharacterinfo()
        name, health, power, sattack, type, initialhealth, croom=characterinfo.split(" , ")
        room=self.room
        rooms=[]
        if croom!="":
            for i in range(len(room)-1):
                if room[i]==croom:
                    pass
                else:
                    rooms.append(room[i])
        self.room=rooms
        removemonster(croom,self.mname)
        if len(self.room)>1:
            self.health=self.ihealth
        
    def gethealth(self):
        return self.health

class Character:
    def __init__(self, name, health, power, specialpower, type, initialhealth, room):
        self.name=name
        self.health=health
        self.power=power #a list of basic attack containing the name of attack and the power of the damage
        self.sattack=specialpower #a list of special attack containing the name of attack and the power of the damage, and the probability, if paladin healing also available
        self.type=type
        self.croom=room #show the room current character is in
        self._ihealth=initialhealth #should not be changed throughout game for character
        #self.lvl=level

    def to_dict(self):  #needs to be edited to fit format
        return {
            "name": self.name,
            "health": self.health,
            "power": self.power,
            "type": self.type
        }

    @classmethod
    def from_dict(cls, data):   #needs to be edited to fit format
        return cls(
            data["name"],
            data["health"],
            data["power"],
            data["type"]
        )

    def attack(self,mdetails):
        power=self.power
        attackpower=power[1]*(random.randint(1,20)/10) #random.randint() is used to mimic a die to see how efficitive the acttack would be
        name=mdetails[0]
        health=mdetails[1]
        power=mdetails[2]
        room=mdetails[3]
        ihealth=mdetails[4]
        monster=Monster(name, health, power, room,ihealth)
        monster.takedamage(attackpower)
        print(f"{name} has taken damage! {random.choice(self.power[0])} strikes the enemy for {self.power[1]} damage.")
    
    def specialattack(self,mdetails):
        passvalue=random.randint(0,10)
        percentage=self.sattack[2]
        name=mdetails[0]
        if passvalue>=percentage:
            health=mdetails[1]
            power=mdetails[2]
            room=mdetails[3]
            ihealth=mdetails[4]
            monster=Monster(name, health, power, room,ihealth)
            print(f"{name} has taken critical damage! {self.sattack[0]} strikes the enemy for {self.sattack[1]} damage.")
            monster.takedamage(self.sattack[1])
        else:
            list=["Oooh, it seems you attack has been diminished to nothing.", "You lost control of the attack and missed."]
            string=random.choice(list)
            print(f"{string} {name} takes 0 damage.")
        if self.type=="paladin":
            self.health=self.health*self.sattack[3]
    
    def takedamage(self, damage):
        health=self.health-damage
        if health>0:
            self.health=health
            print(f"Now you have a health of: {self.health}")
        else:
            Getinfo.defeat()

    def gethealth(self):
        return self.health
    
    def sattackname(self):
        return self.sattack[0]