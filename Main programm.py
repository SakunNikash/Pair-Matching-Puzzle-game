#Importing modules and lists
import startup
import os
import Level2Programm
import score
from datetime import datetime
import time
import random
Labels=L=[' A',' A',' A',' A',' B',' B',' B',' B',' C',' C',' C',' C']
random.shuffle(L)
Variables=V=['01','02','03','04','05','06','07','08','09','10','11','12']
def puzzel():
    print('\u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2566\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2566\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2566\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2557')
    print('\u2551           \u2551           \u2551           \u2551           \u2551 ')
    print('\u2551   ',V[0],'    \u2551    ',V[1],'   \u2551    ',V[2],'   \u2551    ',V[3],'   \u2551')
    print('\u2551           \u2551           \u2551           \u2551           \u2551 ')
    print('\u2560\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u256C\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u256C\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u256C\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2563')
    print('\u2551           \u2551           \u2551           \u2551           \u2551 ')
    print('\u2551   ',V[4],'    \u2551    ',V[5],'   \u2551    ',V[6],'   \u2551    ',V[7],'   \u2551')
    print('\u2551           \u2551           \u2551           \u2551           \u2551 ')
    print('\u2560\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u256C\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u256C\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u256C\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2563')
    print('\u2551           \u2551           \u2551           \u2551           \u2551 ')
    print('\u2551   ',V[8],'    \u2551    ',V[9],'   \u2551    ',V[10],'   \u2551    ',V[11],'   \u2551')
    print('\u2551           \u2551           \u2551           \u2551           \u2551 ')
    print('\u255A\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2569\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2569\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2569\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u255D')
    return
def puzzelanswer():
    print('\u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2566\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2566\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2566\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2557')
    print('\u2551           \u2551           \u2551           \u2551           \u2551 ')
    print('\u2551   ',L[0],'    \u2551    ',L[1],'   \u2551    ',L[2],'   \u2551    ',L[3],'   \u2551')
    print('\u2551           \u2551           \u2551           \u2551           \u2551 ')
    print('\u2560\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u256C\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u256C\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u256C\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2563')
    print('\u2551           \u2551           \u2551           \u2551           \u2551 ')
    print('\u2551   ',L[4],'    \u2551    ',L[5],'   \u2551    ',L[6],'   \u2551    ',L[7],'   \u2551')
    print('\u2551           \u2551           \u2551           \u2551           \u2551 ')
    print('\u2560\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u256C\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u256C\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u256C\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2563')
    print('\u2551           \u2551           \u2551           \u2551           \u2551 ')
    print('\u2551   ',L[8],'    \u2551    ',L[9],'   \u2551    ',L[10],'   \u2551    ',L[11],'   \u2551')
    print('\u2551           \u2551           \u2551           \u2551           \u2551 ')
    print('\u255A\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2569\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2569\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2569\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u255D')
    return
Count=C=[0,0,0,0,0,0,0,0,0,0,0,0]
def count(num1):
    Count[num1-1]+=1
    return
def count1():
    num=0
    while num<12:
        if Count[num]>=2:
            Count[num]-=1
            num+=1
            continue
        else:
            Count[num]=0
            num+=1
            continue
    return
#Create variables
num1=0
num2=0
Score=0
start=''
def convert_timedelta(duration):
    seconds = duration.seconds
    minutes = (seconds % 3600)// 60
    seconds = (seconds % 60)
    print ('{} minutes, {} seconds'.format(minutes, seconds))
    return
#Game process
startup.Start()
while True:#game control command
    start=input("Continue to the game press'Y' :-")
    if start=='Y' or start=='y' or start=='Yes' or start=='yes' or start=='YES':
        os.system('clear')
        puzzel()
        DT1=time.time()
        dt=datetime.now()
        while True:
            #initializing variables
            try:
                num1 = int(input('Insert first cell address : '))
                os.system('clear')
            except ValueError:
                puzzel()
                print("Sorry, I didn't understand that.")
                continue
            if num1>12 or num1<1:
                puzzel()
                print('invalid input, insert using 1-12 number')
                continue
            elif V[num1-1]==' X':
                puzzel()
                print('choose not matched cell')
                continue
            elif V[num1-1]=='':
                puzzel()
                print('unknown character')
                continue
            #connecting V list and L list
            V[num1-1]=L[num1-1]
            puzzel()
            while True:
                try:
                    num2 = int(input('Insert second cell address : '))
                    os.system('clear')
                except ValueError:
                    puzzel()
                    print("Sorry, I didn't understand that.")
                    continue
                if num2==num1:
                    puzzel()
                    print("Don't choose before cell address, Try again")
                    continue
                if num2>12 or num2<1:
                    puzzel()
                    print('invalid input, insert using 1-12 number')
                    continue
                elif V[num2-1]==' X':
                    puzzel()
                    print('choose not matched cell')
                    continue
                elif V[num2-1]=='':
                    puzzel()
                    print('unknown character')
                    continue
                break
            os.system('clear')
            V[num2-1]=L[num2-1]
            puzzel()
            if V[num1-1]==V[num2-1]:#Section of taking action for matched pairs
                dt1=datetime.now()
                DT=dt1-dt
                print('Time : ')
                convert_timedelta(DT)
                print('matched')
                print('\n')
                print('\n')
                Score+=20
                V[num1-1]=V[num2-1]=' X'
                puzzel()
                if V[0]==V[1]==V[2]==V[3]==V[4]==V[5]==V[6]==V[7]==V[8]==V[9]==V[10]==V[11]==' X':
                    #end of the level1
                    dt1=datetime.now()
                    DT2=time.time()
                    print('Time : ')
                    convert_timedelta(DT)
                    print('Level 1 completed')
                    #scoring section
                    count1()
                    print('Time Bonus : ',score.set_bonus(DT2,DT1))
                    Score=Score+score.set_bonus(DT2,DT1)-5*(C[0]+C[1]+C[2]+C[3]+C[4]+C[5]+C[6]+C[7]+C[8]+C[9]+C[10]+C[11])
                    print('Score : ',Score)
                    print('Play again press P')
                    print('Play next level press Enter')
                    print('Exit the game press E')
                    while True:
                        start=input('Input caracter and press the Enter : ')
                        if start=='P' or start=='p':
                            V=['01','02','03','04','05','06','07','08','09','10','11','12']
                            C=[0,0,0,0,0,0,0,0,0,0,0,0]
                            Score=0
                            random.shuffle(L)
                            dt=datetime.now()
                            DT1=time.time()
                            break
                        elif start=='':
                        #Start point of level2
                            C=[0,0,0,0,0,0,0,0,0,0,0,0]
                            Score=0
                            Level2Programm.level2()
                        elif start=='E' or start=='e':
                            exit()
                        else:
                            print('enter valid charactor')
                            continue
            else:#section of taking action for unmatched pairs
                print('Not matched')
                dt1=datetime.now()
                DT=dt1-dt
                print('Time : ')
                convert_timedelta(DT)
                print('\n')
                print('\n')
                count(num1)
                V[num1-1]=str(num1).zfill(2)
                V[num2-1]=str(num2).zfill(2)
                puzzel()
    elif start=='N' or start=='n' or start=='No' or start=='no' or start=='NO':
        print('\n')
        print('\n')
        print('You exited from the game')
        print('\n')
        print('\n')
        exit()
    else:
        print('\n')
        print('\n')
        print('unknown insert')
        print('\n')
        print('\n')
        continue
