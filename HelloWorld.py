from mod import adder
import os
import datetime
import pytz

# First Command (print)
print("Hello")


# ------Variables and Strings----------

word = "HelloWorld"
print(len(word))
print(word.count("l"))
print(word.find("l"))
# Slicing
print(word[0:7])
# Show last letter
print(word[-1])
# Replacement
new_message = word.replace('Hello', "Zohaib's ")
print(new_message)

# String Concatination
first_word = 'Hello'
sec_word = "there"

# first method
mess = first_word + ' ' + sec_word
print(mess)

# second method
mess = "{} {}, Zohaib!".format(first_word, sec_word)
print(mess)

# third method
mess = f"{first_word} {sec_word}, Zohaib!"
print(mess)

# -----------Arithmatic Operations---------------
num = 3.14
print(num)
print(type(num))
print(round(num))

# ----------List, Tuples & Sets---------------
#                         ___List____
subjects = ["English", "Urdu", "Mathematics", "Biology"]
new_list = ["Physics", "Chemistry"]

print(subjects) # prints all
print(subjects[0:2]) # prints selected ones
subjects.append("Arts") # add to end
print(subjects)
subjects.insert(2, "Arts") # adds at specified location
print(subjects)
subjects.append(new_list) # adds list as it is (whole list is treated as a single index value)
print(subjects)
subjects.extend(new_list) # adds list as extension
print(subjects)
subjects.pop() # removes last index value
print(subjects)
subjects.remove("Arts") # removes desired value from first place it finds it
print(subjects)

num_list = [3, 5, 8, 9, 4, 7, 3, 2, 6, 0, 0, 7]
print(num_list)
print(num_list[::2]) # makes jumps
num_list.reverse() # reversing the list
print(num_list)
num_list.sort() # sorting the list in ascending
print(num_list)
num_list.sort(reverse=True) # sorting the list in descending
print(num_list)

for i in new_list:
    print(i)

for index, course in enumerate(new_list, 1):  # 1 makes the index start from 1
    print(index, course)

course_string = ', '.join(new_list) # convert list to string
print(course_string)

new_mess = mess.split(",") # converts string to list by splitting it
print(new_mess)

#                       ___Tuple___
#  they are immutable
tuple1 = ('a', 'b', 'c', 'd')
tuple2 = tuple1
print(tuple1)
print(tuple2)

#                        ___Sets___
# they are unordered without duplicates
set1 = {2, 3, 3, 5, 6, 7} # second 3 will not be printed
print(set1)
set2 = {2, 5, 6, 8}
print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))
"""
In sets, the difference between "remove" and "discard" is that remove will give error 
if a certain value is not in set and is wanted to be removed. On the other 
hand, discard will not give error and will simply return the set. 

If you want to  check difference between two sets, difference method is used.
but if you want to consecutively check difference between 3 or more sets, then use symmetric_difference method. 
"""



# ------------Dictionary-----------
student = {'name': "Zohaib",
           'age': 21,
           'courses': new_list}
print(student)
student['phone'] = '111-123-123'
for key, val in student.items():
    print(key, val)

del student['age']
print(student)

student.update({'name': "Zoha"})
print(student)

# ------------------------Conditionals-------------------------
age = 21
if age > 18:
    print("Permission Granted")
elif age == 18:
    print("Request Sent")
else:
    print("Access Denied")

# --------------------------Loops-------------------------------
for i in subjects:
    print(i)

x = 2
while x > 0:
    print(x)
    x -= 1

# ---------------------------Functions------------------------


def add(val1, val2):
    return val1 + val2


print(add(1, 3))


def function(*args, **kwargs):
    print(args)
    print(kwargs)


function('English', name='zohaib', age=21)

print(adder(2, 6))
print(os.__file__)

# ------------------------Comprehension-------------------------
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_list = [n for n in num if n % 2 == 0]
print(my_list)

my_list = [(i, j) for i in 'abcd' for j in range(4)]
print(my_list)

names = ['Bruce', 'Clark', 'Tony', 'Logan']
heroes = ['Batman', 'Superman', 'Iron Man', 'Wolverine']
my_dict = {name: hero for name, hero in zip(names, heroes)}  # Dictionary Comprehension
print(my_dict)

new_set = {n for n in num}   # Set Comprehension
print(new_set)

my_gen = (n*n for n in num)   # Generator Expression
for i in my_gen:
    print(i)

# Sorting List/Tuple/Set
tuple_new = {5,3,7,3,6,2,7,4,7,8,0}
sorted_tuple_new = sorted(tuple_new)
print(sorted_tuple_new)

# Sorting Objects
# for objects, we create custom sort functions

# ------------------------String Formatting----------------------
sentence = '1 MB is equal to {:,.2f} bytes'.format(1000**2)
print(sentence)

# ------------------------OS Library---------------------------
print(os.getcwd())
print(os.listdir())


# -------------------------DateTime------------------------------
dt_now = datetime.datetime.now(tz=pytz.UTC)
print(dt_now)

dt_pk = dt_now.astimezone(pytz.timezone('ASIA/Karachi'))
print(dt_pk)

# for tz in pytz.all_timezones:
#     print(tz)

