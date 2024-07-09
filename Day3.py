import unittest
import mod
import os
from PIL import Image
import pandas as pd
from collections import Counter
import requests


# --------------------------Unit Testing-------------------------

# # Use separate file to do test
# class Calculate(unittest.TestCase):
#     def test_add(self):      # Test method should always start with test e.g., "test_add" etc.
#         result = mod.adder(2, 4)
#         self.assertEquals(result, 6)
#

# -------------------------Image Resizer--------------------------
# img1 = Image.open("Woody Intense.jpg")
# img1.show()

# new_size = (300, 300)
# for f in os.listdir('.'):
#     if f.endswith('.jpg'):
#         i = Image.open(f)
#         fn, fext = os.path.splitext(f)
#         i.thumbnail(new_size)
#         i.save('{}_300.png'.format(fn)) # changes format of file and resizes it

"""
You can also use this library to rotate, blur and make image black and white to name a few things.
"""


# ------------------- Iterables and Iterators-----------------------
"""
Objects with "__iter__" method, i.e., they can be iterated through, are iterables e.g., Lists.
Interator are objects which know how to get their next value. They have "__next__" method. They remember their states
"""

nums = [1, 2, 3] # this is iterable and not iterator
i_nums = iter(nums) # this is iterator as it has ability to store its state and call the next value.
print(dir(nums))
print(dir(i_nums))


def iterator(sen):
    sentence = sen.split()
    index = 0
    while index < (len(sentence)):
        yield sentence[index]
        index += 1


sentence = "Hello I am Zohaib Tahir Khan"
words = iterator(sentence)
print(next(words))
print(next(words))
print(next(words))
print(next(words))
print(next(words))
print(next(words))

print(list(words))

"""
You can also create custom class for iterators which has overwritten __init__, __iter__ and __next__ methods.
"""


# ---------------------------Pandas----------------------------
data = pd.read_csv('Squirrel_Data.csv')
color = data['Primary Fur Color']
color_list = list(color)
print(color_list)
gray = 0
cinnamon = 0
black = 0
for i in color_list:
    if i == 'Gray':
        gray += 1
    elif i == 'Black':
        black += 1
    elif i == 'Cinnamon':
        cinnamon += 1

print(gray)
print(black)
print(cinnamon)

data_dict = {
    "Fur Color": ["Gray", "Black", "Cinnamon"],
    "Count": [gray, black, cinnamon]
}

df = pd.DataFrame(data_dict)
df.to_csv('count.csv')


"""
Further, you can use .loc method to interact with particular value by using column name and index.
Or, you could use .iloc method and use index of column to get column.
You can sort using sort method or using sort_values method.
"""


# -----------------------Request---------------------------------
r = requests.get("https://xkcd.com/")

print(r.text)
print(r.content)
r_post = requests.post("https://xkcd.com/")

print(r_post.text)

"""
To pass arguments, use 'param' in get method and use 'data' in post method.
request module can also be used to download an image, scraping data etc.
"""


print("hello")
