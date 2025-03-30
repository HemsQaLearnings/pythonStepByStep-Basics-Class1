# Single Executable Statement

name=input("Enter Name:")
print("Here we print the name : ",name)

# -------------------------------------------
# Python also allow us to write Multiple Executable Statements on a Single Line,
# by separating each pair of the statement using a semicolon(;) as :
value=10+20+30+40; print("the value of Value is : ",value)

x = 10; y = 20; z = x + y; print("the value of z is : ",z)

# -------------------------------------------
# Multiple Executable Statements on a Single Line
value1=10+20+30+\
    40+50+\
    10+10
print("the value of Value1 is : ",value1)

# -------------------------------------------
# Multiple Executable Statements on a Single Line

value2=(10+20+30+\
    40+50+\
    10+10)
print("the value of Value1 is : ",value2) # This will result the same oupt as previous example

# -------------------------------------------
# Multiple Executable Statements on a Single Line
# Similarly we can impliment a long list in multiple lines :

myList=[10,20,30,40,50,10,60]
print("the value of myList is : ",myList)