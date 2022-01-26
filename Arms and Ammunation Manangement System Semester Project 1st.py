'''
LAB ASSIGNMENT 2
Names:Badar Masood(Sp19-bcs-051) & Muhammad Bilal Manzoor(Sp19-bcs-052)
Assignment Title:Arms Management System
'''
#Entity1:Arm
#Entity2:Buyer

print("-----------------------------------------------------")
print("\t    ARMS and AMMUNATION MANAGMENT SYSTEM")
print("-----------------------------------------------------")

arm_list=[] 
owner_list=[]
print()
def add_record():
    print("----------------ADD ARM RECORD -----------------------")
    print()
    confirmation="Y"
    
    while confirmation=="Y" or confirmation=="y":
        
        total_arms=int(input("Enter the amount records you want to create about arms:"))
        a=1
        print()
        for i in range(total_arms):
            arm_name=input("Enter arm name of arm_" +str(a)+" here:")
            arm_list.append(arm_name)
            arm_price=eval(input("Enter arm price of arm_" +str(a)+" here:"))
            arm_list.append(arm_price)
            arm_model=input("Enter arm model of arm_" +str(a)+" here:")
            arm_list.append(arm_model)
            arm_color=input("Enter arm color of arm_" +str(a)+" here:")
            arm_list.append(arm_color)
            a+=1
            print()
        total_owner=int(input("Enter the number of owners you want :"))
        print()
        b=1
        for j in range(total_owner):
            buyer_name=input("Enter buyer's name of buyer_"+str(b)+" here:")
            owner_list.append(buyer_name)
            contact_no=eval(input("Enter buyer's contact number of buyer_"+str(b)+" here:"))
            owner_list.append(contact_no)
            id_no=eval(input("Enter buyer's id card number of buyer_"+str(b)+" here:"))
            owner_list.append(id_no)
            arm_model=input("Enter model of arm parchased by buyer_"+str(b)+" here:")
            owner_list.append(arm_model)
            b+=1
            print()
        confirmation=input("Enter \"Y\" to continue to add more records and press any other key to move :")
    print(arm_list)
    print(owner_list)
def view_record():
    print("---------------VIEW RECORD ------------------------")
    choice=eval(input("Enter \"1\" to view record of arms and \"2\" to view record of owners:"))
    if choice==1:
        print()
        print("arm_name\t\tarm_price\t\tarm_model\t\tarm_color")
        for i in range(0,len(arm_list),4):
            print(arm_list[i],"\t\t",arm_list[i+1],"\t\t",arm_list[i+2],"\t\t",arm_list[i+3])
    if choice==2:
        print("buyer_name\t\tcontact_no\t\tid_no\t\tarm_model")
        for i in range(0,len(arm_list),4):
            print(owner_list[i],"\t\t",owner_list[i+1],"\t\t",owner_list[i+2],"\t\t",owner_list[i+3])
def edit_record():
    choice1=eval(input("Enter \"1\" to edit the record of arms and \"2\" to edit the record of owners:"))
    if choice1==1:
        item=input("Enter the name of arm you want to edit its record:")
        for i in range(0,len(arm_list),4):
            if item==arm_list[i]:
                arm_name=input("Enter arm name:")
                arm_list.insert(i,arm_name)
                arm_list.pop(i)
                arm_price=eval(input("Enter arm price:"))
                arm_list.insert(i,arm_price)
                arm_list.pop(i+1)
                arm_model=input("Enter arm model:")
                arm_list.insert(i,arm_model)
                arm_list.pop(i+1)
                arm_color=input("Enter arm color:")
                arm_list.insert(i,arm_color)
                arm_list.pop(i+1)
    if choice1==2:
        item=input("Enter the name of owner you want to edit:")
        for i in range(0,len(owner_list),4):
            if item==arm_list[i]:
                buyer_name=input("Enter buyer's name:")
                owner_list.insert(i,buyer_name)
                owner_list.pop(i+1)
                contact_no=eval(input("Enter buyer's contact number:"))
                owner_list.insert(i,contact_no)
                owner_list.pop(i+1)
                id_no=eval(input("Enter buyer's id card number:"))
                owner_list.insert(i,id_no)
                owner_list.pop(i+1)
                arm_model=input("Enter model of the arm buyer parchased:")
                owner_list.insert(i,arm_model)
                
def search_record():
    print("---------------SEARCH RECORD-----------------------")
    choice2=eval(input("Enter \"1\" to search the record of arms and \"2\" to search the record of owners:"))
    if choice2==1:
        item=input("Enter the name of arm you want to search:")
        print("arm_name\t\tarm_price\t\tarm_model\t\tarm_color")
        for i in range(0,len(arm_list),4):
            if item==arm_list[i]:
                print(arm_list[i],"\t\t",arm_list[i+1],"\t\t",arm_list[i+2],"\t\t",arm_list[i+3])
    if choice2==2:
        item=input("Enter the name of owner you want to search:")
        print("buyer_name\t\tcontact_no\t\tid_no\t\tarm_model")
        for i in range(0,len(arm_list),4):
            if item==owner_list[i]:
                print(owner_list[i],"\t\t",owner_list[i+1],"\t\t",owner_list[i+2],"\t\t",owner_list[i+3])
                    
def user_choice():
    
    choice_confirm="Y"
    while choice_confirm=="Y" or choice_confirm=="y":
        user_input=eval(input("Enter 1 to add Record:\nEnter 2 to view Record:\nEnter 3 to edit Record\nEnter 4 to Search Record:\nEnter Here:"))
        if user_input==1:
            add_record()
        elif user_input==2:
            view_record()
        elif user_input==3:
            edit_record()
        elif user_input==4:
            search_record()
        else:
            print("Invaild input")
            print()
        choice_confirm=input("Enter \"Y\" to continue the choice of User or press any other key to End The Program:")
user_choice()
