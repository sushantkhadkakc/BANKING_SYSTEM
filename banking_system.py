

class info:
  def __init__(self):
    self.money = 0
  def create(self):
    self.username=input("ENTER YOUR USERNAME\n")
    self.password=int(input("ENTER YOUR PASSWORD\n"))
    print("ACCOUNT CREATED\n")
  def login(self):
    user_name=input("ENTER YOUR USERNAME\n")
    password1=int(input("ENTER YOUR PASSWORD\n"))
    if(self.password==password1 and self.username==user_name):
      print("LOGIN SUCESSFULL\n")
      print(f"BANK BALANCE :{self.money}")
     
class payment(info):
   def system(self):
     
     self.payment_1=input("ENTER YOU WANT TO DESPOIT OR WITHDRAW\n").lower()
     if(self.payment_1=="despoit"):
       a=int(input("ENTER AMOUNT WHICH YOU WANT TO DESPOIT\n"))
       self.money+=a
       print(f"BANK BALANCE :{self.money}")
     elif(self.payment_1=="withdraw"):
       b=int(input("ENTER AMOUNT WHICH YOU WANT TO withdraw\n"))
       self.money-=b
       print(f"BANK BALANCE :{self.money}")     
   
a=payment()
a.create()
a.login()
a.system()
