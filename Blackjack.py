#spør om navn på bruker og lode brukerdata
#spør hvor mye de skal bete
#wist spiller får over 21 taper de
#når de sier nei spiller dealeren til han har høyere en spilleren eller til han går bust
#del ut pengene etter hvem som winner og spør om de vil spille igjen
#vist ja gjenta vist nei lagre data og avslutt


from random import randint
from time import sleep
import os
cardnummbers=["2","3","4","5","6","7","8","9","10","jack","queen","king","ace"]
cardtypes=["hearts","diamonds","spades","clubs"]
cards=[y+" of "+x for x in cardtypes for y in cardnummbers]
money=500
bet=0

class player:
    def __init__(self,play,name, total,money):
        self.play=play
        self.name=name
        self.total=total
        self.money=money
    def add(self,cards=[]):
        global money
        global bet
        rand=randint(0,len(cards)-1)
        cardvalue=cards[rand].split(" of ")[0]
        if cardvalue == "jack"or cardvalue == 'king' or cardvalue ==  'queen':
            print(self.name,"got",cards[rand])
            self.total+=10
        elif cardvalue=='ace':
            if(self.play==True):
                print(self.name,"got",cards[rand])
                while True:
                    cin=input("You got an a do you want 11 or 1: ")
                    if(cin=="1"):
                        self.total+=1
                        break
                    elif(cin=="11"):
                        self.total+=11
                        break
                    else:
                        print("enter 1 or 11")
                        continue
            else:
                if self.total+11 <= 21:
                    self.total+=11
                else:
                    self.total+=1
        else:
            print(self.name,"got",cards[rand])
            self.total += int(cardvalue)
        if(self.total>=22):
            print(self.name,"went bust")
            if(self.play==True):
                money-=int(bet)
            else:
                print("You won!")
                money+=int(bet)
            PlayAgain(username)
        return self.total

def PlayAgain(username):
    global bet
    global money
    while True:
        cin=input("You have "+str(money)+" do you want to play again?")
        if(cin=="yes"):
            bet=setbet()
            dealer.total=0
            p1.total=0
            break
        elif(cin=="no"):
            print("ok see you next time "+username)
            with open(username+".txt","w") as file:
                file.write("money:"+str(money))
            exit()
        else:
            print("input yes or no")

def dealerdraw():
    global bet
    global money
    while True:
        dealer.add(cards)
        print("dealer total is",dealer.total)
        sleep(1)
        print('.')
        sleep(1)
        print('.')
        sleep(1)
        print('.')
        if(dealer.total>=p1.total):
            print("Dealer won")
            money-=int(bet)
            break

dealer=player(False,"dealer",0,1000000000)
p1=player(True,"you",0,money)

os.chdir(os.getcwd()+"/"+"blackjack files")
files=os.listdir()

username=input("input username:")
if username+".txt" in files:
    line=open(username+".txt","r")
    lines=line.read().split(":")
    money=int(lines[1])
    print("Welcome back "+username+"\ntotal money:"+str(money))
else:
    print("Welcome"+username+"enjoy your stay, you start white"+str(money)+"money")

def setbet():
    while True:
        bet=input("how much do you want to bet?")
        if True!=bet.isnumeric():
            print("you have to bet a nummber")
            continue
        if int(bet) > money:
            print("you don't have enought money to bet "+bet)
            continue
        return(bet)

bet=setbet()
while True:
    print("Your bet is "+str(bet)+", Your total is", p1.total ,"do you want to draw again?")
    cin=input()
    if cin=="no":
        dealerdraw()
        PlayAgain(username)
    elif cin!="yes":
        print("input yes or no")
        continue
    else:
        p1.add(cards)