"""1. Create a Student class with attributes name, age, and marks.
Create an object and display all the details.

class student:
    def __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self.marks=marks

    def display(self):
        print("name:",self.name)
        print("age:",self.age)
        print("marks:",self.marks)
s1=student("gnaneshwar",23,"45")
s1.display()

o/p:
name: gnaneshwar
age: 23
marks: 45


2. Create a Car class with attributes brand and model.
Create two objects with different values and display their details.

class car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
        print("brand:",self.brand)
        print("modek:",self.model)

c1=car("SUZUKI","swift")
c2=car("HUNDAI","i20")

o/p:
brand: SUZUKI
modek: swift
brand: HUNDAI
modek: i20


3. Create a Calculator class with methods add(), subtract(), multiply(), and divide().
Take two numbers from the user and perform all operations.

class calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def add(self):
        print("add:",self.a+self.b)

    def subtract(self):
        print("subtract:",self.a-self.b)

    def multiply(self):
        print("multiply:",self.a*self.b)

    def divide(self):
        print("divide:",self.a/self.b)

c1=calculator(10,5)
# c2=calculator(8,6)
# c3=calculator(9,2)
c1.add()
c1.subtract()
c1.multiply()
c1.divide()


o/p:
add: 15
subtract: 5
multiply: 50
divide: 2.0


4. Create a Rectangle class with attributes length and breadth.
Create methods area() and perimeter().

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

o/p:
Area: 80
Perimeter: 36

5. Create an Employee class with attributes name, salary, and department.
Create a method display_details() to print the employee information.

class Employee:
    def __init__(self,name,salary,department):
        self.name=name
        self.salary=salary
        self.department=department

    def display_details(self):
        print("Name:",self.name)
        print("Salary:",self.salary)
        print("Department:",self.department)

e1=Employee("Gnaneshwar",45000,"IT")
e1.display_details()

o/p:
Name: Gnaneshwar
Salary: 45000
Department: IT

6. Create a BankAccount class with an initial balance.
Create methods deposit() and withdraw(). Display the updated balance after each operation.

class BankAccount:
    def __init__(self,initial_balance):
        self.initial_balance=initial_balance

    def deposite(self,amount):
        self.initial_balance+=amount
        print("Deposit amount:", amount)
        print("Availabale Balance:",self.initial_balance)

    def withdraw(self,amount):
        if self.initial_balance>=amount:
            self.initial_balance -= amount
            print("withdraw amount:",amount)
            print("Availabale Balance:",self.initial_balance)
        else:
            print("Insufficient Balance")

b1=BankAccount(50000)
b1.deposite(500)
b1.withdraw(5100)

o/p:
Deposit amount: 500
Availabale Balance: 50500
withdraw amount: 5100
Availabale Balance: 45400

7. Create a Student class with a method calculate_grade() that returns:
90–100 → A
75–89 → B
60–74 → C
40–59 → D
Below 40 → F

class Student:
    def __init__(self, marks):
        self.marks = marks

    def calculate_grade(self):
        grades = [
            (90, "A"),
            (75, "B"),
            (60, "C"),
            (40, "D"),
            (0, "F")
        ]

        for marks, grade in grades:
            if self.marks >= marks:
                print("Grade:", grade)
                print("Marks:", self.marks)
                break

s1 = Student(50)
s1.calculate_grade()

o/p:
Grade: D
Marks: 50


8. Create a Person class with a method introduce() that prints the person's name, age, and city.
Create three different objects and call the method for each.

class person:
    def __init__(self,name, age,city):
        self.name=name
        self.age=age
        self.city=city

    def introduce(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("City:",self.city)
p1=person("Gnaneshwar",23,"HYD")
p2=person("Rajeshwari",21,"PDPL")
p1.introduce()
p2.introduce()

o/p:====
Name: Gnaneshwar
Age: 23
City: HYD
Name: Rajeshwari
Age: 21
City: PDPL

9. Create a Product class with attributes name, price, and quantity.
Create a method total_cost() that calculates price × quantity and displays the result.

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_cost(self):
        total = self.price * self.quantity
        print("Product Name:", self.name)
        print("Price:", self.price)
        print("Quantity:", self.quantity)
        print("Total Cost:", total)

p1 = Product("Laptop", 50000, 2)
p1.total_cost()


o/p:====
Product Name: Laptop
Price: 50000
Quantity: 2
Total Cost: 100000"""

