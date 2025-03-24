
"filse i/o"

# openind file and closeing file
# f = open("/home/jtd/Desktop/test.py", "r")
# data = f.read()
# print(data)
# print(type(data))
# f.close()


# line by line reading
# f = open("/home/jtd/Desktop/test.py", "r")
# data = f.read()
# print(data)

# line1 = f.readline()
# print(line1)

# line2 = f.readline()
# print(line2)

# f.close()

# "writing to a file"
# f = open("/home/jtd/Desktop/test.txt", "w")
# f.write("this is a nwe line. 123")
# f.close()

# f = open("/home/jtd/Desktop/test.py", "a")
# f.write("anjum is ms big fan")
# f.close()



 



# 1
# class student:
#     name = "anjum"

# s1 = student()
# print(s1.name)

# s2 = student()
# print(s1.name)

# 1.2
# class student:
#     college = "ABC"
#     name = " anonymuos"
#     def __init__(self,name,marks):
#         self.name = name 
#         self.marks = marks
#         print("add nwe ")
# s1 = student("karan",77)
# print(s1.name)

# 2
# class book:
#     def _init_(self,title,author,price):
#         self.title=title
#         self.author=author
#         self.price=price
#     def BOOKS(self):
#           print(self.title,self.author,self.price)
# book1=book("chandamama","rama",45)
# book2=book("kathala pusthakam","rani",55)
# book3=book("bala bharathi","rama",55)

# book1.BOOKS()
# book2.BOOKS()
# book3.BOOKS()

# 3
# class car:
#     def __init__(self,brand,price):
#         self.brand=brand
#         self.price=price
#     def CAR(self):
#         print(self.brand,self.price) 
# car1=car("bmw",30000000)
# car2=car("handya",45000000)

# car1.CAR()
# car2.CAR()

# 4
# class family:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def FAMILY(self):
#         print(self.name,self.age)
# name1=family("amar",40)
# name2=family("shabana",38)
# name3=family("musfira",17)
# name4=family("marziya",16)
# name5=family("madiha",12)

# name1.FAMILY()
# name2.FAMILY()
# name3.FAMILY()
# name4.FAMILY()
# name5.FAMILY()

# 5
# class student:
#     a="anjum"
#     def __init__(self,a1,a2):
#         self.a1 =a1
#         self.a2= a2
#     def disply(self):
#         print(self.a1,self.a2)
# a1 = student("marziya",16)
# a2 = student("madiha",12)

# a1.disply()
# a2.disply()

# Parent Class
# class Animal:
#     def sound(self):
#         print("Animals make sound")

# # Child Class
# class Dog(Animal):
#     def sound(self):
#         super().sound()  # Call Parent Method
#         print("Dog barks")

# # Create Object
# dog = Dog()
# dog.sound()


# class student:
#     csk = "msd"
#     def __init__(self,name,mark):
#         self.name = name 
#         self.mark = mark
#         print("csk won the macth")
# s1 = student("mahi",7)
# # s1.name = "dhoni"
# print(s1.name)


# class tata:
#     ipl = "cirkate"
#     def __init__(self,teamA1,teamA2,teamB1,teamB2):
#         self.teamA1 = teamA1
#         self.teamA2 = teamA2
#         self.teamB1 = teamB1
#         self.teamB2 = teamB2
#     print("ipl is back")
#     def myteamA(self):
#         print("teamA",self.teamA1,self.teamA2,self.teamB1,self.teamB2)
#     def myteamB(self):
#         print("teamB",self.teamA1,self.teamA2,self.teamB1,self.teamB2)

# s1 = tata("csk",7,7,7)
# s1.myteamA()
# s2 = tata("mi",45,63,33)
# s2.myteamA()
# s3 = tata("gt",77,77,77)
# s3.myteamA()

# m1 = tata("rr",3,31,69)
# m1.myteamB()
# m2 = tata("rcb",18,81,88)
# m2.myteamB()
# m3 = tata("srh",65,25,23)
# m3.myteamB()


# class tata:
#     ipl = "cirkate"
#     def __init__(self,teamA1,teamA2,teamB1,teamB2):
#         self.teamA1 = teamA1
#         self.teamA2 = teamA2
#         self.teamB1 = teamB1
#         self.teamB2 = teamB2
#     # print("ipl is back")
#     def myteamA(self):
#         print("teamA",self.teamA1,self.teamA2)
#     def myteamB(self):
#         print("teamB",self.teamB1,self.teamB2)

# s1 = tata("csk",7,7,7)
# s1.myteamA()
# s2 = tata("mi",45,63,33)
# s2.myteamA()
# s3 = tata("gt",77,77,77)
# s3.myteamA()

# m1 = tata(31,69,"rr",3)
# m1.myteamB()
# m2 = tata(81,88,"rcb",18)
# m2.myteamB()
# m3 = tata(25,23,"srh",65)
# m3.myteamB()
"3"
# class calculas:
#     defal = "abcd"
#     def add(self,a,b):
#         return a+b
#     def sub(self,a,b):
#         return a-b
#     def mul(self,a,b):
#         return a*b
#     def div(self,a,b):
#         return a/b
# tali = calculas()
# print(tali.add(6,7))
# print(tali.sub(6,7))
# print(tali.mul(6,7))
# print(tali.div(6,7))  
"2"
# Juiceshop
# class Juiceshop:
#     def __init__(self, juice_price=25):
#         self.juice_price = juice_price

#     def buy_juice(self, amount):
#         if amount == self.juice_price:
#             print("Take your juice 🍹")
#         elif amount < self.juice_price:
#             print("This money is not sufficient.")
#         else:
#             change = amount - self.juice_price
#             print(f"This is your change: {change}")
#             print("Take your juice 🍹")
# # Creating an object of the class
# machine = Juiceshop()
# # Taking input from the user
# amount = int(input("Enter an amount: "))
# machine.buy_juice(amount)
"1"
# finding area of diffrent shapes,
# class Areas:
#     def squre(self,l):
#         return l*l
#     def rectangel(self,s,b):
#         return s*b
#     def circle(self,r,p):
#         return 2*(r*p)
# a = Areas()
# print(a.squre(4))
# print(a.rectangel(3,4))
# print(a.circle(3.14,2))
"vegtabel"
# class veg:
#     def __init__(self):
#         pass
#     def name(self,n):
#         return n
#     def pri(self,a):
#         return 30*a
# z=veg()
# print(z.name("bringal"))
# print(z.pri(3))
"Vegetable"
# class Vegetable:
#     def __init__(self,veg_name,price_per_kg):
#         self.veg_name = veg_name
#         self.price_per_kg = price_per_kg
#     def number_of_kg(self,number):
#         self.price_per_kg *= number
#     def display(self):
#         print(self.veg_name,self.price_per_kg)
# obj = Vegetable("carrot",30)
# obj.number_of_kg(3)
# obj.display()
"book shop"
# class Book:
#     def __init__(self, title, author, price):
#         self.title = title
#         self.author = author
#         self.price = price

#     def discount(self, percentage):
#         self.price -= self.price * (percentage / 100)
#     def display(self):
#         print(f"Book: {self.title}, Author: {self.author}, Price: {self.price}")

# b1 = Book("Python Basics", "John Doe", 500)
# b1.discount(10)
# b1.display()

# "BANK"
# class BankAccount:
#     def __init__(self, account_holder, balance=0):
#         self.account_holder = account_holder
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance += amount
#         print(f"{amount} deposited. New Balance: {self.balance}")

#     def withdraw(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#             print(f"{amount} withdrawn. New Balance: {self.balance}")
#         else:
#             print("Insufficient balance!")

# # Example
# acc = BankAccount("Musfira", 1000)
# acc.deposit(500)
# acc.withdraw(300)
# acc.withdraw(1500)
# "students grade"
# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def calculate_grade(self):
#         average = sum(self.marks) / len(self.marks)
#         if average >= 90:
#             return "A"
#         elif average >= 75:
#             return "B"
#         elif average >= 60:
#             return "C"
#         else:
#             return "F"
#     def display(self):
#         print(f"Student: {self.name}, Grade: {self.calculate_grade()}")

# # Example
# s1 = Student("Ali", [85, 90, 78])
# s2 = Student("Sara", [55, 60, 58])
# s1.display()
# s2.display()
# "car managment"
# class Car:
#     def __init__(self, brand, model, year):
#         self.brand = brand
#         self.model = model
#         self.year = year

#     def display(self):
#         print(f"Car: {self.year} {self.brand} {self.model}")
# # Example
# car1 = Car("Toyota", "Camry", 2022)
# car2 = Car("Honda", "Civic", 2021)
# car1.display()
# car2.display()
