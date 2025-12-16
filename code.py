import sys

def start():
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

class game():
    def __init__(self,charnum=6,chartype):
        
