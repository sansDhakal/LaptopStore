#importing files and date and time
from read import *
from bill import *
import datetime
now= datetime.datetime.now()
date_time = now.strftime("%Y-%m-%d %H-%M-%S")

#define function selling
def selling():

    name=input("Enter the name of costumer: ")
    #try except
    while True:
        try:
           contactnumber=int (input("Enter the contact number of the costumer: "))
           break
        except:
            print("INVALID,PLEASE ENTER VALID IMFORMATION")
            
    print ("-----------------------------------------------------------------------------------------------------------------------------------") 
    users_laptop=[]
        
    want = True
    while want==True:
        #displaying file.txt
       
        print ("---------------------------------------------------------------------------------------------------------------------------------")
        
        print("S.N \t\tLaptop Name            Company Name\t        Price\t      Quantity      \t  CPU        \t\t GUP")
        print ("---------------------------------------------------------------------------------------------------------------------------------------") 
        #opening file on read mode
        file = open("laptop.txt","r")
        a=1

        for line in file:
            print(a,"\t\t"+line.replace(",","\t \t"),)
            a=a+1
        print("---------------------------------------------------------------------------------------------------------------------------------------")
        file.close()
        print("\n")
        
        while True:
            
            ##asking for valid data
            serial=int(input("Write the serial number of laptop : "))
        
            while serial<=0 or serial>len(laptop_dictionary):
            
                
                        
                print("Please provide the valid serial number.")
                print ("\n")
                       
                serial=int (input("Please provide the serial number of laptop do you want to buy: "))
            
                
            selected_quantity=laptop_dictionary[serial][3]
            
            if int(selected_quantity)!=0:
                quantity =int(input("Please provide the number of quantity of the laptop: "))
            

                
            
                
                while quantity<=0 or quantity>int(selected_quantity):
                                    
                    print ("Dear costumer,the laptop you are searching in our laptop is not avialable in our shop")
                    print("\n")

                    quantity=int(input("Please provide the laptop quantity of the laptop you want to buy: ")) 
                print("\n")
                break
            else:
                print("Laptop is out of stock , please another id ")
           ##UPDATED TEXT FILE (STOCK)
                #calling stock functiom
        stock_filesubstract(serial,quantity,users_laptop)

        cont=input("Do you want to continue shopping  ? Y/N :")
        
        if cont =="Y" or cont == "y":
            want=True     
                         
        else:
            #calling sellbill
            sell_bill(name,contactnumber,date_time,users_laptop)
            want=False
          
                
        



#define function purchasing       

def purchasing():
    name=input("Enter the name of Company: ")
    contactnumber=int (input("Enter the contact number of the company: "))

    users_laptop=[]
            
    want=True
            
    while want==True:
        
         #displaying fille.txt         
        print ("---------------------------------------------------------------------------------------------------------------------------------")
        
        print("S.N \t\tLaptop Name            Company Name\t      Price\t    Quantity          \t CPU        \t\tGPU")
        print ("---------------------------------------------------------------------------------------------------------------------------------------") 
    #opeing file in read mode
        file = open("laptop.txt","r")
        a=1

        for line in file:
            print(a,"\t\t"+line.replace(",","\t \t"),)
            a=a+1
        print("---------------------------------------------------------------------------------------------------------------------------------------")
        file.close()
        print("\n")
        
        serial=int(input("Write the serial number of laptop : "))
        
        while serial<=0 or serial>len(laptop_dictionary):
            print("Please provide the valid serial number.")
            print ("\n")
            
            serial=int (input("Please provide the serial number of laptop do you want to buy: "))
        
        quantity =int(input("Please provide the number of quantity of the laptop: "))
        print ("\n")

           ##UPDATED TEXT FILE (STOCK)
        stock_fileadd(serial,quantity,users_laptop)
        
        #asking for continue shopping
        
        cont=input("Do you want to continue shopping  ? Y/N :")
        
        if cont =="Y" or cont == "y":
            want=True     
                         
        else:
            #calling purchase bill function
            purchase_bill(users_laptop,name,contactnumber,date_time)
            want=False
          



        
    
    
