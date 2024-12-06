#Dimitrios Gazos, A.M. 4035 

#main program


import random


def check(CodePlayer):
    err = "You can only use ['1', '2', '3', '4', '5', '6'] as colors. Try again:"
    if len(CodePlayer) !=4:
        print('The secret code has exactly four colors. Try again!')     # check if code is EXACTLY 4 digits
        return 0

    if CodePlayer.isdigit() == False:                                    # check if the code contains only digits
        print(err)
        return 0

    for i in range(0, len(CodePlayer)):                                  # check if the code contains the numbers ['0', '7', '8', '9']
        if CodePlayer[i] == '0':
            print (err)
            return 0
        if CodePlayer[i] == '7':
            print(err)
            return 0
        if CodePlayer[i] == '8':
            print(err)
            return 0
        if CodePlayer[i] == '9':
            print(err)
            return 0
        
    return 1
                   

def comp(code1, code2):        # def to print 'o' and 'x'
    findc = [0, 0, 0, 0]
    findd = [0, 0, 0, 0]       #2 lists which mark the positions
    answer = ''
    for i in range(0,4):
        if code1[i] == code2[i]:  #compare the 2 codes for the same digit in the same position
            answer = answer + 'o'       #print 'o' if true
            findc[i] = 1            #mark the position of 'o'
            findd[i] = 1             #if the 2 codes have the same digit in the same position change the 0 to 1 in the 2 lists so the program knows NOT to bother with that position anymore
    for i in range(0,4):
        if findc[i] == 0:         #if a position on the first list is 1, don't use the position
            
            for j in range(0,4):
                if findd[j] == 0:           #if a position on the second list is 1, don't use the position
                    if code1[i] == code2[j]:
                        answer = answer + 'x'           #print 'x' if true
                        findd[j] = 1              #mark the position of 'x'
                        
                       
                        break
  
    
    return answer
        

            
  
colors = {'1':'blue', '2':'green', '3':'yellow', '4':'white', '5':'pink', '6':'black'}


CodePlayer = ''
Attempts = 1


print('CODECRACKER GAME')     #print the starting messages
print('The objective is to guess the secret code in as few attempts as possible.')
print('\n')
while True:
    choose = input('Input 1 for 1-player game or 2 for 2-player game:')
    if choose == '1' or choose =='2':       #choose 1 or 2 players and make the program not advance if the answer is not right!
        break
    



if choose == '1':                                           #player vs PC
    print ('Player 1 please, enter your color code.')
    print ('You can use any combination of 4 symbols as colors')
    n1 = random.randrange(1,6)
    n2 = random.randrange(1,6)
    n3 = random.randrange(1,6)
    n4 = random.randrange(1,6)
    CodePC = '%d%d%d%d' % (n1,n2,n3,n4)               #generate 4 random codes and "stick" them together to create the 4-digit code, in case player selects player 1 mode!
    #print(CodePC) 
    

if choose == '2':                                           #player vs player
    
    print('Player 2 enter the secret code (4 colors).')
    print("You can use any combination of 4 symbols in ['1', '2', '3', '4', '5', '6'] as colors")
    while True:
        CodePC = input('')
        check_code2 = check(CodePC)                 #Player 2 inputs the code and the system checks if the code is valid
        if check_code2 == 0:
            print ('Try again:')                    #if not valid, try again
        else:
            print ("\n" * 100)
            print ('Player 1 please, enter your color code.')     #if the code is valid, advance to the game
            print ('You can use any combination of 4 symbols as colors')
            break


while Attempts < 9:                                     #maximum 8 attempts                                        
    st1 = "Attempt %d :" % (Attempts)                   #game shows the number of attempts 
        
    CodePlayer = input(st1)
    result = check(CodePlayer)                      #check code if valid and if not repeat without counting as an attempt
    if result == 0:
        continue
    
    ans = comp(CodePC, CodePlayer)            
    
    print (ans)
    
    if ans == 'oooo':                           # stop the game in case the answer is 'oooo'
        break
    Attempts = Attempts + 1                           #the game counts an attempt in case the ans is not right but it is valid
if ans == 'oooo':
    print ('Congratulations! You found it in',Attempts,'attempt(s)!')    #winning message

if ans != 'oooo':
    print ('You failed to guess within 8 attempts.')        #losing message
    print ('The secret code was', CodePC)
    print ('CPU WINS')







    
        

    
    
    
    


   
