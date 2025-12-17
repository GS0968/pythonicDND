import sys

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

class Room:
    def __init__(self,name, items, monster, trap, visit=False):
        self.rname=name 
        self.loot=items #will get a list of each loot in the room
        self.monsters=monster #will get a list of each monster(if visted the attacked mosters wont be seen) in the room
        self.visited=visit
        self._traps=trap #will show the number of traps present in the room (shouldnt be visible to characters/players)
    
    def showinfo(self):
        name=self.rname
        if len(self.loot)>0:
            items=self.loot
            for i in range(len(items)):
                itemstring=str()
                itemstring=itemstring+items[i]
        if len(self.monsters)>0:
            monsters=self.monsters
            for i in range(len(monsters)):
                monsterinfo=str()
                monster=Monster(monsters[i])
                monsterinfo=monsterinfo+monster.getinfo()
        if self.visited==True:
            visit="You have already visited this place"
        else:
            visit="You haven't opened this room"
        if self._traps>5:
            traps= "multiple traps"
        elif 0<self._traps<=5:
            traps= "a few traps"
        else:
            traps= "no traps"

class Monster: #didn't start yet just added for class room
    def __init__(self):
        self