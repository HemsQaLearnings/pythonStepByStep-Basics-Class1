# 1. Empty Function
def empty_function():
    pass  # This function does nothing

# Calling the empty function
empty_function()

# -------------------------------------------------
# 2. Empty Loop
for i in range(5):
    pass  # This loop does nothing

# The loop iterates over the range, but no action is taken

# -------------------------------------------------
# 3. Empty Class Definition

class EmptyClass:
    pass  # This class has no attributes or methods

# Creating an instance of the empty class
obj = EmptyClass()

# -------------------------------------------------
# 4.Using pass in Conditional Statements
x = 10

if x > 0:
    pass  # No action needed if x is positive
else:
    print("x is not positive")
# -------------------------------------------------
# 5. Using pass in Exception Handling
try:
    # Code that may raise an exception
    1 / 0
except ZeroDivisionError:
    pass  # Ignore the exception and do nothing

print("Program continues running after the exception")
