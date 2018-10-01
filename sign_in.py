import cx_Oracle
class sign_cust:
    def sign_in(self,cust_id,password):
        self.cust_id=cust_id
        self.passw=password
        con=cx_Oracle.connect("SYSTEM/ameya@localhost/xe")
        cur=con.cursor()
        cur.execute("""SELECT * FROM Details WHERE account_no=:1 and password=:2 and enabled=0""",(self.cust_id,self.passw))
        
        if(cur.fetchall()):
            return True
        else:
            return False
        con.commit()
        con.close()
        
    def admin_in(self,admin_id,password):
        self.admin_id=admin_id
        self.passw=password
        con=cx_Oracle.connect("SYSTEM/ameya@localhost/xe")
        cur=con.cursor()
        cur.execute("""SELECT * FROM ADMIN WHERE admin_id=:1 and password=:2""",(self.admin_id,self.passw))
        
        if(cur.fetchall()):
            return True
        else:
            return False
        con.commit()
        con.close()
        
