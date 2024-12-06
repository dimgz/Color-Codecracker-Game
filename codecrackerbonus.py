#Dimitrios Gazos, A.M. 4035 

def check_feedback(guess):
    if guess == 'ooox':        #Check an invalid case of feedback
        print('This is impossible!!')
    num=len(guess)
    
    if num > 4:      #check the length of the code
        print("Feedback can't be bigger than 4 characters!")
        return 0
    for  i in range(0,num):
        
        if guess[i]!='x' and guess[i]!='o':    #check for invalid input 
            print("Feedback contains only 'o' and 'x' or maybe nothing")
            return 0
    
    return 1


    

# I use the same def with the other programm
def comp(code1, code2):             # def to print 'o' and 'x'
    findc = [0, 0, 0, 0]
    findd = [0, 0, 0, 0]            #2 lists        
    answer = ''
    for i in range(0,4):
        if code1[i] == code2[i]:        #compare the 2 codes for the same digit in the same position
            answer = answer + 'o'            #print 'o' if true
            findc[i] = 1
            findd[i] = 1                #if the 2 codes have the same digit in the same position change the 0 to 1 in the 2 lists so the program knows NOT to bother with that position anymore
    for i in range(0,4):
        if findc[i] == 0:                   #if a position on the first list is 1, don't use the position
           
            for j in range(0,4):
                if findd[j] == 0:               #if a position on the second list is 1, don't use the position
                    if code1[i] == code2[j]:
                        answer = answer + 'x'        #print 'x' if true     
                        findd[j] = 1
                                            
                        break
                
            
    return answer

#def to calculate the score
def score(code, lst):
    #print(code)
    kind = ['','o','oo','ooo','ox','oxx','oxxx','oox','ooxx','x','xx','xxx','xxxx']        #all the possible combinations 
    d = [0 for i in range(0,13)]    #list with 14 positions. Each position represents one of the above combinations
    skore = 0
    for l1 in lst:
        resp = comp(code, l1)           
        for i in range(0,13):
            if resp == kind[i]:         #if the respond is one of the above combinations count it
                d[i] = d[i] + 1      #count all the combinations

    #print(d)

    maxd=max(d)                 #the biggest number from the list

    #print (maxd)
    skore=len(lst)-maxd
    #print (skore)

    return skore
    




        

key_words = []       #generate the list with all the combinations
new_list = []
digits = ['1', '2', '3', '4', '5', '6']   
for i in digits:
    for j in digits:
        for k in digits:
            for l in digits:
                key_words.append(i+j+k+l)



#print(key_words)
#print(count)



guess = ''
guess_code = '1122'
print("CodeFinder game")
print("Think a 4-digit number with numbers from 1 to 6 and the PC will try to find it!!")
print("You can use 'o','x' or nothing in order to guide the CPU")
print("Type 'o' if one of the numbers is correct and in the right position")
print("Type 'x' if one of the numbers is correct but not in the right position")
print("Do not type anything if non of the above is true")
print("Let the games begin!!")

attempt = 1

while True:
    

    count = len(key_words)
    if count == 0:                  #when there are no numbers on the list (and maybe the player has made a mistake)
        print('Oops! Something is not right here..')
        break
    if count == 1:                  #in case only one number remains on the list
        print('Hey! The number must be %s I found it in %d attempts!' % (key_words[0],attempt-1))
        break
    
    print("Attempt %d : %s " % (attempt, guess_code)) #print the number of the attempts
    
     
    guess = input('Enter your feedback: ')  
    check_fee = check_feedback(guess)  #check if feedback is valid 
    if check_fee == 0:
        print('Try again')   #try again if not correct
        continue
 
    
    if attempt > 5:
        
        print('I could not find it within 5 attempts')
        print('It is beyond my powers!!')
        break
    if guess == 'oooo':
       print ('Ha! I found it in %d attempts!' % (attempt))  #if the user types 'oooo' end the game
       break
    
    attempt = attempt + 1
   
    for i in range(0,count):
        
        res = comp(guess_code, key_words[i])    #compare all the valid codes
        
        if guess == res:
           
           new_list.append(key_words[i])            #make an nww list with all the numbers from the compare
           #if attempt==2:
           #    print("i ",guess_code,key_words[i])
           #print (key_words[i])
           
    #count2 = len(new_list)
    #print(new_list)
    #print(count2)
    mscore = 0
    mdata=''
    for ll in new_list:
        rscore = score(ll, new_list)   
        if rscore > mscore:             #find the smallest number with the biggest score & the list is in order
            mscore = rscore
            mdata = ll     #save the number
    #print(mscore)
    #print(mdata)
    guess_code = mdata   #the guess code is the above number

    del key_words[:]    #delete the key words comtains
    key_words = list(new_list)
    del new_list[:]     #delete the new list contains

     

  
    
