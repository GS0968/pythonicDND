import json

def getroom(roomname, sfile):
    found=False
    with open(sfile, "r")as file:
        data=json.load(file)
    rooms=data["rooms"]
    for i in range(len(rooms)):
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
    for i in range(len(monsters)):
        monster=monsters[i]
        if monstername==monster[0]:
            return monster

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
            print(room[1])
            return room[1]