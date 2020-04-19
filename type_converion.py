# Basic understanding of type conversions in Python 

# Implicit type conversion
num_int = 123
num_flo = 1.23

num_new = num_int + num_flo

print("datatype of num_int:",type(num_int))
print("datatype of num_flo:",type(num_flo))

print("Value of num_new:",num_new)
print("datatype of num_new:",type(num_new))

''' Output
datatype of num_int: <class 'int'>
datatype of num_flo: <class 'float'>
Value of num_new: 124.23
datatype of num_new: <class 'float'>
'''

# Explicit type conversion
num_int = 123
num_str = "456"

print("Data type of num_int:",type(num_int))
print("Data type of num_str before Type Casting:",type(num_str))

num_str = int(num_str)
print("Data type of num_str after Type Casting:",type(num_str))

num_sum = num_int + num_str

print("Sum of num_int and num_str:",num_sum)
print("Data type of the sum:",type(num_sum))

''' Output
Data type of num_int: <class 'int'>
Data type of num_str before Type Casting: <class 'str'>
Data type of num_str after Type Casting: <class 'int'>
Sum of num_int and num_str: 579
Data type of the sum: <class 'int'>
'''

# using  tuple(), set(), list() 
# initializing string 
s = 'geeks'
  
# printing string converting to tuple 
c = tuple(s) 
print ("After converting string to tuple : ",end="") 
print (c) 
  
# printing string converting to set 
c = set(s) 
print ("After converting string to set : ",end="") 
print (c) 
  
# printing string converting to list 
c = list(s) 
print ("After converting string to list : ",end="") 
print (c) 

''' Output
After converting string to tuple : ('g', 'e', 'e', 'k', 's')
After converting string to set : {'k', 'e', 's', 'g'}
After converting string to list : ['g', 'e', 'e', 'k', 's']
'''