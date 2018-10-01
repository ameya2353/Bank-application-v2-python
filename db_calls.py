'''
Created on 29-Sep-2018

@author: AMEYA BRID
'''
import cx_Oracle
from cx_Oracle import connect
con=cx_Oracle.connect("SYSTEM/ameya@localhost/xe")
cur=con.cursor()
# cur.execute("""CREATE TABLE Details (
#                             account_no NUMBER(38,0) CONSTRAINTS acc_no_pk  PRIMARY KEY,
#                             name VARCHAR(50),
#                             address VARCHAR(100),
#                             phone_no NUMBER(10),
#                             password VARCHAR(20),
#                             enabled NUMBER(1),
#                             created_time DATE,
#                             closed_time DATE
#                                     )""") #USED TO CREATE TABLE TO STORE CUSTOMER DETAILS
# 
# cur.execute("""CREATE TABLE Balance (
#                             account_no NUMBER(38,0) CONSTRAINTS acc_no REFERENCES Details(account_no) ,
#                             balance NUMBER(30)
#                                     )""") #USED TO CREATE TABLE TO STORE THE BALANCE OF CUSTOMER
# 
# cur.execute("""CREATE TABLE Transactions (
#                             account_to VARCHAR(30)  ,
#                             account_from VARCHAR(30),
#                             amount NUMBER(30),
#                             transaction_time DATE
#                                     )""")#USED TO KEEP A TRACK OF THE CUSTOMERS TRANSACTIONS
# 
# cur.execute("""CREATE TABLE ADMIN (
#                             admin_id VARCHAR(30) PRIMARY KEY,
#                             password VARCHAR(30) )""")#ADMIN LOGINS RECORDS
# 
# cur.execute("""INSERT INTO ADMIN(admin_id,password) VALUES('ADMIN','PASSWORD') """)#IN THE PLACE OF ADMIN PUT ANY ID YOU WISH IN PLACE OF PASSWORRD PUT ANY PASSWORD U WISH



con.commit()
con.close()