name, age, sal = "Hemanth", 30, 10000.35

# Approach1
print(name, age, sal)

# Approach2
print("Name is:", name)
print("Age is:", age)
print("Sal is:", sal)

# Approach3 : using  %  Here type is imp
print("Name:%s  age:%d  salary:%g" % (name, age, sal))

# Approach3 : using  {} Here value is imp
print("Name:{}  age:{}  salary:{}".format(name, age, sal))

# Approach4 : using  {} Here value is imp
print("Name:{0}  age:{2}  salary:{2}".format(name, age, sal))
