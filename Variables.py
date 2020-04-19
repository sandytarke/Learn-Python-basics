# Basic Variables understanding in Python 

#Assigning values to the variables

var1 = "Sandhya"    # This var1 is global variable
var2 = 2020
var3 = "Python"

print(var1,var3,var2)

def var_func():
    var1 = "Sandhya\'s programming"  # This var1 is local variable 
    var2 = 2010
    print(var1, var2, var3)

var_func()
print(var1)

# Multiple assigments
v1=v2=v3=30
a,b,c =10,20,30
print(v1, v2+v3)
print(a,b,c)


'''
Output
Sandhya Python 2020
Sandhya's programming 2010 Python
Sandhya
30 60
10 20 30
'''