import random
import sys
exp=0
explvlup=10
name=input("Please enter your name")
namehp=10
namestr=5
namelevel=1
monsterlist=["Uler Kadut","Arden Pejuang Bangsa","uler uleran","Sexy Boiz","Magnificient Fashion BOIZ"]
monsterlvl=random.randint(1,6)
monsterhp=7+monsterlvl
monsterstr=7+monsterlvl
b=random.choice(monsterlist)
c=monsterlvl
def Mainmenu ():
    global name
    j = input("welcome "+ name +", do you want to fight or see your stats?")
    if (j == "stats"):
        menustat()
    if (j == "fight"):
        battle()

def menustat ():
    print("Fighter:",name)
    print("Level:",namelevel)
    print("HP:",namehp)
    print("STR",namestr)
    print("EXP",exp,"/",explvlup)
    Mainmenu()
def battle ():
    global b
    global c
    global monsterlist
    global monsterlvl
    monsterhp = 7 + monsterlvl
    monsterlvl = random.randint(1, 6)
    b=(random.choice(monsterlist))
    c= monsterlvl
    print("Enemy:",b)
    print("Level:",c)
    print(input("press enter to battle"))
    if namehp>=monsterhp:
        print("you survive")
        afterbattle()
    if namehp<monsterhp:
        print("you died")
        sys.exit()
def afterbattle():
    global namestr
    global namehp
    global namelevel
    exp=monsterlvl+9
    if exp>=explvlup:
        namehp=namehp+1
        namestr=namestr+1
        namelevel=namelevel+1
        print("you have leveled up")
        print("Fighter:",name)
        print("Level:",namelevel)
        print("HP:",namehp)
        print("STR:",namestr)
        print(input("press enter to go back"))
        Mainmenu()
    else:
        Mainmenu()
    return namehp,namestr,namelevel,
Mainmenu()









