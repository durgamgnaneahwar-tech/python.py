# 1. Create a Student class with attributes name, age, and marks. Create an object and display all the details.

# class student:
#     def __init__(self,name,age,marks):
#         self.name=name
#         self.age=age
#         self.marks=marks
#     def display(self):
#         # print("NAME:",self.name)
#         # print("AGE:",self.age)
#         # print("MARKS:",self.marks)
#         if self.marks>=40:
#             print(self.name,"pass")
#         else:
#             print(self.name,"fail")

# s1=student("Gnaneshwar",23,35)
# s1.display()

##O/P:
# NAME: Gnaneshwar
# AGE: 23
# MARKS: 0.8723404255319149

# 2. Create a Car class with attributes brand and model. Create two objects with different values and display their details. 

# class CAR:
#     def __init__(self,brand,model) :
#         self.brand=brand
#         self.model=model
#         pass

#     def display(self):
#         print("BRAND:",self.brand)
#         print("MODEL:",self.model)

# c1 = CAR("Toyota", "Fortuner")
# c2 = CAR("BMW", "X5")
# c1.display()

### output:
# MARKS: 0.8723404255319149
# BRAND: Toyota
# MODEL: Fortuner

# c2.display()
### output:
# MODEL: Fortuner
# BRAND: BMW
# MODEL: X5

# 3. Create a Calculator class with methods add(), subtract(), multiply(), and divide(). Take two numbers from the user and perform all operations. 

# class Calculator:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b

#     def add(a,b):
#         print()
#         pass


# 4. Create a Rectangle class with attributes length and breadth. Create methods area() and perimeter(). 
# 5. Create an Employee class with attributes name, salary, and department. Create a method display_details() to print the employee information. 
# 6. Create a BankAccount class with an initial balance. Create methods deposit() and withdraw(). Display the updated balance after each operation. 
# class bank:
#     def __init__(self,name,blc):
#         self.name=name
#         self.blc=blc
#     def deposite(self,amount):
#         self.blc+=amount
#         print("deposite amount",amount)
#     def withdrawal(self,amount):
#         if amount<=self.balance:
#             self.blc-=amount
#             print("withdrawl amount",amount)
#         else:
#             print("check_blc")

#     def check(self):
#         print(amount)

# 7. Create a Student class with a method calculate_grade() that returns: ○ 90–100 → A ○ 75–89 → B ○ 60–74 → C ○ 40–59 → D ○ Below 40 → F 
# 8. Create a Person class with a method introduce() that prints the person's name, age, and city. Create three different objects and call the method for each. 
# 9. Create a Product class with attributes name, price, and quantity. Create a method total_cost() that calculates price × quantity and displays the result. 



class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Deposit amount must be positive.")
        self.display_balance()

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrawn: {amount}")
            else:
                print("Insufficient balance!")
        else:
            print("Withdrawal amount must be positive.")
        self.display_balance()

    def display_balance(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Updated Balance: {self.balance}")


c1= BankAccount("Gnaneshwar", 1000) 
c1.deposit(500)
c1.withdraw(300)
c1.withdraw(1500) 



class product:
    def __init__(self,name,price):
        self.name=name
        self.price=price

    def discount(self):
        if self.price>5000:
            disc=(self.price/100)*20
        elif self.price>2000:
            disc=(self.price/100)*10
        else:
            disc=(self.price/100)
        final_result=self.price-disc
        print("product_name:",self.name)
        print("price:",self.price)
        print("discount:",disc)
        print("final_price:",final_result)

p1=product("iphone",50000)
p2=product("sofa",2000)
p3=product("mouse",1500)
p1.discount()












