# Collaborators (including web sites where you got help: (enter none if you didn't need help)
#Megan
teamdictionary = {}
def code():
    while True:
        teams=input("enter an NFL team: ")
        qbs=input("enter a quarterback: ")
        teamdictionary[teams]=qbs
        stop=input("press stop to stop or cont to continue ")
        if stop=="stop":
            for x, y in teamdictionary.items():
                print (teamdictionary)
                import sys
                quit()
    if stop=="cont":
        code()

code()

        
        
        
        

