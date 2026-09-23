"""1. inheritence:--
structure:=
class parent:    # parent class or super class
variable/con/methodcaller
class child(parent):  # sub class
var/con/method"""
##=====================================================================================
###types of inheritence:--
"""1.Single Inheritance"""

class parent:
    def father(self):
        print("2 homes")

class child(parent):
    def child(self):
        print("RE350 bike")

a=child()
a.father()
a.child()

##=====================================================================================

class employee:
    def __init__(self,emp_id,name,salary):
        self.emp_id=emp_id
        self.name=name
        self.salary=salary

    def display(self):
        print(f"emp_id is {self.emp_id} name is {self.name} salary is {self.salary}")

class manager(employee):
    def __init__(self, emp_id, name, salary):
        super().__init__(emp_id, name, salary)
    def role(self,job):
        self.job=job
        print(f"empjob is {self.job}")

e1=manager(12,"Gnaneswhar",10000)
e2=manager(13,"Rajeshwar",100001)
e1.display()
e2.display()
e1.role("manager")
e2.role("manager")

##=====================================================================================

class current_bank_acc:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance

    def deposite(self,amount):
        self.balance+=amount

    def check_balance(self):
        print(f"Your balance is {self.balance}")

class saving_bank_acc(current_bank_acc):
    def __init__(self, name, balance):
        super().__init__(name, balance)

    def interest(self):
        self.balance+=self.balance*0.05
        print("interest:",self.balance)

ac1=saving_bank_acc("Gnaneshwar",20000)
ac1.deposite(1000)
ac1.check_balance()
ac1.interest()

##=====================================================================================

"""2.Multiple Inheritance"""
"""3.Multilevel Inheritance"""
"""4.Hierarchical Inheritance"""
"""5.Hybrid Inheritance"""




"""class durgam_family:
    def __init__(self,surename,name,job):
        self.surename=surename
        self.name=name
        self.job=job

    def names(durgam_family):
        def __init__(surename,name,job):
            super().__init__(surename,name,job)

        def role(self,place):
            self.place=place
"""

class parent:
    print("abc")




