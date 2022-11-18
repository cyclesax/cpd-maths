
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
