#importing read file
from read import *
# define function stockfilesubstract
def stock_filesubstract(serial,quantity,users_laptop):
    laptop_dictionary[serial][3]=int((laptop_dictionary)[serial][3])-int(quantity)
    file=open("laptop.txt","w")
    for values in laptop_dictionary.values():
        file.write(str(values[0])+","+str(values[1])+","+str(values[2])+","+str(values[3])+","+str(values[4])+","+str(values[5]))
        file.write("\n")
    file.close()


    Products_name=laptop_dictionary[serial][0]
    selected_quantity=quantity
    
    unit_price=laptop_dictionary[serial][2].replace("$",'')
    unit_price=unit_price.replace(" ",'')
    total_price=(int(unit_price))*(int(selected_quantity))
    

    users_laptop.append([Products_name,selected_quantity,unit_price,total_price])
                        
#define function stockfileadd
def stock_fileadd(serial,quantity,users_laptop):
    laptop_dictionary[serial][3]=int((laptop_dictionary)[serial][3])+int(quantity)
    file=open("laptop.txt","w")
    for values in laptop_dictionary.values():
        file.write(str(values[0])+","+str(values[1])+","+str(values[2])+","+str(values[3])+","+str(values[4])+","+str(values[5]))
        file.write("\n")
    file.close()


    Products_name=laptop_dictionary[serial][0]
    selected_quantity=quantity
    
    unit_price=laptop_dictionary[serial][2].replace("$",'')
    unit_price=unit_price.replace(" ",'')
    total_price=(int(unit_price))*(int(selected_quantity))
    
    users_laptop.append([Products_name,selected_quantity,unit_price,total_price])
  #define function sell_bill                      
def sell_bill(name,contactnumber,date_time,users_laptop):
    print("------------------------Thank you for shooping---------------------------")
    total=0
    for i in users_laptop:
       #for bill calculation
        total=total+(i[3])
    shipping_cost=500
    grand_total=total+shipping_cost
    
        
        
     #displaying for bill   
    print("\n")
    print("\t\t\t----------Adobe Laptop Shop Bill---------------")
    print("\n")
    print("\t\t\tKamalpokhari,Kathmandu ,   Contactnumber:9999999")
    print("-----------------------------------------------------------------------------------\n")
    print("\n")
    print("Name of the costumer: "+str(name))
    print("Contact Number :"+str(contactnumber))
    print("Date and time of shopping: "+str(date_time), )
    print("------------------------------------------------------------------------\n")
    print("\n")
    print("Purchase Details are: ")
    print("------------------------------------------------------------------------------------------------------------------\n")
    print("Item Name \t \t Total Quantity \t\tUnit Price \t \tTotal Price")
    for i in users_laptop:
        print(str(i[0])+"\t\t\t"+str(i[1])+"\t\t\t"+str(i[2])+"\t\t\t"+str(i[3])+"\n")
    print("-------------------------------------------------------------------------------------------------\n")
    print("Your Shipping cost is : "+str(shipping_cost)+"\n")
        
    print("Grand Total Price : "+ str(grand_total)+"\n")
    print("***Notes: Shipping cost is added in Grand Total Price ***")
    print("\n")
        
                
      #opening file in write mode  
    file=open(str(name)+str()+".txt","w")
        
    file.write("\n")
    file.write("\t \t \t \t LAPTOP'S BILL")
    file.write("\n")
    file.write("\t \t \t \t Kamalpokhari | Contact no. 9999")
    file.write("\n")
    file.write("------------------------------------------------------------------------\n")
    file.write("Laptop's details : \n")
    file.write("------------------------------------------------------------------------\n")

    file.write("Name of constumer: "+str(name)+"\n")
    file.write("Contact number:" +str(contactnumber)+"\n")

    file.write("Date and  time of purchase: "+ str(date_time)+"\n")
    file.write("------------------------------------------------------------------------\n")
    file.write("\n")
    file.write("Purchase Details: \n")
    file.write("------------------------------------------------------------------------\n")
    file.write("Item Name \t \t Total Quantity \t\tUnit Price \t \tTotal Price")
    file.write("------------------------------------------------------------------------\n")
    for i in users_laptop:
        file.write(str(i[0])+"\t\t\t"+str(i[1])+"\t\t\t"+str(i[2])+"\t\t\t"+str(i[3])+"\n")
    file.write("------------------------------------------------------------------------\n")
    file.write("\n")
    file.write("Your Shipping cost is : "+str(shipping_cost)+"\n")
    file.write("\n")
    file.write("Grand Total Price : "+ str(grand_total)+"\n")
    file.write("\n")
    file.write("***Notes: Shipping cost is added in Grand Total Price ***")
                    
    file.close()
#closing file

#define function purchase_bill
def purchase_bill(users_laptop,name,contactnumber,date_time):
    print("---------Thank you for shooping--------------")
    netamount=0
    for i in users_laptop:
        netamount=netamount+(i[3])
    vat="13%"
   
    grand_total = netamount+ 0.13 * netamount

        
        
     #displaying for bill   
    print("\n")
    print("\t\t\tLaptop Shop Bill")
    print("\n")
    print("\t\t\tKamalpokhari,Kathmandu Contactnumber:9999999")
    print("------------------------------------------------------------------------\n")
    print("\n")
    print("Name of the costumer: "+str(name))
    print("Contact Number :"+str(contactnumber))
    print("Date and time of shopping: "+str(date_time), )
    print("------------------------------------------------------------------------\n")
    print("\n")
    print("Purchase Details are: ")
    print("------------------------------------------------------------------------\n")
    print("Item Name \t \t Total Quantity \t \t Unit Price \t \t Total Price")
    for i in users_laptop:
        print(str(i[0])+"\t\t\t"+str(i[1])+"\t\t\t"+str(i[2])+"\t\t\t"+str(i[3])+"\n")
    print("------------------------------------------------------------------------\n")
    print("VAT is : "+vat+"\n")
        
    print("Grand Total Price : "+ str(grand_total)+"\n")
    print("***Notes: VAT amount is added in Grand Total Price ***")
    print("\n")
        
                
     #opening file in write mode   
    file=open(str(name)+str()+".txt","w")
        
    file.write("\n")
    file.write("\t \t \t \t LAPTOP'S BILL")
    file.write("\n")
    file.write("\t \t \t \t Kamalpokhari | Contact no. 9999")
    file.write("\n")
    file.write("------------------------------------------------------------------------\n")
    file.write("Laptop's details : \n")
    file.write("------------------------------------------------------------------------\n")

    file.write("Name of constumer: "+str(name)+"\n")
    file.write("Contact number:" +str(contactnumber)+"\n")

    file.write("Date and  time of purchase: "+ str(date_time)+"\n")
    file.write("------------------------------------------------------------------------\n")
    file.write("\n")
    file.write("Purchase Details: \n")
    file.write("------------------------------------------------------------------------\n")
    file.write("Item Name \t \t Total Quantity \t \t Unit Price \t \t Total Price")
    file.write("------------------------------------------------------------------------\n")
    for i in users_laptop:
        file.write(str(i[0])+"\t\t\t\t"+str(i[1])+"\t\t\t\t"+str(i[2])+"\t\t\t\t"+str(i[3])+"\n")
    file.write("------------------------------------------------------------------------\n")
    file.write("\n")
    file.write(" VAT  is : "+vat+"\n")
    file.write("\n")
    file.write("Grand Total Price : "+ str(grand_total)+"\n")
    file.write("\n")
    file.write("***Notes: VAT amount is added in Grand Total Price ***")
                    
    file.close()
    #closing file
