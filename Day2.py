import random
import csv
from collections import namedtuple
import json
from contextlib import contextmanager

# ------------------------File Objects--------------------------
# Read
with open('text.txt', 'r') as f:
    print(f.name)
    size = 10
    content = f.read(size)
    print(content, end='*')

    f.seek(15)          # makes the file go to specific point
    content = f.read(size)
    print(content, end='*')

# Write
with open("test.txt", 'w') as f:     # "w" will override whatever is written in file
    f.write("Test2")
    f.seek(0)     # "Seek" in write will override character-wise for instance Test2 overwritten by R will become Rest2.
    f.write("R")

with open("test.txt", 'a') as f:     # "a" will append to whatever is written in file
    f.write("Test3")

# *********Note*************
""" To read and write binary files, we use rb and wb """

print("\n")
# -------------------------Random Module-----------------------------
# Russian Roulette
number = random.randint(1, 6)
print(number)

num = random.uniform(1, 10)      # Gets Float
print(num)

# -------------------------CSV Module-------------------------------
# Read
with open('Test.csv',  "r") as csv_file:
    reader = csv.reader(csv_file)
    for line in reader:
        id, title, genre = line
        print(id)

# Write
with open('Test.csv',  "r") as csv_file:
    reader = csv.reader(csv_file)
    with open('new.csv',  "w") as new_file:
        writer = csv.writer(new_file)
        for line in reader:
            writer.writerow(line)

# ------------------------Regex---------------------------------
"""
you can use regex101.com or "re" library of python to work with regular expressions.  
They can be used to clean data, extract info and validate data, emails for example.
"""

# ------------------------Exception Handling--------------------
try:
    f = open("testfile.txt", "r")
except Exception:
    print("File Not Found")
else:
    print(f.read())
finally:
    f.close()


# -------------------------Generators-------------------------
"""
Generators are python functions that generate iterable objects.
They use "yield" keyword instead of "return". Generators provide a space-efficient 
method for such data processing as only parts of the file are handled at one given point in time
They yield object which is read using loop.
"""

# -------------------------NameTuple-----------------------------
"""
Namedtuple is sort of something between a regular tuple and a dictionary. 
It tells us what a value represents(Dictionary) and is immutable(Tuple)
"""

Color = namedtuple('Color', ['red', 'green', 'blue'])
color = Color(239, 233, 65)
print(color.blue)


# --------------------------Decorators--------------------------------
def decor(func):
    def wrapper(*args, **kwargs):
        print("Inside Wrapper Function")
        my_func = func(*args, **kwargs)
        print("After the function call")
        print(my_func)
    return wrapper


@decor
def adder(val1, val2):
    print("Inside Adder")
    return val1 + val2


adder(4, 6)
# ----------------------------Classes--------------------------------


class Employee:
    def __init__(self, fn, ln, pay):
        self.first_name = fn
        self.last_name = ln
        self.pay = pay

    @property
    def email(self):
        return f'{self.first_name}.{self.last_name}@company.com'.lower()

    def work(self):
        print(f"{self.first_name} is working.")

    def details(self):
        print(f'Name: {self.first_name} {self.last_name} \nPay: {self.pay} \nEmail: {self.email}')


e1 = Employee("Zohaib", "Khan", 250000)
e1.email
e1.work()
e1.details()


class Engineer(Employee):
    def __init__(self, fn, ln, pay, lang):
        super().__init__(fn, ln, pay)
        self.prog_lang = lang

    def details(self):
        Employee.details(self)
        print(f"Language: {self.prog_lang}")


eng1 = Engineer("Zohaib", "Khan", 250000, "Python")
eng1.details()


# *****  Dunder Method *****
"""
Methods which start and end with __ e.g., __init__  etc., are the dunder methods.
"__repr__" method is used to show an object to developer instead of showing object 
created at memory location. It has to be overwritten. Its goal is to be unambiguous.
"__str__" method is used to show an object to user instead of showing object 
created at memory location. It has to be overwritten. Its goal is to be readable.
Function override like that of __add__, __sub__ etc, is also done to add subtract etc the objects
"""

print(e1.first_name)
print(e1.email)
e1.first_name = "Ali"
print(e1.first_name)
print(e1.email)

# ----------------------Working With JSON-------------------------
# From same FIle
x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann", "Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

data = json.dumps(x)    # will give a string
real_data = json.loads(data)    # will give a dictionary
print(real_data["name"])

# From Different File
with open("test.json") as f:
    data = json.load(f)
for car in data['cars']:
    print(car)

# ------------------------Context Manager------------------------


@contextmanager
def open_file(file, mode):
    f = open(file, mode)
    yield f
    f.close()


# ------------------------Else in Loop-------------------------------------
num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in num:
    print(i)
else:
    print("List has ended!")
