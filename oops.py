#Create a Banking System:
#Parent_class - User - (which hold the details of users)
# Child_Class - Bank - (which hold the details of the amount, account_balance, deposite, withdraw

class User () :
    def __init__ (self,name,age,gender):
        self.name = name
        self.age=age
        self.gender=gender

    def show_user_details(self):
        print("Personal_details")
        print("Name :",self.name)
        print("age :",self.age)
        print("gender :",self.gender)

#Aswin = User("Aswin",24,"male")
#Aswin.show_user_details()

class Bank (User):
    def __init__(self,name,age,gender):
        super(). __init__ (name,age,gender)
        self.balance = 0

    def deposite(self,amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print("Account balance hasbeen updated : Rs", self.balance)

    def withdraw(self,amount):
        self.amount = amount
        if self.amount > self.balance :
            print("Insufficient fund | current_balance = Rs ", self.balance)
        else:
            self.balance = self.balance -self.amount
            print("Account balance hasbeen updated | current balance = Rs:",self.balance)

    def view_balance(self):
        self.show_user_details()
        print("Available account balance = Rs :", self.balance)
#Aswin = Bank("Aswin",24,"male")
#print(Aswin.name)
#print(Aswin.age)
#print(Aswin.gender)








