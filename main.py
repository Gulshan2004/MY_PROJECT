import random
"""
1 for stone
-1 for paper
0 for scissor
"""
computer= random.choice([-1,0,1])
youstr=input("Enter you choice :")
youdict={"s":1,"p":-1, "s":0}
reversedict={1:"stone",-1:"paper",0:"scissor"}
you=youdict[youstr]
#till now we have to  user one is the user and the second is the computer
print(f"you chose : {reversedict[you]}\ncomputer chose : {reversedict[computer]}")

if (computer==you):
    print("its a Draw !")
else:
   if(computer==1 and you==-1):
    print("you win!")
   elif(computer==1 and you==0):
    print("you lose!")
   elif(computer==-1 and you==1):
    print("you lose!")
   elif(computer==-1 and you==0):
    print("you win!")
   elif(computer==0 and you==1):
    print("you win!")
   elif(computer==0 and you==-1):
    print("you lose!")
   else:
    print("something went wrong")
