import time
import os
def Start():
    os.system('clear')
    print("\t********************G.S.N.EDIRISINGHE Games coporations*********************")
    print('ABC pair game Recommended requirments')
    print('Operating systems','\tmacOS,Ubuntu,Linux')
    print('Windows operating systems : Need Terminal console')
    print('loading',end='')
    Time=time.time()
    T=0
    while T!=5:
        time.sleep(1)
        print('.',end=' ')
        Time1=time.time()
        T=round(Time1-Time)
    print('\nInstruction!')
    time.sleep(2)
    print("\n\t Start the game press 'Y'")
    time.sleep(1)
    print("\n\t Quit the game press 'N'")
    time.sleep(3)
    print('\n\t When you are going to select tiles, \n \t \tEnter the tile address which appear on the puzzel')
    time.sleep(3)
    print('\n\t Tile address should be an Integer and between 0 to 13(without 0 and 13)')
    time.sleep(3)
    print('\n\t You can exit the after end of the level of this game')
    time.sleep(3)
    print('\n\tFollow the instructions that come up while playing')
    time.sleep(3)
    print('\nIntroducing levels of this game')
    time.sleep(2)
    print('\nLevel 1 - \tyou will have 60 seconds to match 6 pairs and 3 different numbers or pictures.\n \tLevel 2 - \tGrid will be revealed initially for 8 seconds and then you will have 60 seconds to match 6 pairs and 3 different Alphabet.')
    time.sleep(6)
    print('\nScoring of the game')
    print('\n\tIf you fail to match and you should have been able to (a matching tile was previously shown), you score (-5 * number of times match tile has been shown). \n\tSo if a matching tile has been revealedthree times before, you will score -15.\n\tAt the end of a level, if successful, you score a bonus of the number of seconds remaining.')
    time.sleep(7)
    print("\nLet's ready to play ABC pair games")
    return



        
