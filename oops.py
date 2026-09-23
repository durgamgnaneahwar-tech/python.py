# #===============================================================================================
# ## OOPS ASSIGNMENT - 9 PROBLEMS WITH PROGRAMS
# #===============================================================================================

# """1. Create a Student class with attributes name, age, and marks.
# Create an object and display all the details.

# class student:
#     def __init__(self,name,age,marks):
#         self.name=name
#         self.age=age
#         self.marks=marks

#     def display(self):
#         print("name:",self.name)
#         print("age:",self.age)
#         print("marks:",self.marks)
# s1=student("gnaneshwar",23,"45")
# s1.display()

# o/p:
# name: gnaneshwar
# age: 23
# marks: 45


# 2. Create a Car class with attributes brand and model.
# Create two objects with different values and display their details.

# class car:
#     def __init__(self,brand,model):
#         self.brand=brand
#         self.model=model
#         print("brand:",self.brand)
#         print("modek:",self.model)

# c1=car("SUZUKI","swift")
# c2=car("HUNDAI","i20")

# o/p:
# brand: SUZUKI
# modek: swift
# brand: HUNDAI
# modek: i20


# 3. Create a Calculator class with methods add(), subtract(), multiply(), and divide().
# Take two numbers from the user and perform all operations.

# class calculator:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b

#     def add(self):
#         print("add:",self.a+self.b)

#     def subtract(self):
#         print("subtract:",self.a-self.b)

#     def multiply(self):
#         print("multiply:",self.a*self.b)

#     def divide(self):
#         print("divide:",self.a/self.b)

# c1=calculator(10,5)
# # c2=calculator(8,6)
# # c3=calculator(9,2)
# c1.add()
# c1.subtract()
# c1.multiply()
# c1.divide()


# o/p:
# add: 15
# subtract: 5
# multiply: 50
# divide: 2.0


# 4. Create a Rectangle class with attributes length and breadth.
# Create methods area() and perimeter().

# class Rectangle:
#     def __init__(self, length, breadth):
#         self.length = length
#         self.breadth = breadth

#     def area(self):
#         a = self.length * self.breadth
#         print("Area:", a)

#     def perimeter(self):
#         perimeter = 2 * (self.length + self.breadth)
#         print("Perimeter:", perimeter)

# r1 = Rectangle(10, 8)
# r1.area()
# r1.perimeter()

# o/p:
# Area: 80
# Perimeter: 36

# 5. Create an Employee class with attributes name, salary, and department.
# Create a method display_details() to print the employee information.

# class Employee:
#     def __init__(self,name,salary,department):
#         self.name=name
#         self.salary=salary
#         self.department=department

#     def display_details(self):
#         print("Name:",self.name)
#         print("Salary:",self.salary)
#         print("Department:",self.department)

# e1=Employee("Gnaneshwar",45000,"IT")
# e1.display_details()

# o/p:
# Name: Gnaneshwar
# Salary: 45000
# Department: IT

# 6. Create a BankAccount class with an initial balance.
# Create methods deposit() and withdraw(). Display the updated balance after each operation.

# class BankAccount:
#     def __init__(self,initial_balance):
#         self.initial_balance=initial_balance

#     def deposite(self,amount):
#         self.initial_balance+=amount
#         print("Deposit amount:", amount)
#         print("Availabale Balance:",self.initial_balance)

#     def withdraw(self,amount):
#         if self.initial_balance>=amount:
#             self.initial_balance -= amount
#             print("withdraw amount:",amount)
#             print("Availabale Balance:",self.initial_balance)
#         else:
#             print("Insufficient Balance")

# b1=BankAccount(50000)
# b1.deposite(500)
# b1.withdraw(5100)

# o/p:
# Deposit amount: 500
# Availabale Balance: 50500
# withdraw amount: 5100
# Availabale Balance: 45400

# 7. Create a Student class with a method calculate_grade() that returns:
# 90–100 → A
# 75–89 → B
# 60–74 → C
# 40–59 → D
# Below 40 → F

# class Student:
#     def __init__(self, marks):
#         self.marks = marks

#     def calculate_grade(self):
#         grades = [
#             (90, "A"),
#             (75, "B"),
#             (60, "C"),
#             (40, "D"),
#             (0, "F")
#         ]

#         for marks, grade in grades:
#             if self.marks >= marks:
#                 print("Grade:", grade)
#                 print("Marks:", self.marks)
#                 break

# s1 = Student(50)
# s1.calculate_grade()

# o/p:
# Grade: D
# Marks: 50


# 8. Create a Person class with a method introduce() that prints the person's name, age, and city.
# Create three different objects and call the method for each.

# class person:
#     def __init__(self,name, age,city):
#         self.name=name
#         self.age=age
#         self.city=city

#     def introduce(self):
#         print("Name:",self.name)
#         print("Age:",self.age)
#         print("City:",self.city)
# p1=person("Gnaneshwar",23,"HYD")
# p2=person("Rajeshwari",21,"PDPL")
# p1.introduce()
# p2.introduce()

# o/p:====
# Name: Gnaneshwar
# Age: 23
# City: HYD
# Name: Rajeshwari
# Age: 21
# City: PDPL

# 9. Create a Product class with attributes name, price, and quantity.
# Create a method total_cost() that calculates price × quantity and displays the result.

# class Product:
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity

#     def total_cost(self):
#         total = self.price * self.quantity
#         print("Product Name:", self.name)
#         print("Price:", self.price)
#         print("Quantity:", self.quantity)
#         print("Total Cost:", total)

# p1 = Product("Laptop", 50000, 2)
# p1.total_cost()


# o/p:====
# Product Name: Laptop
# Price: 50000
# Quantity: 2
# Total Cost: 100000"""

# #===============================================================================================
# # CLASS WORK
# #===============================================================================================
# ## STUDENT:

# class student:
#     def __init__(self,name,age,course):
#         self.name=name
#         self.age=age
#         self.course=course

#     def display(self):
#         print("name:",self.name)
#         print("age:",self.age)
#         print("course:",self.course)
# s1=student("gnaneshwar",23,"EEE")
# s1.display()


# """2. Employee Salary
# Create a class Employee with:
# name
# basic_salary
# Create a method display_salary() that prints the employee's salary.
# Example:
# Name: Aparna
# Salary: 30000"""

# class employee:
#     def __init__(self,name,basic_salary):
#         self.name=name
#         self.basic_salary=basic_salary

#     def display(self):
#         print("name:",self.name)
#         print("salary:",self.basic_salary)

# e1=employee("aparna",30000)
# e1.display()

# """ 3. Bank Account
# Create a class BankAccount with:
# account_holder
# balance
# Create methods:
# deposit(amount)
# withdraw(amount)
# display_balance()"""

# class bank():
#     def __init__(self,account_holder,balance):
#         self.account_holder=account_holder
#         self.balance=balance

#     def display_details(self):
#         print("acc holder name:",self.account_holder)
#         print("Bank balance:",self.balance)

#     def deposit(self,amount):
#         self.balance+=amount
#         print("diposite amount:",amount)

#     def withdrawl(self,amount):
#         if self.balance>=amount:
#             self.balance-=amount
#             print("withdrawl amount:",amount)
#             print("available balance:",self.balance)
#         else:
#             print("Insufficient Balance:" "ERROR")

#     def display_balance(self):
#         print("Balance:",self.balance)

# b1=bank("Gnaneshwar",500000)
# b1.display_details()
# b1.deposit(5000)
# b1.withdrawl(600000)
# b1.display_balance()

# #===============================================================================================
# class BankAccount:
#     def __init__(self, account_holder, balance):
#         self.account_holder = account_holder
#         self.balance = balance

#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#             print(f"Deposited: {amount}")
#         else:
#             print("Deposit amount must be positive.")
#         self.display_balance()

#     def withdraw(self, amount):
#         if amount > 0:
#             if amount <= self.balance:
#                 self.balance -= amount
#                 print(f"Withdrawn: {amount}")
#             else:
#                 print("Insufficient balance!")
#         else:
#             print("Withdrawal amount must be positive.")
#         self.display_balance()

#     def display_balance(self):
#         print(f"Account Holder: {self.account_holder}")
#         print(f"Updated Balance: {self.balance}")


# c1= BankAccount("Gnaneshwar", 1000) 
# c1.deposit(500)
# c1.withdraw(300)
# c1.withdraw(1500) 

# #======================================================================

# class product:
#     def __init__(self,name,price):
#         self.name=name
#         self.price=price

#     def discount(self):
#         if self.price>5000:
#             disc=(self.price/100)*20
#         elif self.price>2000:
#             disc=(self.price/100)*10
#         else:
#             disc=(self.price/100)
#         final_result=self.price-disc
#         print("product_name:",self.name)
#         print("price:",self.price)
#         print("discount:",disc)
#         print("final_price:",final_result)

# p1=product("iphone",50000)
# p2=product("sofa",2000)
# p3=product("mouse",1500)
# p1.discount()


# #=======================================================================================================================================================================================================##################
# ## OOPS BASIC PROBLEMS:  20 QUESTIONS
# #=======================================================================================================================================================================================================##################

# """Level 1 – Basic """

# """1. Student Details 
# Create a class Student 
# with: 
# • Variables: name, age, course  
# • Constructor to initialize the variables  
# • Method display() to print student details.  
# Expected concept: Constructor + instance variables + method """

# class student:
#     def __init__(self,name,age,course):
#         self.name=name
#         self.age=age
#         self.course=course

#     def display(self):
#         print("name:",self.name)
#         print("age:",self.age)
#         print("course:",self.course)
        
# s1=student("gnaneshwar",23,"EEE")
# s1.display()

# """output:-
# name: gnaneshwar
# age: 23
# course: EEE"""

# #==========================================================================================

# """2. Employee Salary 
# Create a class Employee 
# with: 
# • name , basic_salary  
# Create a method display_salary() that prints the employee's salary. 
# Example: Name: Aparna Salary: 30000 """

# class employee:
#     def __init__(self,name,basic_salary):
#         self.name=name
#         self.basic_salary=basic_salary

#     def display(self):
#         print("name:",self.name)
#         print("salary:",self.basic_salary)
        

# e1=employee("aparna",30000)
# e1.display()

# """output:-
# name: aparna
# salary: 30000"""


# #==========================================================================================


# """3. Bank Account 
# Create a class BankAccount 
# with
# • account_holder  
# • balance  
# Create methods: 
# • deposit(amount)  
# • withdraw(amount)  
# • display_balance()  
# If the withdrawal amount is greater than the balance,display "Insufficient Balance". """

# class bank():
#     def __init__(self,account_holder,balance):
#         self.account_holder=account_holder
#         self.balance=balance

#     def display_details(self):
#         print("acc holder name:",self.account_holder)
#         print("Bank balance:",self.balance)
        

#     def deposit(self,amount):
#         self.balance+=amount
#         print("diposite amount:",amount)
        

#     def withdrawl(self,amount):
#         if self.balance>=amount:
#             self.balance-=amount
#             print("withdrawl amount:",amount)
#             print("available balance:",self.balance)
#         else:
#             print("Insufficient Balance:" "ERROR")
            

#     def display_balance(self):
#         print("Balance:",self.balance)
        

# b1=bank("Gnaneshwar",500000)
# b1.display_details()
# b1.deposit(5000)
# b1.withdrawl(600000)
# b1.display_balance()

# """output:-
# acc holder name: Gnaneshwar
# Bank balance: 500000
# diposite amount: 5000
# Insufficient Balance:ERROR
# Balance: 505000"""


# #==========================================================================================


# """4. Mobile Phone
# Create a class Mobile 
# with: 
# • brand  
# • model  
# • price  
# Create a method 
# display() 
# to display all details.
# Create objects for 3 different mobiles."""

# class mobile:
#     def __init__(self,brand,model,price ):
#         self.brand=brand
#         self.model=model
#         self.price=price

#     def display(self):
#         print("Mobile Brand:",self.brand)
#         print("Mobile Model:",self.model)
#         print("Mobile Price:",self.price)
        

# m1=mobile("samsung","S 25 ULTRA",155000)
# m2 = mobile("Apple", "iPhone 17", 120000)
# m3 = mobile("OnePlus", "13", 70000)

# m1.display()
# m2.display()
# m3.display()


# """outputs:=
# Mobile Brand: samsung
# Mobile Model: S 25 ULTRA
# Mobile Price: 155000

# Mobile Brand: Apple
# Mobile Model: iPhone 17
# Mobile Price: 120000

# Mobile Brand: OnePlus
# Mobile Model: 13
# Mobile Price: 70000"""


# #==========================================================================================


# """5. Rectangle Calculation
# Create a class Rectangle 
# with: 
# • length  
# • breadth  
# Create methods:
# • area() 
# • perimeter()  
# Use the constructor to initialize length and breadth."""


# class Rectangle:
#     def __init__(self, length, breadth):
#         self.length = length
#         self.breadth = breadth

#     def area(self):
#         a = self.length * self.breadth
#         print("Area:", a)
        

#     def perimeter(self):
#         perimeter = 2 * (self.length + self.breadth)
#         print("Perimeter:", perimeter)
        

# r1 = Rectangle(10, 8)
# r1.area()
# r1.perimeter()

# """o/p:
# Area: 80
# Perimeter: 36"""

# #==========================================================================================
# """Level 2 – Logic-Based Problems"""

# """6. Student Marks 
# Create a class Student 
# with:
# • name
# • marks  
# Create methods:
# • display_marks()  
# • check_result()  
# Rules: 
# marks >= 40 → Pass 
# marks < 40  → Fail 
# Create objects for 5 students. """

# class Student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks

#     def display_marks(self):
#         print("Student Name:",self.name)
#         print("MARKS:",self.marks)
        

#     def check_result(self):
#         if self.marks>= 40:
#             result="PASS"
#         else:
#             result="FAIL"
#         print(result)
        

# s1 = Student("Rahul", 49)
# s2 = Student("Sneha", 39)
# s3 = Student("Kiran", 75)
# s4 = Student("Priya", 35)
# s5 = Student("Arjun", 50)

# s1.display_marks()
# s1.check_result()

# s2.display_marks()
# s2.check_result()

# s3.display_marks()
# s3.check_result()

# s4.display_marks()
# s4.check_result()

# s5.display_marks()
# s5.check_result()

# """output:--
# Student Name: Rahul
# MARKS: 49
# PASS

# Student Name: Sneha
# MARKS: 39
# FAIL

# Student Name: Kiran
# MARKS: 75
# PASS

# Student Name: Priya
# MARKS: 35
# FAIL

# Student Name: Arjun
# MARKS: 50
# PASS"""

# #==========================================================================================

# """7. Employee Bonus 
# Create a class Employee 
# with:
# • name
# • salary
# Create a method 
# calculate_bonus(). 
# Rules: 
# salary >= 50000 → 10% bonus 
# salary < 50000  → 5% bonus 
# Display: Employee Name Salary Bonus Total Salary """

# class Employee:
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary

#         print("Employee name:",self.name)
#         print("Salary:",self.salary)
        

#     def calculate_bonus(self):
#         if self.salary>= 50000:
#             bonus=self.salary*0.10
#         else:
#             bonus=self.salary*0.05
#         Total_Salary=self.salary+bonus

#         print("Bonus:",bonus)
#         print("Total Salary:",Total_Salary)
        

# e1=Employee("Gnaneswhar",55000)
# e1.calculate_bonus()

# """output:--
# Employee name: Gnaneswhar
# Salary: 55000
# Bonus: 5500.0
# Total Salary: 60500.0"""

# #==========================================================================================

# """8. Product Discount
# Create a class Product 
# with:
# • product_name
# • price  
# Create a method 
# calculate_discount(). 
# Rules: 
# price >= 5000 → 20% discount
# price >= 2000 → 10% discount
# otherwise → 5% discount 
# Display the final price. """

# class Product:
#     def __init__(self,product_name,price):
#         self.product_name=product_name
#         self.price=price

#     def calculate_discount(self):
#         if self.price >= 5000:
#             discount=self.price*0.20
#         elif self.price>= 2000:
#             discount=self.price*0.10
#         else:
#             discount=self.price*0.05
#         total = self.price - discount
#         print("Product:",self.product_name)
#         print("Final price:",total)
        

# p1 = Product("Headphones", 3000)
# p2 = Product("Keyboard", 1500)

# p1.calculate_discount()
# p2.calculate_discount()

# """output:--
# Product: Headphones
# Final price: 2700.0

# Product: Keyboard
# Final price: 1425.0"""

# #==========================================================================================

# """9. ATM Transaction 
# Create a class ATM 
# with:
# • account_number
# • balance  
# Create methods: 
# • deposit()
# • withdraw()
# • check_balance()  
# The object should maintain the updated balance after every transaction."""

# class ATM:
#     def __init__(self, account_number, balance):
#         self.account_number = account_number
#         self.balance = balance
#         print("Balance:", self.balance)
        

#     def deposit(self, amount):
#         self.balance += amount
#         print("Deposit Amount:", amount)
#         print("Balance:", self.balance)
        

#     def withdraw(self, amount):
#         if self.balance >= amount:
#             self.balance -= amount
#             print("Withdraw:", amount)
#             print("Balance:", self.balance)
#         else:
#             print("Insufficient Balance")
            

#     def check_balance(self):
#         print("Updated Balance:", self.balance)
        

# a1 = ATM(963852741, 15000)
# a1.deposit(5000)
# a1.withdraw(2000)
# a1.check_balance()  

# """output:--
# Balance: 15000
# Deposit Amount: 5000
# Balance: 20000
# Withdraw: 2000
# Balance: 18000
# Updated Balance: 18000"""

# #==========================================================================================

# """10. Car Information 
# Create a class Car
# with:
# • brand
# • model
# • price
# • fuel_type 
# Create methods:
# • display()
# • check_price()  
# If price is greater than ₹10,00,000, display "Premium Car",
# otherwise "Normal Car"."""

# class car:
#     def __init__(self,brand,model,price,fuel_type):
#         self.brand=brand
#         self.model=model
#         self.price=price
#         self.fuel_type=fuel_type

#     def display(self):
#         print("Brand:", self.brand)
#         print("Model:", self.model)
#         print("Price:", self.price)
#         print("Fuel Type:", self.fuel_type)
        

#     def check_price(self):
#         if self.price>1000000:
#             print("car range:","Premium Car")
#         else:
#             print("car range:","Normal Car")
            


# c1 = car("Toyota", "Fortuner", 4500000, "Diesel")
# c1.display()
# c1.check_price()

# c2 = car("Hyundai", "Creta", 900000, "Petrol")
# c2.display()
# c2.check_price()


# """output:--
# Brand: Toyota
# Model: Fortuner
# Price: 4500000
# Fuel Type: Diesel
# car range: Premium Car
# Brand: Hyundai
# Model: Creta
# Price: 900000
# Fuel Type: Petrol
# car range: Normal Car"""


# #==========================================================================================
# """Level 3 – Multiple Methods """

# """11. Electricity Bill 
# Create a class ElectricityBill with: 
# • customer_name  
# • units  
# Create a method calculate_bill(). 
# Use: 
# Units <= 100 → ₹2/unit   
# 101–200  → ₹3/unit        
# 201–300  → ₹5/unit     
# Above 300  → ₹7/unit       
# Create another method display_bill()."""

# class ElectricityBill:
#     def __init__(self,customer_name,units):
#         self.customer_name=customer_name
#         self.units=units

#     def calculate_bill(self):
#         if self.units <= 100:
#             bill = self.units * 2
#         elif self.units <= 200:
#             bill = self.units * 3
#         elif self.units <= 300:
#             bill = self.units * 5
#         else:
#             bill = self.units * 7
#         print("total_bill:",bill)
        

#     def display(self):
#         print("customer name:",self.customer_name)
#         print("Total units:",self.units)
        


# e1=ElectricityBill("ramu",90)
# e1.display()
# e1.calculate_bill()

# """o/p:--
# customer name: ramu
# Total units: 90
# total_bill: 180"""


# #==========================================================================================

# """12. Library Book 
# Create a class Book with: 
# • title  
# • author  
# • price  
# • available  
# Create methods: 
# • display_book()  
# • borrow_book()  
# • return_book()  
# When a book is borrowed, change availability to False."""

# class Book:
#     def __init__(self,title,author,price,available):
#         self.title=title
#         self.author=author
#         self.price=price
#         self.available=available

#     def display_book(self):
#         print("Book Title:",self.title)
#         print("Auther Name:",self.author)
#         print("Price:",self.price)
#         print("availability:",self.available)
        

#     def borrow_book(self):
#         if self.available==True:
#             self.available=False
#             print("book was soldout")
#         else:
#             print("book is not avalable",self.title)
            

#     def return_book(self):
#         if self.available == False:
#             self.available = True
#             print("Book returned successfully")
#         else:
#             print("Book is already available")
            


# book1=Book("Python Basics", "Guido", 500, True)
# book1.display_book()
# """
# Book Title: Python Basics
# Auther Name: Guido
# Price: 500
# availability: True"""
# book1.borrow_book()
# """book was soldout"""

# book1.display_book()
# """Book Title: Python Basics
# Auther Name: Guido
# Price: 500
# availability: False"""

# book1.return_book()
# """Book returned successfully
# """
# book1.display_book()
# """Book Title: Python Basics
# Auther Name: Guido
# Price: 500
# availability: True"""


# #==========================================================================================
# """
# 13. Shopping Cart 
# Create a class Product with: 
# • name  
# • price  
# • quantity  
# Create methods: 
# • calculate_total()  
# • display_product()  
# Create 3 product objects and calculate the total shopping amount. """

# class Product:
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity

#     def calculate_total(self):
#         return self.price * self.quantity

#     def display_product(self):
#         print("Product Name:", self.name)
#         print("Price:", self.price)
#         print("Quantity:", self.quantity)
#         print("Total:", self.calculate_total())
#         print()

# p1 = Product("Laptop", 50000, 1)
# p2 = Product("Mouse", 500, 2)
# p3 = Product("Keyboard", 1000, 1)

# p1.display_product()
# p2.display_product()
# p3.display_product()
# total_amount = (p1.calculate_total()+ p2.calculate_total()+ p3.calculate_total())
# print("Total Shopping Amount:", total_amount)

# """o/p:
# Product Name: Laptop
# Price: 50000
# Quantity: 1
# Total: 50000

# Product Name: Mouse
# Price: 500
# Quantity: 2
# Total: 1000

# Product Name: Keyboard
# Price: 1000
# Quantity: 1
# Total: 1000

# Total Shopping Amount: 52000"""

# #==========================================================================================
# """14. Employee Performance 
# Create a class Employee with: 
# • name  
# • salary  
# • rating  
# Create methods: 
# • display()  
# • calculate_increment() 
# Rules: 
# rating >= 4.5 → 20% increment 
# rating >= 3.5 → 10% increment 
# rating < 3.5  → 5% increment """

class Employee:
    def __init__(self,name,salary,rating):
        self.name=name
        self.salary=salary
        self.rating=rating

    def display(self):
        print("NAME:",self.name)
        print("SALARY:",self.salary)
        print("RATING:",self.rating)
        print()

    def calculate_increment(self):
        if rating

e1 = Employee("Gnaneshwar", 50000, 4.7)
e1.display()
e1.calculate_increment()



     



# #==========================================================================================
# #==========================================================================================
# #==========================================================================================
# #==========================================================================================
# #==========================================================================================
# #=======================================================================================================================================================================================================##################
# #=======================================================================================================================================================================================================##################
# #===============================================================================================
# ###############################------PILLERS OF OOPS-------#####################################
# #===============================================================================================

# """1. inheritence:--
# structure:=
# class parent:    # parent class or super class
# variable/con/methodcaller
# class child(parent):  # sub class
# var/con/method"""
# ##=====================================================================================
# ###types of inheritence:--
# """1.Single Inheritance"""

# class parent:
#     def father(self):
#         print("2 homes")

# class child(parent):
#     def child(self):
#         print("RE350 bike")

# a=child()
# a.father()
# a.child()

# ##=====================================================================================

# class employee:
#     def __init__(self,emp_id,name,salary):
#         self.emp_id=emp_id
#         self.name=name
#         self.salary=salary

#     def display(self):
#         print(f"emp_id is {self.emp_id} name is {self.name} salary is {self.salary}")

# class manager(employee):
#     def __init__(self, emp_id, name, salary):
#         super().__init__(emp_id, name, salary)
#     def role(self,job):
#         self.job=job
#         print(f"empjob is {self.job}")

# e1=manager(12,"Gnaneswhar",10000)
# e2=manager(13,"Rajeshwar",100001)
# e1.display()
# e2.display()
# e1.role("manager")
# e2.role("manager")

# ##=====================================================================================

# class current_bank_acc:
#     def __init__(self,name,balance):
#         self.name=name
#         self.balance=balance

#     def deposite(self,amount):
#         self.balance+=amount

#     def check_balance(self):
#         print(f"Your balance is {self.balance}")

# class saving_bank_acc(current_bank_acc):
#     def __init__(self, name, balance):
#         super().__init__(name, balance)

#     def interest(self):
#         self.balance+=self.balance*0.05
#         print("interest:",self.balance)

# ac1=saving_bank_acc("Gnaneshwar",20000)
# ac1.deposite(1000)
# ac1.check_balance()
# ac1.interest()

# ##=====================================================================================

# """2.Multiple Inheritance"""
# """3.Multilevel Inheritance"""
# """4.Hierarchical Inheritance"""
# """5.Hybrid Inheritance"""




# """class durgam_family:
#     def __init__(self,surename,name,job):
#         self.surename=surename
#         self.name=name
#         self.job=job

#     def names(durgam_family):
#         def __init__(surename,name,job):
#             super().__init__(surename,name,job)

#         def role(self,place):
#             self.place=place
# """

# class parent:
#     print("abc")






# #===============================================================================================
# #===============================================================================================
# #===============================================================================================
# #===============================================================================================



