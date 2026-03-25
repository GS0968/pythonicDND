import random
import json
import Getinfo


class Room:
    def __init__(self,name, monster, visit):
        self.rname=name 
        #self.loot=items #will get a list of each loot in the room (added later)
        self.monsters=monster #will get a list of each monster(if visted the defeated mosters wont be seen) in the room
        self.visited=visit
        #self._traps=trap #will show the number of traps present in the room (shouldnt be visible to characters/players) #will add later
    
    #def showinfo(self):
        #name=self.rname
        #if self._traps>5:
            #traps= "multiple traps"
        #elif 0<self._traps<=5:
            #traps= "a few traps"
        #else:
            #traps= "no traps"
        #if self.visited==True:
            #string=f"You have already visited this place. There are currently {len(self.monsters)} undefeated, {traps} armed, and {len(self.loot)} not looted in this place"
        #else:
            #visit=f"You haven't opened this room. There are currently {len(self.monsters)} undefeated, {traps} armed, and {len(self.loot)} not looted in this place"
       
        #if len(self.monsters)>0:
            #monsters=self.monsters
            #monsterinfo=str()
            #for i in range(len(monsters)):
                #monster=Monster(monsters[i])
                #monsterinfo=monsterinfo+monster.getinfo()
    
    def removemonster(self,mname,sfile):
        newmonsters=[]
        monsters=self.monsters
        for i in range(len(monsters)):
            if mname!=monsters[i]:
                newmonsters.append(monsters[i])
        self.monsters=newmonsters
        self.update(sfile)

    def update(self,sfile):
        with open(sfile,"r") as file:
            data = json.load(file)
        rooms = data["rooms"]
        for i in range(len(rooms)):
            room=rooms[i]
            if room[0]==self.rname:
                rooms[i]=self.getinfo()
            else:
                rooms[i]=room
        data["rooms"]=rooms
        with open(sfile, "w") as file:
            json.dump(data, file, indent=4)

    def getinfo(self):
        return [self.rname,self.monsters,self.visited]

class Monster: 
    def __init__(self, name, health, power, room, ihealth):
        self.mname=name
        self.health=health
        self.power=power
        self.mroom=room
        self.ihealth=ihealth


    def attack(self):
        print(f"The {self.mname} hits and deals {self.power}.")
        return self.power

    def takedamage(self, damage,sfile,character):
        health=int(self.health)-int(damage)
        if health>0:
            self.health=health
            print(f"The {self.mname} is at {self.health} health")
            self.update(sfile)
        else:
            print("You have defeated the monster")
            self.health=self.ihealth
            self.removeroom(sfile,character)
        return health

    
    def getinfo(self):
        details=[self.mname,self.health,self.power,self.mroom,self.ihealth]
        return details
    
    def removeroom(self,sfile,character):
        self.link(sfile,character)
        characterinfo=character.getinfo()
        croom=characterinfo[5]
        newrooms=[]
        mrooms=self.mroom
        for i in range(len(mrooms)):
            if mrooms[i]!=croom:
                newrooms.append(mrooms[i])
        self.mroom=newrooms
        if len(self.mroom)>1:
            self.update(sfile)
        else:
            self.removemonster(sfile)

    def link(self,sfile,character):
        characterinfo=character.getinfo()
        croom=characterinfo[6]
        with open(sfile,"r") as file:
            data=json.load(file)
        rooms=data["rooms"]
        match croom:
            case "Entrance Hall":
                roomdetail=rooms[0]
            case "Hall of Fame":
                roomdetail=rooms[1]
            case "Abandoned Armory":
                roomdetail=rooms[2]
            case "Dark Corridor":
                roomdetail=rooms[3]
            case "Poison Laboratory":
                roomdetail=rooms[4]
            case "Ancient Library":
                roomdetail=rooms[5]
            case "Chamber of Secrets":
                roomdetail=rooms[6]
            case _:
                raise ValueError
        rname=roomdetail[0]
        rmonsters=roomdetail[1]
        r=Room(rname,rmonsters,"True")
        r.removemonster(self.mname,sfile)

    def update(self,sfile):
        with open(sfile,"r") as file:
            data = json.load(file)
        monsters= data["monster"]
        newmonsters=[]
        for i in range(len(monsters)):
            monster=monsters[i]
            if monster[0]==self.mname:
                newmonsters.append(self.getinfo())
            else:
                newmonsters.append(monster)
        data["monster"]=newmonsters
        with open(sfile, "w") as file:
            json.dump(data, file, indent=4)
    
    def gethealth(self):
        return self.health
    
    def removemonster(self,sfile):
        with open(sfile,"r") as file:
            data = json.load(file)
        monsters= data["monster"]
        newmonsters=[]
        for i in range(len(monsters)):
            monster=monsters[i]
            if monster[0]==self.mname:
                pass
            else:
                newmonsters.append(monster)
        data["monster"]=newmonsters
        with open(sfile, "w") as file:
            json.dump(data, file, indent=4)

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

    def gethealth(self):
        return self.health

    def attack(self,Monster,sfile):
        mdetails=Monster.getinfo()
        power=self.power
        attackpower=power[1]*int(random.randint(1,20)/10) #random.randint() is used to mimic a die to see how efficitive the acttack would be
        mname=mdetails[0]
        health=mdetails[1]
        power=mdetails[2]
        room=mdetails[3]
        ihealth=mdetails[4]
        if attackpower>0:
            print(f"{mname} has taken damage! {random.choice(self.power[0])} strikes the enemy for {attackpower} damage.")
        else:
            print(f"{mname} dodged your {random.choice(self.power[0])}")
        return attackpower
    
    def specialattack(self,Monster,sfile):
        mdetails=Monster.getinfo()
        passvalue=random.randint(0,10)
        percentage=self.sattack[2]
        name=mdetails[0]
        if passvalue>=percentage:
            print(f"{name} has taken critical damage! {self.sattack[0]} strikes the enemy for {self.sattack[1]} damage.")
            if self.type=="paladin":
                self.health=self.health*self.sattack[3]
            return self.sattack[1]
        else:
            list=["Oooh, it seems you attack has been diminished to nothing.", "You lost control of the attack and missed."]
            string=random.choice(list)
            print(f"{string}")
            print(f"{name} takes 0 damage.")
            return 0
    
    def takedamage(self, damage:int,sfile):
        health=self.health-damage
        if health>0:
            self.health=health
            print(f"Now you have a health of: {self.health}")
            self.update(sfile)
        else:
            self.health=health
            self.update(sfile)
        return health

    def gethealth(self):
        return self.health
    
    def sattackname(self):
        return self.sattack[0]

    def getinfo(self):
        return [self.name,self.health,self.power,self.sattack,self.type,self._ihealth,self.croom]
    
    def heal(self,amount:int):
        self.health+=amount
    
    def update(self,sfile):
        with open(sfile,"r") as file:
            data = json.load(file)
        data["character"]=self.getinfo()
        with open(sfile, "w") as file:
            json.dump(data, file, indent=4)
    
    def move(self,newroom,sfile):
        self.croom=newroom
        self.update(sfile)

    def getinfostr(self):
        print(f"{self.name}, you currently have {self.health} lifepoints and you are in {self.croom}")

    def getname(self):
        return self.name
    