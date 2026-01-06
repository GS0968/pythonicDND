import sys
import random
import json
import gameplay

class Room:
    def __init__(self,name, monster, trap, visit=False):
        self.rname=name 
        #self.loot=items will get a list of each loot in the room (added later)
        self.monsters=monster #will get a list of each monster(if visted the defeated mosters wont be seen) in the room
        self.visited=visit
        self._traps=trap #will show the number of traps present in the room (shouldnt be visible to characters/players)

    def to_dict(self):
        return {
            "name": self.rname,
            #"loot": self.loot,
            "monsters": [m.to_dict() for m in self.monsters],
            "traps": self._traps,
            "visited": self.visited
        }

    @classmethod
    def from_dict(cls, data):
        monsters = [Monster.from_dict(m) for m in data["monsters"]]
        return cls(
            data["name"],
            data["loot"],
            monsters,
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
    def __init__(self, name, health, power, room):
        self.mname=name
        self.health=health
        self.power=power
        self.room=room

    def to_dict(self):
        return {
            "name": self.mname,
            "health": self.health,
            "power": self.power,
            "room": self.room
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["name"],
            data["health"],
            data["power"],
            data["room"]
        )
    
    def attack(self):
        characterinfo=getcharacterinfo()
        name, health, power, type, initialhealth, room=characterinfo.split(" , ")
        c=Character(name, health, power, type, initialhealth, room)
        c.takedamage(self.power)

    def takedamage(self, damage):
        health=self.health-damage
        if health>0:
            self.health=health
        else:
            print("You have defeated the monster")
            self.removeroom()
    
    def getinfo(self):
        details=[f"{self.mname}, {str(self.health)}, {str(self.power)}"]
        return details
    
    def removeroom(self):
        characterinfo=getcharacterinfo()
        name, health, power, type, initialhealth, croom=characterinfo.split(" , ")
        room=self.room
        rooms=[]
        if croom!="":
            for i in range(len(room)-1):
                if room[i]==croom:
                    pass
                else:
                    rooms.append(room[i])
        self.room=rooms
        gameplay.removemonster(croom,self.mname)

class Character:
    def __init__(self, name, health, power, type, initialhealth, room):
        self.name=name
        self.health=health
        self.power=power
        self.type=type
        self.croom=room #show the room current character is in
        self._ihealth=initialhealth #should not be changed throughout game for character
        #self.lvl=level

    def to_dict(self):
        return {
            "name": self.name,
            "health": self.health,
            "power": self.power,
            "type": self.type
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["name"],
            data["health"],
            data["power"],
            data["type"]
        )

    def attack(self,mdetails):
        attack=self.power*(random.randint(1,20)/10) #random.randint() is used to mimic a die to see how efficitive the acttack would be
        name, health, power, room=mdetails.split(" , ")
        monster=Monster(name, health, power, room)
        monster.takedamage(attack)
    
    def takedamage(self, damage):
        health=self.health-damage
        if health>0:
            self.health=health
        else:
            print(f"{self.name} has been defeated")
