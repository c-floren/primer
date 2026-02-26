print("Hello from Python!")
print("-------------------")

# Claude Dynamic Typing Python Practice Problems
# Problem 1: Type Shape-Shifter
def describe(value):
    print(type(value), value)

describe(42)
describe("hello")
describe([1, 2, 3])

# Problem 2: Reassignment Tracker
x = 10
describe(x)
x = "ten"
describe(x)
x = [10]
describe(x)

# Problem 3: Flexible Adder
def flexible_add(a, b):
    return a + b

print(flexible_add(3, 4))
print(flexible_add("hello", "world"))
print(flexible_add([1, 2], [3, 4]))

# Claude list loop exercises
# Exercise 1: Sum It Up
numbers = [4, 7, 2, 9, 1]
total = 0
for num in numbers:
    total += num
print(f"The sum of numbers is {total}")

# Exercise 2: Flip the Negatives
values = [3, -5, 8, -2, 6, -1]
for val in values:
    print(abs(val), end=" ")
print()

# Exercise 3: Build a New List
words = ["apple", "banana", "cherry", "date"]
long_words = []
for word in words:
    if len(word) > 5:
        long_words.append(word)
print(f"The new list is {long_words}")

# Loop Practice 1-10 with for vs while
# for loop
print("for loop: 1-10")
for i in range(1, 11):
    print(i, end=" ")
print()

# while loop
print("while loop: 1-10")
i = 1
while i <= 10:
    print(i, end=" ")
    i += 1
print()

# Functions
def my_greet(name):
    return f"Hello {name}"

# ask Claude: Can you check my function for clarity
# and suggest a more Pythonic version?
def claude_greet(name="World"):
    return f"Hello, {name}!"

# Claude responded
# default parameter makes function usable without an argument
# comma and exclamation mark follow standard greeting punctuation

print(my_greet("Claude"))
print(claude_greet("friend"))
print(claude_greet())

# Exceptions
# Claude real world try-except exercise
"""You're building a simple calculator. Write a function safe_divide(a, b) that:

1. Takes two inputs from the user using input() (so they come in as strings)
2. Converts them to integers
3. Divides a by b and prints the result
Handle these two real-world problems with try/except:

1. The user types something that isn't a number (e.g. "five")
2. The user enters 0 as the divisor"""

def safe_divide(a, b):
    try:
        print("Result:", int(a)/int(b))
    except ValueError:
        print("Error: Please enter valid integers.")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")

num1 = 10 #input("Enter a: ")
num2 = 2  #input("Enter b: ")
safe_divide(num1, num2)

# Python Modules
# Claude 5 useful beginner-friendly Python modules

# 1. random - generate random values
import random
print(random.randint(1, 10))
print(random.choice(["a", "b", "c"]))

# 2. math - mathematical functions
import math
print(math.sqrt(16))
print(math.pi)
print(math.ceil(4.2))

# 3. datetime - work with dates and times
from datetime import datetime
now = datetime.now()
print(now.strftime("%Y-%m-%d %H:%M"))

# 4. os - interact with the operating system
import os
print(os.getcwd)
print(os.listdir("."))

# 5. json - read and write JSON data
import json
data = {"name": "Alice", "age": 30}
encoded = json.dumps(data)
decoded = json.loads(encoded)
print(decoded["name"])

# Debugging with print statements
def count_long_words(sentence):
    words = sentence.split()
    count = 0
    for word in words:
        if len(word) > 5:
            # print("count:", count)
            # count never changed from 0
            # count + 1
            # fix: += instead of +
            count += 1
    return count

print(count_long_words("elephant runs quickly through the forest"))

# Debugging with breakpoints
def factorial(n):
    result = 1
    for i in range(1, n):
        result *= i
    return result

print(factorial(5))

# Basic tests with pytest
def multiply(a, b):
    return a * b

result = multiply(3, 4)
print(result)

def test_multiply_negative_numbers():
    assert(multiply(-2, -9) == 18)

def test_multiply_zero():
    assert(multiply(2, 0) == 0)

# Assertion inside scripts
x = 5
y = 10
assert x + y == 15, "Math is broken"
