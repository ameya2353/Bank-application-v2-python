'''
Created on 29-Sep-2018

@author: AMEYA BRID
'''
import insert_cust
import sign_in
import acc_managment
x=" "

def submenu(account_no):
    acc_no=account_no
    print(x*70,"1. Address Change")
    print(x*70,"2. Money Deposit")
    print(x*70,"3. Money Withdrawal")
    print(x*70,"4. Print Statement")
    print(x*70,"5. Transfer Money")
    print(x*70,"6. Account Closure")
    print(x*70,"7. Customer Logout")
    ch=input("enter ur choice")
    if(ch=='1'):
        address=input("enter address")
        s=acc_managment.manage()
        s.address(address, acc_no)
        print('ADDRESS CHANGED TO',address)
        submenu(acc_no)
        
    elif(ch=='2'):
        acc=int(input("ENTER THE ACCOUNT NUMBER"))
        amt=int(input("enter the amount"))
        s=acc_managment.manage()
        s.deposit(amt, acc_no)
        submenu(acc_no)
        
 
    elif(ch=='3'):
        acc=int(input("ENTER THE ACCOUNT NUMBER"))
        amt=int(input("enter the amount"))
        s=acc_managment.manage()
        s.withdraw(amt, acc)
        submenu(acc_no)
    
    
    elif(ch=='4'):
        s=acc_managment.manage()
        s.prints(acc_no)
        submenu(acc_no)
    
    
    elif(ch=='5'):
        amt=int(input("enter the amount"))
        trans_d=int(input("enter the CUSTOMER ACCOUNT NUMBER to which money is to be transfered"))
        s=acc_managment.manage()
        s.transfer(amt, acc_no,trans_d)
        submenu(acc_no)
        
    
    elif(ch=='6'):
        print("YOU WOULD BE REDIRECTED TO THE MAIN MENU DIRECTLY")
        d=input("DO Y WANT TO CLOSE YOUR ACCCOUNT Y/N?")
        if(d=='Y' or d=='y'):
            s=acc_managment.manage()
            s.acc_close(acc_no)
            loop()
        elif(d=='n' or d=='N'):
            submenu(acc_no)
        
    elif(ch=='7'):
        signin()
    
    else:
        print("ENTER THE CORRECT CHOICE BETWEEN 1 to 7")
        submenu(acc_no)


def admin_menu():
    print(x*70,"1.Print Closed Account History")
    print(x*70,"2. Admin Logout")
    ch=input("enter ur choice")
    if (ch=='1'):
        acc_managment.manage().admin()
        print(" ")
        
        admin_menu()
    elif(ch=='2'):
        admin_in()
    else:
        print("please enter the correct choice")
        admin_menu()


def menu():
    print(x*80,"MENU")
    print(x*70,"1. SIGN UP (NEW CUSTOMER)")
    print(x*70,"2. SIGN IN (EXISTING CUSTOMER)")
    print(x*70,"3. ADMIN SIGN IN")
    print(x*70,"4. QUIT")
    q=input("enter your choice: ")
    return q


def signup():
    print("1.signup")
    print("2. back")
    ch=int(input("enter choice"))
    if(ch==1):
        name=input("Enter name")
        address=input("Enter Address")
        password=input("Set a password")
        ph_no=input("Enter phone number")
        try:
            insert_cust.InsertCust().InsertCust(name,address,ph_no,password)
            acc=insert_cust.InsertCust().account(name)
            print("your account number is",acc)
            print("remember your account number")
            
        except:
            print("something went wrong")
            signup()
        else:
            print("USER SUCCESSFULLY CREATED")
            loop()
    if(ch==2):
        loop()


def signin():
    print("1.signin")
    print("2.Main Menu")
    ch=int(input("enter choice"))
    if(ch==1):
        account_no=input("ACCOUNT NUMBER")
        password=input("Enter password")
        p=sign_in.sign_cust().sign_in(account_no, password)
        if(p==True):
            submenu(account_no)
        else:
            print("PLEASE CHECK YOUR ACCOUNT NUMBER AND PASSWORD OR YOUR ACCOUNT HAD BEEN PREVIOUSLY CLOSED")
            signin()
    if(ch==2):
        loop()
        


def admin_in():
    print("1.admin sign in")
    print("2.back")
    ch=input("enter choice")
    if(ch=='1'):
        admin_id=input("ADMIN ID")
        password=input("password")
        p=sign_in.sign_cust().admin_in(admin_id, password)
        if(p==True):
            admin_menu()
        else:
            print("wrong admin id or password")
            admin_in()
    elif(ch=='2'):
        loop()
    else:
        print("please chose between the give two options(1 or 2)")
        admin_in()



def loop():
    q=menu()
    if(q=='1'):
        signup()
    elif(q=='2'):
        signin()
    elif(q=='3'):
        admin_in()
    elif(q=='4'):
        a=input("""DO YOU WISH TO EXIT??
                ENTER Y/N FOR YES OR NO""")
        if(a=='y' or a=='Y'):
            print(x*70,"""THANK YOU FOR USING THIS SYSTEM.""")
            print(x*70,"""YOU HAVE EXITED THE SYSTEM""")
            exit()
        else:
            loop()
    else:
        print("ENTER THE CORRECT CHOICE BETWEEN 1 TO 4")
        loop()
        
loop()