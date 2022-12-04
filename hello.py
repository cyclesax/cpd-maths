# Part 1: 18 November (there are later parts in this document)
# ============================================================ 

# camelcase was installed with pip ... but has some old fashioned structure warning
# camecase was installed in a system folder ... a different one in VS to terminal
# there are multiple versions existing at the same time ... so pip command may need
# to be done like python3 -m pip install camelcase, not pip install camelcase.
import camelcase

# camelcase is a module and CamelCase is a class ... so c is an instance of the class
c = camelcase.CamelCase()

txt = "hello world should be processed with camelcase"
# hump() is a method of the class
print(c.hump(txt))

# import does not have to be at the top of the page
# math is a standard package
import math
x = math.sqrt(64)
print(x)

# fruits is an "list" of strings.
fruits = ["apple", "cherry", "banana"]
# simple for operates over items in a list
for x in fruits:
    # loop must be indented
    print(x)
    # there is no terminator of the loop ... it indentation

# print statements can have multiple items
# len() is function to get the size of a list
print('length of list %d' % len(fruits))

# mymodule is a file in this folder
import mymodule
mymodule.greeting('Dan')

# python dictionary is a map in other languages.
# create an empty map is easy ... yes, I've used the wrong name here, should be dict
mymap = {}
mymap["Dan"] = 100
mymap["Rob"] = 13

# print can dump a whole map to the console
print(mymap)

if 'Sue' in mymap:
    print('Sue is in the map')
else:
    print('Sue is MISSING!')

# can we change the type of value in the map?
mymap["Rob"] = 'Thirteen'
print(mymap)
# yes, we can. so the values are heterogeneous types

# do the keys support heterogeneous types too?
mymap[14] = 'Retirement company'
print(mymap)
# yes, they do

# how to add an item to a list?
fruits.append("treacle tart")
print(fruits)

# can we remove an items from the list
fruits.remove("apple")
print(fruits)

# can we force a value into a list at a specific location (existing) ie replace
fruits[2] = "Peppers"
# yes, we can.  But we can't use this technique in place of append
# and it is zero-based like most normal languages except Lua and APL and a few others.

# can we add a number to it?
fruits.append(99)
print(fruits)
# yes, these are also heterogeneous

# arrays are homogeneous
import array
myarray = array.array('i', [1,2,3])
# myarray.append('cake') would break
# adding another item is ok, as arrays are dynamic in size
myarray.append(99)
# easy to adjust a specific element
myarray[0] = 13
# print can print arrays with no trouble
print(myarray)

# write to a file
f = open("demofile.txt", "w")
# write does not end the line, so strings append
f.write("Replace any existing contents of file with this string")
f.write(" ... And another string")
# so we need to explicitly have new line characters 
f.write('\n')
# to get us onto the next line
f.write('And then this will appear on a new line')
f.close()

# open and read the file
f = open("demofile.txt", "r")
print(f.read())

# perhaps there is more modern style of Python to use?
mylines = []
with open("demofile.txt") as file:
    while (line := file.readline().rstrip()):
        mylines.append(line)

print(mylines)

# This is how we do a simple loop
for i in range(3):
    print(i)

# Part 2: 19 November (looking at simple w3schools.com Python Tutorial)
# =====================================================================

# Conversion between types in Python is known as casting and this looks like
# it is using a fuction call (in syntax and probably in practice too)
x = str(3) # converts from a number to a string
y = int(3) # this might not do anything different to y = 3
z = float(3) # this creates a float of 3.0 ... SO, floats are different
print(z)

# Variable names can start with _ but not numbers and cannot have spaces
# so Python variables are pretty much like other languages

# Shorthand allocation to multiple variables is allowed on one line, saving space
x,y,z = 1,2,3

# And we can allocate the same variable on one line
x = y = z = 13

# And we can unpack lists, but need to match number of variables to length
# or a runtime error will occur
print(fruits)
x,y,z,z2 = fruits

# We can catch runtime exceptions with try/catch as in other languages
try:
    x,y = fruits # this will fail, because of mismatch of count of items
except:
    print('caught an exception assigning wrong number/size')

# Concatenation of strings is ok
s = 'Bakewell' + ' puddings'
print(s)

# But you can't concatenate strings and numbers ... no automated conversion
# as there is in many JavaScript equivalents
try:
    s = 'Liverpool 3: Arsenal: ' + 1
except:
    s = 'Liverpool 3: Arsenal: ' + str(1)
print(s)

# All of the code in this file so far is just global, not in a function
# and all the variables are global variables
# Let's define a function here (we've already defined one in a separate file)
# and then we can see how local and global variables operate

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x) # this will print 'Python is fantastic'

myfunc()

print("Python is " + x) # this will print 'Python is awesome'

# there's no problem with the code in this file ... it is just bad practice
# to have something as simple as this as we can't reuse it and it is not
# structured ... we'll address those points later.

# Data types in Python are: 
# Text:	        str
# Numeric:	    int, float, complex
# Sequence:	    list, tuple, range
# Mapping :	    dict
# Set:	        set, frozenset
# Boolean:	    bool
# Binary:	    bytes, bytearray, memoryview
# None:         NoneType

# We've looked at some of these types already. Let's have a look at a few more
# now.

# a "set" has different types of brackets {} to lists that use []
myset = {'apple', 'banana', 'cherry'}
try:
    myset.insert('apple')
    print('used insert() function') # this does not work
except:
    myset.add('apple')
    print('used add() function') # this one works

# but we still only have three items as sets don't have duplicates
print('items in set: ', len(myset))

# we can remove items
myset.remove('apple')

# and we can iterate over a set as we did with a list
for x in myset:
    print(x)

# we can join sets with the union() function
myset2 = {'BMW'}
myset3 = myset.union(myset2)
print(myset3)

# to see if something is in a set is straightforward
print('banana in myset3?: ', 'banana' in myset3)

# there are a lot of set method that manipulate sets including:
# clear()           - removes all elements
# intersection()    - returns a set that's intersection of two others
# isdisjoint()      - returns whether has no common elements
# ... and many others

print(myset.isdisjoint(myset3))   

# On to another item, tuples.  This is a little "object" that binds together
# other variables
mytuple = ('apple', 0.95, 1000) # this cannot be changed now it is created
print(mytuple)

price = mytuple[1] # index this items using 0-based indexing
print(price)

# These tuples are a bit like lists and we can access elements or sub-ranges of them
# we can count from the back or the front
lastitem = mytuple[-1]
# if we specify a range then the last item is NOT included, eg 1:3 gives items 1 & 2
someitems = mytuple[1:3]
print(lastitem)
print(someitems)

# Tuples cannot be changed once created, but there is a workaround to reconstruct
alist = list(mytuple)
alist[2] = 2000
mytuple = tuple(alist)
print(mytuple)

# There are a couple of methods in tuples to count occurrences and to find a specific value
print(mytuple.count(2000)) # should return 1 as it occurs once
print(mytuple.index(2000)) # should return 2 as 2000 is the last item in 0-based positioning

# More on functions and parameters
# Normally a fixed number of parameters in a function and we must use the correct numbers

def AnotherFunc(para1, para2, para3):
    print('Min is: ', min(para1, para2, para3))

AnotherFunc(1, 2, 3)

# We can name the arguments in the function call
AnotherFunc(para2=12, para3=15, para1=13)

# It is possible to have an unknown number of argments
def UnFunc(*params):
    if(len(params) > 2):
        print('I was sent ', len(params), ' parameters')
    else:
        print('I was sent less than 3 parameters')

UnFunc(1)
UnFunc(1,2,3,4)

# A dictionary of arguments can be sent
def my_function(**child):
  print("His last name is " + child["lname"])

my_function(fname = "Sam", lname = "Green")

# functions can also have a default value for parameters
def my_func_with_defs(name, age=25):
  print(name, ':' + str(age))

my_func_with_defs('Raymond', 116)
my_func_with_defs('Fred')

# Lambda functions are defined as a local function within another function
lamb1 = lambda a, b, c: a + b + c
print(lamb1(5, 6, 2))

# Part 3: Still 19 November: Style Guide for Python coding
# ========================================================

# What are the coding guidelines for naming and layout and structure of Python?
# There is documentation here: https://peps.python.org/pep-0008/ and at the start
# it recommends line length of no more than 79, indendation of 4 spaces and how
# to lay out function headers with lots of long names etc.
# There's a whole load of comments about how to use white space around other parts
# of the language such as commas etc.  This isn't surprising relative to other
# languages.
# Whilst it would be a good idea to read and understand some of the
# information, one of the most important recommendations is to follow the
# style of the code that you are maintaining in a team.

# Part 4: 21 November: Classes
# ============================

# Python supports classes.  The approach to classes will be similar to
# other languages.

# We define a class and it contains functions that belong to the class
# and implicitly defines variables that are members of the class. 
class Rocket():
    # Rocket simulates a rocket ship for a game, or a physics simulation.
    
    # The __init__(self) function is called for each instance of the
    # object.  This is done automatically upon creation.  The self
    # variable is required.
    def __init__(self, x=0, y=0):
        # Each rocket has an (x,y) position.
        # The position can be provided at creation, and if not then
        # the default position will be (0,0) using default parameters.
        # self is used to refer to the specific instance of the object
        self.x = x
        self.y = y
    
    # This move_up(self) function is a normal method and it must also
    # have self as its first parameter to refer to the specific instance
    def move_up(self):
        # Increment the y-position of the rocket.
        self.y += 1

# we create an instance of the method in a similar way to variables
my_rocket = Rocket()
my_rocket.move_up()
print('rocket position', my_rocket.x, my_rocket.y)

# Note that the internal variables of the object are accessible outside
# of the object.  In C++ terms this is like having the 'public' attribute
# apply to all member variables.
# Rather than use public/private keywords as in C++, there is a 
# naming convention that varibles starting with an _underscore 
# should be treated as internal, and not used as part of the public
# API of the class.
# So, let's create another classe and see what happens if we use
# a name with an underscore
class Protector():
    def __init__(self):
        # double __underscore means private
        self.__mysecret = 'ABC123'
        self._lesssecret = 'DEF456'

    # We can declare a member variable directly, not inside a function
    a_var = 987

    # If we want to encapsulate the variable and have getter/setter
    # functions.  This allows validation checks on setting
    def get_secret(self):
        return self.__mysecret
    def set_secret(self, secret):
        self.__mysecret = secret

p = Protector()

try:
    print(p.__mysecret)
except:
    print('Did not access the variable with double __underscore')

try:
    print(p._lesssecret)
except:
    print('Did not access the variable with single _underscore')

print('using getter function', p.get_secret())

# We can access an internal variable declared directly that does not
# have the double __underscore naming
print(p.a_var)

# Names with the single _underscore are a convention to discourage 
# use outside of the object, but it is not enforced by the system
p._lesssecret = 'changed it!'
print(p._lesssecret)

# How to class attributes work? Do they vary by instance?
p1 = Protector()
print('p1', p1.a_var) # expect 987
p2 = Protector()
p2.a_var = 999
print('p1', p1.a_var) # stays at 987
print('p2', p2.a_var) # now 999 
# what if we change it on the class?
Protector.a_var = 123
print('p1', p1.a_var) # changes to 123
print('p2', p2.a_var) # now 999 
p1.a_var = 456
print('p1', p1.a_var) # changes to 456
print('p2', p2.a_var) # still 999
print('Protector.a_var', Protector.a_var) # is 123
# create a new object and what does it have?
p3 = Protector()
print('p3', p3.a_var) # expect 123
# The class attribute works ok unless there's a clashing name in which
# case external access as above uses the object's version that masks
# the class attribute.

# Class methods can be created and called on a class rather than an
# instance.  These methods cannot access the objects.

class MyClass:
    class_counter = 0

    @classmethod
    def IncrementClassCount(cls, num=1):
        cls.class_counter += num

mc = MyClass()
mc.IncrementClassCount()
mc.IncrementClassCount(4)
print(mc.class_counter)

# Classes can be created that inherit from another class
class Pet:
    def __init__(self, name):
        self.name = name

class Dog(Pet):
    def __init__(self, name):
        super().__init__(name)

    def Speak(self):
        print('woof, I am ', self.name)

class Cat(Pet):
    def __init__(self, name):
        super().__init__(name)

    def Speak(self):
        print('meouw, I am', self.name)

d = Dog('Pepper')
c = Cat('Mash')

d.Speak()
c.Speak()

# Static methods are how some libraries of functions work
class Math:
    @staticmethod  
    def Add5(x):
        return x + 5

# no need to have an instance of the class, just call the class method
print(Math.Add5(8))

# Part 5: 23 November: Environments
# =================================

# Like most other modern languages, Python has a rich ecosystem of packages
# in the public domain with different versions existing. When a computer is
# used for more than a few software tasks there can be problems with version
# clashes at the package/source code level

# Virtual environments can  be created to address this.  This is an optional
# feature.  The essence of this is a (hidden) folder .venv inside a project
# folder that can hold a specific version of Python and pip plus all of the
# packages required by the project.

# This can make a project folder larger ... but can be reproduced and will
# ensure separation.  Links and shortcuts may make some aspects of the
# virtual environment more effcient ... but this is handled by the tools.

# There are different ways of creating virtual environments by OS and by
# IDE, but it is well supported by VS Code and its documentation.

# This may not be an issue in small/personal environments, but it
# would certainly be a big consideration for standardised and robust version
# control in production environments in teaching or business to keep support
# overheads under control.


# Part 6: 23 November: numpy
# ==========================

# Python's lists can contain any type of variable and this makes them
# potentially inefficient.  Also, manipulating data using Python code
# that is iterpreted can be less efficient than compiled code.

# Numpy is a package for "scientific" computing using multidimensional
# array and associated functions.  There are many packages that use
# numpy as its base.

# Numpy can be more efficient because it is using a more efficient data
# structure and also because functions in numpy's package that are
# written in C can be used.

import numpy as np

# arange(15) returns a vector with 15 elements, starting at 0
# and reshape converts this vector into a 2D matrix
a = np.arange(15).reshape(3,5)
print(a)

print(type(a)) # returns <class 'numpy.ndarray'>
print(type(a[0])) # returns <class 'numpy.ndarray'>
print(type(a[0][0])) # returns <class 'numpy.int64'>

print(a.ndim) # returns 2
print(a.shape) # returns (3,5)
print(a.dtype.name) # returns int64
print(a.itemsize) # returns 8 (bytes)

# We can apply some straigthforward operations with little code
# as numpy is smart enough to allow a mix of matrix and scalar
# expressions and do something sensible without visible loop code
b = a + 5
print(b)

# numpy arrays can be created from normal lists
c = np.array([1,2,3])
print(type(c)) # returns <class 'numpy.ndarray'>

# combinations of lists can produce arrays ... etc
d = np.array([[1,2,3], [4,5,6]])
print(d.shape) # returns (2,3)

# Numpy has many functions included and numpy is used as the target
# for many other packages that require fast calculations.
# This is a good introduction to numpy arrays:
# https://www.youtube.com/watch?v=lLRBYKwP8GQ

# control over the specific data type at creation
e = np.array([1,2,3], dtype=np.int8)

# handy functions
z = np.zeros((2,2))
o = np.ones((2,2))
x = np.empty((2,2)) # contains uninitialised data: dangerous?
i = np.eye(3) # 1 on diagonal
j = np.eye(5, k=-1) # 1 on sub-diagonal 

# filtering can select items satisfying a condition
j[j == 1] = 13 # updates values that were value 1 to 13
print(j)

# filtering (selecting) a specific row and amending
j[0] = 3 # updates first row to value 3
print(j)
j[:2] = 4 # updates the first two rows (ie up to the stop value)
print(j)

# column operations are not quite so slick
j[:,-1] = 99 # updates the last column, also showing index from RHS
print(j)

# can sort data in each row ... syntax defaults to row
l = np.sort(j)
print(l)

# or we can sort by column
m = np.sort(j, axis=0)
print(m)

# we can create a view of the data ... but be careful because if we
# modify a view then the original data is changed ... a view is a reference
# and not a copy.  But what's useful is that a view can have a different
# shape and that does not impact on the shape of original data

n = m.view()
q = m.copy()

n[:] = 4
print(m)
print(n)
print(q)


# Part 7: 24 November: list comprehension
# =======================================

# A list comprehension is an efficient syntax for expression operations on a list
# It can be much more efficient than a loop.  There are similar features in other
# languages.
# This creates a list from an operation on each item in a range 
mylist = range(1,10)
squares = [x**2 for x in mylist]
print(squares)

# we can add a filter on the items chosen
even_squares = [x**2 for x in mylist if x % 2 == 0]
print(even_squares) # => [4, 16, 36, 64]

# comprehensions work with lists of strings
fruit = ['apple', 'banana', 'chocolate']
first_character = [name[0] for name in fruit]
print(first_character) # => [a, b, c] 

# and with individual characters in a string
info = "Charlie 07987 654 321"
phone_num = [x for x in info if x.isdigit()]
print(phone_num)

# could be used to read lines in a file ... but who knows whether this is fast
file = open('demofile.txt', 'r')
txt = [line.strip() for line in file]
print(txt)

# compound argments can be used
nums = [x+y for x in [1,2,3] for y in [10,20,30]]
print(nums)

# => Using list comprehensions well will require a new way of thinking


# Part 8: 25 November: JSON
# =========================

# JSON can be created and manipulated in Python with native support
import json
# This string could have come from a file ...
jstr = '{ "name":"John", "age":30, "city":"New York"}'

# This returns a Python dictionary
j = json.loads(jstr)

print(j['age']) # => 30

# what if we have something more complex?
# we get back a more complex dictionary and as that can hold anything it
# converts nicely to Python objects.
jstr = '{ "name":"John", "myarray":[30, 40, 50]}'
j = json.loads(jstr)
print(type(j['myarray'])) # => list

# make a simple amendment to the data whilst in Python form
j['myarray'].append(99)

# how do we save this to a file?
# just write the dumps() string to a file
f = open("demofile.json", "w")
f.write(json.dumps(j))
f.close()

# for completeness, let's load it back
def CheckJsonFileRead():
    f = open("demofile.json", 'r')
    kstr = f.read()
    k = json.loads(kstr)
    f.close()
    print(k == j)
    assert k == j

CheckJsonFileRead()

# Check that it works if we have the object split over lots of lines
f = open("demofile.json", "w")
# create a messy but legal version
f.write('{"name":"John"\n,\n "myarray":\n[30,\n\n 40, 50,99\n]\n}')
f.close()

CheckJsonFileRead()


# Part 9: 1 December: CSV
# =======================

# There is a standard module that provides CSV functionality and has various
# options to parameterise the read/write processes to deal with dialects that
# exist in common sub-dialects, eg as preferred by Excel.
import csv

with open('mycsv.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',')
    spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
    spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])

# The file created just contains data, but does not contain a field header row
# at the start.  This could be added by just having another row sent at the start

with open('mycsv.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    for row in spamreader:
        # each row here is a list containing strings
        print(row)

# CSVs that have a first row with field names are produced by many DB systems and
# this is also a logical format of choice so that the fieldnames can be dynamic
# and data-driven rather than in either a separate file or hard coded in a program.

# There is a csv.Sniffer class that looks at the data and seeks to deduce information
# including whether there is a header.  This could be useful, but might give all sorts
# of false positives/negatives.  However, in some situations this may be more helpful
# with a more restricted subset of data and be part of some dynamic identification.

# Let's do this again with a header, which from a writing perspective is just another
# row of data
with open('data.csv', 'w', newline='') as csvfile:
    datawriter = csv.writer(csvfile, delimiter=',')
    # This is my header row
    datawriter.writerow(['PolNum','Age','Term','SA','Premium'])
    datawriter.writerow(['P001', 25, 10, 100000, 100])
    datawriter.writerow(['P002', 35, 12, 200000, 150])
    datawriter.writerow(['P003', 45, 15, 300000, 200])

# Now we can read it back and give the first row special treatment
with open('data.csv', newline='') as csvfile:
    datareader = csv.reader(csvfile, delimiter=',')
    # special treatment puts names into a list
    header = []
    header = next(datareader)
    print(header)
    for row in datareader:
        # each row here is a list containing strings
        print(row)

# if we were very confident of the data ... perhaps we wrote it in a stable
# and well controlled piece of code earlier ... then we could have a small
# amount of validation code ... but we might have to have extensive checks
# if the data is less well controlled in upstream processes.

# csv also allows a dictionary to be read (or written) using the header
# field names as the dictionary keys.  Once again, you'd need to have some
# confidence on the data structure ... or write lots of validation code.
with open('data.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['PolNum'], row['SA'])


# Part 10: 14 December: main() function and parameters from command line
# ======================================================================

# When run at the command line using "python hello.py" the special variable
# __name__ will have the value "__main__" and then we would know to call
# the main function.  This is done explicitly in our code, unlike many
# compiled languages that require this as the executable's entry point.
# Then we can define a main() function and execute it if the name of
# this special variable is "__main__".

print("The value of __name__ is:", repr(__name__))
print("The value from a module is: ", mymodule.GetNameString())

# There are two ways of parsing arguments ... argparse is an easier way.

import argparse

def test(para):
    print("in test", para)

def main():
    print("in main function")
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--test')
    parser.add_argument('-a', '--addtest')
    parser.add_argument('-v', dest='verbose', action='store_true')
    args = parser.parse_args()
    print(args)
    test("called from main")
    
    # Now we can respond to whatever we received 
    
if __name__ == "__main__":
    main()



# Other things to look at, standard:
# Pandas
# Plotting ... matplotlib

# More adventurous areas:
# Cython
# Embedding
# Extending