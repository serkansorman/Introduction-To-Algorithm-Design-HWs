import random

def findWinner(n,m):
    if n % (m+1) != 0:
        #First player can win if n = (m+1)k + 1, k can be any positive number
        if((n-1) % (m+1) == 0): 
            while(True):
                #If first condition is true and remain_coins mod(m+1) == 0 after his/her move, first player will be winner
                firstPlayerMove = random.randint(1,m)
                remain_coins = n - firstPlayerMove
                #Generate move until it is true for above condition
                while(remain_coins % (m+1) != 0):
                    firstPlayerMove = random.randint(1,m)
                    remain_coins = n - firstPlayerMove

                print("First Player:  ",firstPlayerMove)
                n = remain_coins
                if(n == 0):
                    print ("First is the winner")
                    break
                    
                #Second player's move is not important if first player play game with this way
                secondPlayerMove = random.randint(1,m) 
                print("Second Player: ",secondPlayerMove)
                n -= secondPlayerMove
                if(n == 0):
                    print ("Second is the winner")
                    break
        else:
            print ("Second is the winner")
    else:
        print ("Invalid m value")

findWinner(21,4)