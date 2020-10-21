# Collaborators (including web sites where you got help: (enter none if you didn't need help)
#Megan
teamdictionary = {}
while True:
    teams=input("enter an NFL team: ")
    qbs=input("enter a quarterback: ")
    teamdictionary[teams]=qbs
    stop=input("press stop to stop or cont to continue ")
    if stop=="stop":
        for x, y in teamdictionary.items():
            print (x,y)
            break
    if stop=="cont":
        teams=input("enter an NFL team: ")
        qbs=input("enter a quarterback: ")
        stop=input("press stop to stop or cont to continue ")

        
        
        
        

