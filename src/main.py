#Importing each file 
from operations import *
from read import *
from bill import *

#displaying of welcome message
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")

print ("----------------------------------------------------------------------------------------------------")
print("\t \t \t WELCOME!  you will definately enjoy Shopping !")
print("------------------------------------------------------------------------------------------------------")

print("\t \t \t \t Adobe laptop Shop")
print("------------------------------------------------------------------------------------------------------")
print(" \t\t \t \tkamalpokhari,kathmandu")
print("------------------------------------------------------------------------------------------------------")
print(" \t\t \t \t Contact Number:98219821")

print("\n")



#staring of while loop 
loop =True
while loop:
      
      #displaying message for user 
      print("Press 1 to sale")
      print("press 2 to purchase")
      print("press 3 to EXIT")
      print("\n")

     ##taking input from user
      ##try except
      while True:
            try:
            #Asking options
                  u_i=int(input("Enter the option to continue:  "))
                  if u_i<1 or u_i>3:
                        print("please enter option from 1 to 3")
                  else:
                        break
            except ValueError:
                        print ("Invalid")
            
      
      
            
                  
            
      
    #for user input is 1
      if u_i==1:
            
            
            print("\n")
            print ("-----------------------------------------------------------------------------------------------------------------------------------") 
            #calling function selling
            selling()
       #for user input is 2
      elif u_i==2:

            print("\n")
            print ("-----------------------------------------------------------------------------------------------------------------------------------") 
 #calling function purchasing
            purchasing()
   #for user input is 3      
      if u_i==3:
            loop=False
            print("----------You have exited-----------")




                        
                        
