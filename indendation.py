# Using Indentation in a Function
def greet(name):
    if name:
        print(f"Hello, {name}!")  # Indented to belong to the if block
    else:
        print("Hello, World!")  # Indented to belong to the else block

greet("Alice")
greet("")

# ------------------------------------------------------------------------------
# Indentation in Loops and Conditionals
# Example: Using Indentation in a Loop

for i in range(3):
    print(i)  # This line is part of the for loop block
    if i % 2 == 0:
        print(f"{i} is even")  # This line is part of the if block within the for loop

# ------------------------------------------------------------------------------

# Indentation in Classes
# Example: Using Indentation in a Class Definition

class Person:
    def __init__(self, name):
        self.name = name  # This line is part of the __init__ method

    def greet(self):
        print(f"Hi, I'm {self.name}")  # This line is part of the greet method

person = Person("Alice")
person.greet()

# Shortcut Keys for Indentation in Popular IDEs
# PyCharm
# Increase Indentation: Tab
# Decrease Indentation: Shift + Tab
# Auto-Indent: Ctrl + Alt + I (Windows/Linux) or Cmd + Option + I (macOS)