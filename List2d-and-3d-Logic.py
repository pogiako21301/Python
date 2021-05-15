#Magkasama
list2d = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]
listm = list2d[0][0], list2d[1][3], list2d[2][0]
print(listm)
#Magkahiwalay
list2d = [[1,2,3,4,5],[6,7,8,9,10]]
print(list2d[0][0])
print(list2d[1][0])
#2d but 3 list
list2d = [["Gars", "Garry", "Garreeh"], ["A", "B", "C"], ["D", "E", "F"]]
listm = list2d[0][1], list2d[1][1], list2d[2][0]
print(listm)
#3D
dota3d = [[["Mana Burn", "Blink", "Shield","Mana Void"],["B.Fury","Ward","B.Dance","Omni Slash"]],[["Quas","Wex","Exort","Invoke"],["Shadow Raze", "Necro", "Presence", "Req"]],[["Quas","Wex","Exort","Invoke"],["Rage", "Feast", "Open Wounds", "Infest"]]]
print(dota3d[0][0][1])
#For Loop
dota3d = [[["Mana Burn", "Blink", "Shield","Mana Void"],["B.Fury","Ward","B.Dance","Omni Slash"]],[["Quas","Wex","Exort","Invoke"],["Shadow Raze", "Necro", "Presence", "Req"]],[["Quas","Wex","Exort","Invoke"],["Rage", "Feast", "Open Wounds", "Infest"]]]
for hero in dota3d:
    for list in hero:
        for skill in list:
            print(skill)
