msg = "Hello world Python!"

# Testing 'else' clauses in 'try' blocks
try:
    #raise IOError()
    pass
except RuntimeError as rerror:
    print("Hit a runtime error")
except IOError as ioerror:
    pass
else:
    print("Hit no errors?")
finally:
    print("Done")

# Testing lambda expressions
from typing import Callable
def lambdaInput(n: int, arg: Callable[[int], int]) -> int:
    return arg(n) + 5

lambdaRes = lambdaInput(5, lambda x: x + 5)

def lambdaOutput(n: int) -> Callable[[str], int]:
    return lambda s: len(s) + n

lambdaFunc = lambdaOutput(n=5)
lambdaRes = lambdaFunc("HelloWorld")

# List comprehension
comprehendedList1 = [b+1 for b in range(10)]
print(comprehendedList1)

comprehendedList2 = list(map(lambda x: x*x, range(5)))
print(comprehendedList2)

# Slice allocates a new list
# (replacing words3 in for-iterator with words or words2 will result in infinite loop)
words = ['cat', 'window', 'defenestrate']
words2 = words
words3 = words[:]
for w in words3:
    if (len(w) > 6):
        words.insert(0, w)
print(words)

# Explicit type instantiation and simple conditional block
b = bool(False)
if b == True:
    print(msg)
else:
    print("Hmm")

# Explicit type instantiation and while block
b = int(False)
print(b)
while (b < 20):
    print(b)
    b+=1

# Range, for loop, and list appends
l = []
for i in range(b, b+10, 1):
    l.append(i)

print(l)

import sys as sis

def print_input_number():
    try:
        arg = int(sis.argv[1])
        print(1.0 / arg)
    except ValueError:
        print(f"Expected numeric argument, but got '{sis.argv[1]}'")
    except ZeroDivisionError:
        print("Expected nonzero numeric argument")

# Generator functions
def my_range(n):
    i = 0
    while (i < n):
        yield i
        i+=1

generator = my_range(5)
l = [x for x in range(5)]
another_generator = (x for x in range(5))
print(list(another_generator))

print(l)
for i in generator:
    print(i)

# File I/O
file = open('readme.md', 'r')
for line in file:
    print(line)
file.close()

# Classes
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self: Point, other: Point) -> Point:
        res = Point(self.x, self.y)
        res.x += other.x
        res.y += other.y
        return res
    def __str__(self):
        return f"({self.x}, {self.y})"

p = Point(5, 10)
q = Point(1, 5)
r = p + q
print(r)
print(msg)

# Numeric instantiation of bool
numericBool: bool = 1
if numericBool:
    print(numericBool)
else:
    print(True)

exit()