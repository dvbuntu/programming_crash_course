# basic syntax

## printing
print('Hello, World!')

# pound sign indicates a comment, i.e. not code

## store values into a variable
x = 'I am a variable'
print(x)

y = 'Different variable'
print(y)

y = 'Overwritten variable'
print(y)

## types of variables
x = 'ABC'   # string
x2 = "def"  # also a string, can use either quote
y = 10      # integer
z = 10.0    # floating point (i.e. decimal)
a = True    # boolean value
b = False   # boolean value

# simple calculations
x = 2 + 2
print(x)

y = 3 * (x-2)
print(y)

z = x**y # exponentiation
print(z)

print( y % x ) # y modulo x

## add two strings!
x = 'abc'
y = 'def'
print(x + y)

# conditional operation
x = 2
if x < 1:
    print("Success!")
elif x == 2:
    print("x is 2")
else:
    print("No luck!")

if False:
    print("Will never show up")

# Lists and dictionaries
## Lists store many things in some order
thing = [1, 2, 'abc']
print(thing)

## Access specific elements by index (first is 0)
print(thing[0])
print(thing[0] + thing[1])

## Assign new value
thing[2] = 'def'
print(thing)

## list of lists!
foo = [thing, ['a', 'b', 'c']]
print(foo)

## append new value to end of list
foo.append('def')
print(foo)

## strings are similar to lists, access by index
bar = 'my string'
print(bar[3])

## but you can't set values in a string
bar[2] = 'x' # Error!

## Dictionaries store things indexed by other things!
info = {'cat':3, 'dog':2, 'wombat':0}
print(info['cat'])

## add new entry to dictionary
info[4] = 'four'
print(info)

## overwrite an entry
info['cat'] = [1,2,3]
print(info)

# Iteration
## Automate doing nearly the same thing over and over again
for element in [1,2,3]:
    print(element)

## often iterate through list of just numbers
for i in range(10):
    print(i, i**2)

# sum 0-100
s = 0
for i in range(101):
    s += i
print(s)


* Basic syntax (printing, arithmetic operations, basic types, variables)
* Conditionals/simple flow control (if...elif...else)
* Iteration (for loops, maybe while loops, probably some python `range` magic)
* Functions
* Useful packages (numpy with basic array ops, maybe scipy, matplotlib)
