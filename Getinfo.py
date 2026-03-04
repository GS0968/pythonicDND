import json

def getcharacterinfo(sfile):
    with open(sfile, "r")as file:
        data=json.load(file)
    character=data["character"]
    characterinfo=str()
    for i in range(len(character)-1):
        characterinfo=characterinfo + str(character[i])+ " ; "
    i+=1
    characterinfo=characterinfo+str(character[i])
    return characterinfo

def getroom(roomname, sfile):
    found=False
    with open(sfile, "r")as file:
        data=json.load(file)
    rooms=data["rooms"]
    for i in range(len(rooms)-1):
        room=rooms[i]
        if roomname==room[0]:
            found=True
            return room
    if found==False:
        raise ValueError

def getmonster(monstername, sfile):
    with open(sfile, "r")as file:
        data=json.load(file)
    monsters=data["monster"]
    for i in range(len(monsters)-1):
        monster=monsters[i]
        if monstername==monster[0]:
            return monster


def getrooms(sfile):
    with open(sfile, "r")as file:
        data=json.load(file)
    return data["rooms"]

def getmonsters(sfile):
    with open(sfile, "r")as file:
        data=json.load(file)
    return data["monster"]

def getcharacter(sfile):
    with open(sfile, "r")as file:
        data=json.load(file)
    return data["character"]

def getnewrooms(croom):
    with open("Roomlayout", "r") as file:
        data=json.load(file)
    print(data[croom])
    return data[croom]

def getroommonster(croom,sfile):
    with open(sfile, "r")as file:
        data=json.load(file)
    rooms=data["rooms"]
    for i in range(len(rooms)):
        room=rooms[i]
        if room[0]==croom:
            if room[1]!=None:
                return room[1]
            else:
                return []

def getallinfo(sfile):
    with open(sfile, "r")as file:
        data=json.load(file)
    clearedrooms=[]
    rooms=data["rooms"]