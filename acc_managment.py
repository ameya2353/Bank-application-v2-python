'''
Created on 29-Sep-2018

@author: AMEYA BRID
'''
import cx_Oracle
# import tabulate
from _datetime import datetime, date

class manage:
    def address(self,adress,acc_no):
        self.adress=adress
        self.acc_no=acc_no
        con=cx_Oracle.connect("SYSTEM/ameya@localhost/xe")
        cur=con.cursor()
        cur.execute("""UPDATE Details SET address=:1 WHERE account_no=:2 """,(self.adress,self.acc_no))
        con.commit()
        con.close()
        
    
    def acc_close(self,acc_no):
        self.acc_no=acc_no
        con=cx_Oracle.connect("SYSTEM/ameya@localhost/xe")
        cur=con.cursor()
        cur.execute("""UPDATE Details SET enabled=1,closed_time=:now WHERE account_no=:paramID """,{'paramId':self.acc_no,'now':datetime.now()})
        cur.execute("""DELETE FROM Balance WHERE account_no=:paramID""",{'paramID':self.acc_no})
        con.commit()
        con.close()
        
        
    def deposit(self,amt,cust_id):
        self.amt=amt
        self.cust_id=cust_id
        con=cx_Oracle.connect("SYSTEM/ameya@localhost/xe")
        cur=con.cursor()
        cur.execute("""SELECT balance FROM Balance WHERE account_no=:paramID """,{'paramId':self.cust_id})
        b=cur.fetchone()
        c=int(b[0])
        curr_bal=c+self.amt
        cur.execute("""UPDATE Balance SET balance=:1 WHERE account_no=:2 """,(curr_bal,self.cust_id))
        con.commit()
        con.close()
        
        
    def withdraw(self,amt,cust_id):
        self.amt=amt
        self.cust_id=cust_id
        con=cx_Oracle.connect("SYSTEM/ameya@localhost/xe")
        cur=con.cursor()
        cur.execute("""SELECT balance FROM Balance WHERE account_no=:paramID """,{'paramId':self.cust_id})
        b=cur.fetchone()
        c=int(b[0])
        curr_bal=c-self.amt
        cur.execute("""UPDATE Balance SET balance=:1 WHERE account_no=:2 """,(curr_bal,self.cust_id))
        con.commit()
        con.close()
        
        
    def transfer(self,amt,cust_id,trans_id):
        self.amt=amt
        self.cust_id=cust_id
        self.trans_id=trans_id
        con=cx_Oracle.connect("SYSTEM/ameya@localhost/xe")
        cur=con.cursor()
        cur.execute("""SELECT balance FROM Balance WHERE account_no=:paramID """,{'paramId':self.cust_id})
        b=cur.fetchone()
        c=b[0]
        curr_bal=c-self.amt
        cur.execute("""UPDATE Balance SET balance=:1 WHERE account_no=:2 """,(curr_bal,self.cust_id))
        cur.execute("""SELECT balance FROM Balance WHERE account_no=:paramID """,{'paramId':self.trans_id})
        b=cur.fetchone()
        c=b[0]
        curr_bal=c+self.amt
        cur.execute("""UPDATE Balance SET balance=:1 WHERE account_no=:2 """,(curr_bal,self.trans_id))
        cur.execute("""INSERT INTO Transactions VALUES(:1,:2,:3,:4)""",(self.trans_id,self.cust_id,self.amt,datetime.now()))
        con.commit()
        con.close()
        
     
    def prints(self,cust_id):
        self.cust_id=cust_id
        con=cx_Oracle.connect("SYSTEM/ameya@localhost/xe")
        cur=con.cursor()
        cur.execute("""SELECT name,address,phone_no FROM Details 
                       WHERE account_no=:paramID """,{'paramId':self.cust_id})
        b=cur.fetchone()
        print("CUSTOEMR NAME= ",b[0])
        print("ADDRESS= ",b[1])
        print("PHONE NUMBER= ",b[2])
        cur.execute("""SELECT balance FROM Balance 
                       WHERE account_no=:paraACC """,{'paraACC':self.cust_id})
        c=cur.fetchone()
        print("balance=",c[0])
        cur.execute("""SELECT * FROM Transactions WHERE account_from=:paraACC""",{'paraACC':self.cust_id})
        b=cur.fetchall()
        print("TRANSACTION DETAILS:")
        print('|',"Transfered To",'|',"Amount Transfered",'|',"Transfer Date",'      |')
        for item in b:
            print('|',item[0],' '*(12-(len(item[0]))),'|',item[2],' '*12,'|',item[3],'|')
        con.commit()
        con.close()     
        
        
    def admin(self):
        con=cx_Oracle.connect("SYSTEM/ameya@localhost/xe")
        cur=con.cursor()
        cur.execute("""SELECT account_no,name,address,phone_no,created_time,closed_time FROM Details 
                       WHERE enabled=1 """)
        b=cur.fetchall()
        print('| ACCOUNT_NO   | CUSTOMER NAME | LOCATION | PHONE NUMBER |     CREATED ON      |     CLOSED ON       |')
        for item in b:
            print('|  ',item[0],' '*4,'|',item[1],' '*(12-len(item[1])),'|',item[2],' '*(7-len(item[2])),'|',item[3],' ','|',item[4],'|',item[4],'|')     
        
        con.commit()
        con.close()
    
        
        
