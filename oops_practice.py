
"""Level 1 – Basic
1. Student Details
Create a class Student with:
Variables: name, age, course
Constructor to initialize the variables
Method display() to print student details.
Expected concept: Constructor + instance variables + method"""

""" class student:
    def __init__(self,name,age,course):
        self.name=name
        self.age=age
        self.course=course

    def display(self):
        print("name:",self.name)
        print("age:",self.age)
        print("course:",self.course)
s1=student("gnaneshwar",23,"EEE")
s1.display()"""


"""2. Employee Salary
Create a class Employee with:
name
basic_salary
Create a method display_salary() that prints the employee's salary.
Example:
Name: Aparna
Salary: 30000"""

"""class employee:
    def __init__(self,name,basic_salary):
        self.name=name
        self.basic_salary=basic_salary

    def display(self):
        print("name:",self.name)
        print("salary:",self.basic_salary)

e1=employee("aparna",30000)
e1.display()
"""
""" 3. Bank Account
Create a class BankAccount with:
account_holder
balance
Create methods:
deposit(amount)
withdraw(amount)
display_balance()"""

"""class bank():
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
b1.display_balance()"""




# If the withdrawal amount is greater than the balance, display "Insufficient Balance".

"""4. Mobile Phone
Create a class Mobile with:
brand
model
price
Create a method display() to display all details.
Create objects for 3 different mobiles."""

class mobile_phone:
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price

    def display(self):

    

"""
5. Rectangle Calculation

Create a class Rectangle with:

length
breadth

Create methods:

area()
perimeter()

Use the constructor to initialize length and breadth.

Level 2 – Logic-Based Problems
6. Student Marks

Create a class Student with:

name
marks

Create methods:

display_marks()
check_result()

Rules:

marks >= 40 → Pass
marks < 40 → Fail

Create objects for 5 students.

7. Employee Bonus

Create a class Employee with:

name
salary

Create a method calculate_bonus().

Rules:

salary >= 50000 → 10% bonus
salary < 50000 → 5% bonus

Display:

Employee Name
Salary
Bonus
Total Salary
8. Product Discount

Create a class Product with:

product_name
price

Create a method calculate_discount().

Rules:

price >= 5000 → 20% discount
price >= 2000 → 10% discount
otherwise → 5% discount

Display the final price.

9. ATM Transaction

Create a class ATM with:

account_number
balance

Create methods:

deposit()
withdraw()
check_balance()

The object should maintain the updated balance after every transaction.

10. Car Information

Create a class Car with:

brand
model
price
fuel_type

Create methods:

display()
check_price()

If price is greater than ₹10,00,000, display "Premium Car", otherwise "Normal Car".

Level 3 – Multiple Methods
11. Electricity Bill

Create a class ElectricityBill with:

customer_name
units

Create a method calculate_bill().

Use:

Units <= 100 → ₹2/unit
101–200 → ₹3/unit
201–300 → ₹5/unit
Above 300 → ₹7/unit

Create another method display_bill().

12. Library Book

Create a class Book with:

title
author
price
available

Create methods:

display_book()
borrow_book()
return_book()

When a book is borrowed, change availability to False.

13. Shopping Cart

Create a class Product with:

name
price
quantity

Create methods:

calculate_total()
display_product()

Create 3 product objects and calculate the total shopping amount.

14. Employee Performance

Create a class Employee with:

name
salary
rating

Create methods:

display()
calculate_increment()

Rules:

rating >= 4.5 → 20% increment
rating >= 3.5 → 10% increment
rating < 3.5 → 5% increment
15. Bank Account Validation

Create a class BankAccount with:

account_holder
balance

Create methods:

deposit(amount)
withdraw(amount)
check_balance()

Additional rule:

Minimum balance = ₹1000

A withdrawal should not be allowed if the remaining balance becomes less than ₹1000.

Level 4 – Challenge Problems
16. Online Food Order

Create a class FoodOrder with:

customer_name
food_name
price
quantity

Methods:

calculate_total()
apply_discount()
display_order()

Rules:

Total >= ₹2000 → 20% discount
Total >= ₹1000 → 10% discount
Otherwise → No discount
17. Hospital Patient

Create a class Patient with:

name
age
disease
bill

Methods:

display_patient()
add_bill(amount)
check_bill()

Create multiple patient objects and update their bills.

18. Employee Attendance

Create a class Employee with:

name
total_days
present_days

Methods:

attendance_percentage()
check_attendance()

Rules:

Attendance >= 75% → Eligible
Attendance < 75% → Not Eligible
19. Movie Ticket Booking

Create a class MovieTicket with:

movie_name
ticket_price
number_of_tickets

Methods:

calculate_total()
apply_discount()
display_ticket()

Rules:

Tickets >= 5 → 10% discount
Otherwise → No discount
20. Student Report Card

Create a class Student with:

name
roll_no
python
sql
powerbi

Create methods:

calculate_total()
calculate_average()
calculate_grade()
display_report()

Grade rules:

Average >= 90 → A
Average >= 75 → B
Average >= 60 → C
Average >= 40 → D
Below 40 → Fail"""