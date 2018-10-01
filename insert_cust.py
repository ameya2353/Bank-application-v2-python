'''
Created on 29-Sep-2018

@author: AMEYA BRID
'''
import cx_Oracle
import datetime
class  InsertCust:
    
    def InsertCust(self,name,address,ph_no,password):
        con=cx_Oracle.connect("SYSTEM/ameya@localhost/xe")
        cur=con.cursor()
        cur.execute("""INSERT INTO Details 
                       VALUES(acc_no.nextval,:name,:address,:phno,:password,0,:now,NULL) """,{'name':name,'address':address,'phno':ph_no,'password':password,'now':datetime.datetime.now()})
        con.commit()
        con.close()
        
        
    def account(self,name):
        self.name=name
        con=cx_Oracle.connect("SYSTEM/ameya@localhost/xe")
        cur=con.cursor()
        cur.execute("""SELECT account_no FROM Details
                           WHERE name= :paraName """,{':paraName':name})
        acc=cur.fetchone()
        acco=acc[0]
        cur.execute("""INSERT INTO Balance(account_no,balance) VALUES(:paraACC,0)""",{':paraACC':acco})
        con.commit()
        con.close()
        return acco
       
d=InsertCust()
d.account('anagha')
