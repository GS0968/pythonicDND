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
    with open(sfile, "r")as file:
        data=json.load(file)
    rooms=data["rooms"]
    for i in range(len(rooms)-1):
        room=rooms[i]
        if roomname==room[0]:
            return room

def getmonster(monstername, sfile):
    with open(sfile, "r")as file:
        data=json.load(file)
    monsters=data["monster"]
    for i in range(len(monsters)-1):
        monster=monsters[i]
        if monstername==monster[0]:
            return monster

def defeat():
    with open("Deafeattxt.txt","r") as file:
        for line in file:
            print(line)


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
#def getfile()
    