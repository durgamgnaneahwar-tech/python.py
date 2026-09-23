"""Level 1 – Basic """

"""1. Student Details 
Create a class Student 
with: 
• Variables: name, age, course  
• Constructor to initialize the variables  
• Method display() to print student details.  
Expected concept: Constructor + instance variables + method """

class student:
    def __init__(self,name,age,course):
        self.name=name
        self.age=age
        self.course=course

    def display(self):
        print("name:",self.name)
        print("age:",self.age)
        print("course:",self.course)
s1=student("gnaneshwar",23,"EEE")
s1.display()

"""output:-
name: gnaneshwar
age: 23
course: EEE"""

#==========================================================================================

"""2. Employee Salary 
Create a class Employee 
with: 
• name , basic_salary  
Create a method display_salary() that prints the employee's salary. 
Example: Name: Aparna Salary: 30000 """

class employee:
    def __init__(self,name,basic_salary):
        self.name=name
        self.basic_salary=basic_salary

    def display(self):
        print("name:",self.name)
        print("salary:",self.basic_salary)

e1=employee("aparna",30000)
e1.display()

"""output:-
name: aparna
salary: 30000"""


#==========================================================================================


"""3. Bank Account 
Create a class BankAccount 
with
• account_holder  
• balance  
Create methods: 
• deposit(amount)  
• withdraw(amount)  
• display_balance()  
If the withdrawal amount is greater than the balance,display "Insufficient Balance". """

class bank():
    def __init__(self,account_holder,balance):
        self.account_holder=account_holder
        self.balance=balance

    def display_details(self):
        print("acc holder name:",self.account_holder)
        print("Bank balance:",self.balance)

    def deposit(self,amount):
        self.balance+=amount
        print("diposite amount:",amount)

    def withdrawl(self,amount):
        if self.balance>=amount:
            self.balance-=amount
            print("withdrawl amount:",amount)
            print("available balance:",self.balance)
        else:
            print("Insufficient Balance:" "ERROR")

    def display_balance(self):
        print("Balance:",self.balance)

b1=bank("Gnaneshwar",500000)
b1.display_details()
b1.deposit(5000)
b1.withdrawl(600000)
b1.display_balance()

"""output:-
acc holder name: Gnaneshwar
Bank balance: 500000
diposite amount: 5000
Insufficient Balance:ERROR
Balance: 505000"""


#==========================================================================================


"""4. Mobile Phone
Create a class Mobile 
with: 
• brand  
• model  
• price  
Create a method 
display() 
to display all details.
Create objects for 3 different mobiles."""

class mobile:
    def __init__(self,brand,model,price ):
        self.brand=brand
        self.model=model
        self.price=price

    def display(self):
        print("Mobile Brand:",self.brand)
        print("Mobile Model:",self.model)
        print("Mobile Price:",self.price)

m1=mobile("samsung","S 25 ULTRA",155000)
m2 = mobile("Apple", "iPhone 17", 120000)
m3 = mobile("OnePlus", "13", 70000)

m1.display()
m2.display()
m3.display()


"""outputs:=
Mobile Brand: samsung
Mobile Model: S 25 ULTRA
Mobile Price: 155000

Mobile Brand: Apple
Mobile Model: iPhone 17
Mobile Price: 120000

Mobile Brand: OnePlus
Mobile Model: 13
Mobile Price: 70000"""


#==========================================================================================


"""5. Rectangle Calculation
Create a class Rectangle 
with: 
• length  
• breadth  
Create methods:
• area() 
• perimeter()  
Use the constructor to initialize length and breadth."""


class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        a = self.length * self.breadth
        print("Area:", a)

    def perimeter(self):
        perimeter = 2 * (self.length + self.breadth)
        print("Perimeter:", perimeter)

r1 = Rectangle(10, 8)
r1.area()
r1.perimeter()

"""o/p:
Area: 80
Perimeter: 36"""

#==========================================================================================


"""Level 2 – Logic-Based Problems"""
"""6. Student Marks 
Create a class Student 
with:
• name
• marks  
Create methods:
• display_marks()  
• check_result()  
Rules: 
marks >= 40 → Pass 
marks < 40  → Fail 
Create objects for 5 students. """

class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def display_marks(self):
        print("Student Name:",self.name)
        print("MARKS:",self.marks)

    def check_result(self):
        if self.marks>= 40:
            result="PASS"
        else:
            result="FAIL"
        print(result)

s1 = Student("Rahul", 49)
s2 = Student("Sneha", 39)
s3 = Student("Kiran", 75)
s4 = Student("Priya", 35)
s5 = Student("Arjun", 50)

s1.display_marks()
s1.check_result()

s2.display_marks()
s2.check_result()

s3.display_marks()
s3.check_result()

s4.display_marks()
s4.check_result()

s5.display_marks()
s5.check_result()

"""output:--
Student Name: Rahul
MARKS: 49
PASS

Student Name: Sneha
MARKS: 39
FAIL

Student Name: Kiran
MARKS: 75
PASS

Student Name: Priya
MARKS: 35
FAIL

Student Name: Arjun
MARKS: 50
PASS"""

#==========================================================================================

"""7. Employee Bonus 
Create a class Employee 
with:
• name
• salary
Create a method 
calculate_bonus(). 
Rules: 
salary >= 50000 → 10% bonus 
salary < 50000  → 5% bonus 
Display: Employee Name Salary Bonus Total Salary """

class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

        print("Employee name:",self.name)
        print("Salary:",self.salary)

    def calculate_bonus(self):
        if self.salary>= 50000:
            bonus=self.salary*0.10
        else:
            bonus=self.salary*0.05
        Total_Salary=self.salary+bonus

        print("Bonus:",bonus)
        print("Total Salary:",Total_Salary)

e1=Employee("Gnaneswhar",55000)
e1.calculate_bonus()

"""output:--
Employee name: Gnaneswhar
Salary: 55000
Bonus: 5500.0
Total Salary: 60500.0"""

#==========================================================================================

"""8. Product Discount
Create a class Product 
with:
• product_name
• price  
Create a method 
calculate_discount(). 
Rules: 
price >= 5000 → 20% discount
price >= 2000 → 10% discount
otherwise → 5% discount 
Display the final price. """

class Product:
    def __init__(self,product_name,price):
        self.product_name=product_name
        self.price=price

    def calculate_discount(self):
        if self.price >= 5000:
            discount=self.price*0.20
        elif self.price>= 2000:
            discount=self.price*0.10
        else:
            discount=self.price*0.05
        total = self.price - discount
        print("Product:",self.product_name)
        print("Final price:",total)

p1 = Product("Headphones", 3000)
p2 = Product("Keyboard", 1500)

p1.calculate_discount()
p2.calculate_discount()

"""output:--
Product: Headphones
Final price: 2700.0

Product: Keyboard
Final price: 1425.0"""

#==========================================================================================

"""9. ATM Transaction 
Create a class ATM 
with:
• account_number
• balance  
Create methods: 
• deposit()
• withdraw()
• check_balance()  
The object should maintain the updated balance after every transaction."""

class ATM:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
        print("Balance:", self.balance)

    def deposit(self, amount):
        self.balance += amount
        print("Deposit Amount:", amount)
        print("Balance:", self.balance)

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print("Withdraw:", amount)
            print("Balance:", self.balance)
        else:
            print("Insufficient Balance")

    def check_balance(self):
        print("Updated Balance:", self.balance)

a1 = ATM(963852741, 15000)
a1.deposit(5000)
a1.withdraw(2000)
a1.check_balance()  

"""output:--
Balance: 15000
Deposit Amount: 5000
Balance: 20000
Withdraw: 2000
Balance: 18000
Updated Balance: 18000"""

#==========================================================================================

"""10. Car Information 
Create a class Car
with:
• brand
• model
• price
• fuel_type 
Create methods:
• display()
• check_price()  
If price is greater than ₹10,00,000, display "Premium Car",
otherwise "Normal Car"."""

class car:
    def __init__(self,brand,model,price,fuel_type):
        self.brand=brand
        self.model=model
        self.price=price
        self.fuel_type=fuel_type

c1 = car("Toyota", "Fortuner", 4500000, "Diesel")
c2 = car("Hyundai", "Creta", 900000, "Petrol")




#==========================================================================================
#==========================================================================================
#==========================================================================================
#==========================================================================================
#==========================================================================================
#==========================================================================================
#==========================================================================================
#==========================================================================================
#==========================================================================================
#==========================================================================================
#==========================================================================================
#==========================================================================================
#==========================================================================================
#==========================================================================================
#==========================================================================================
#==========================================================================================









