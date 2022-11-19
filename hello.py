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
# languages








