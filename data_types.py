# Basic understanding of Data types in Python 

# Numbers
a = 5
print(a, "is of type", type(a)) # Type() function is used to know the datatype class

a = 2.0
print(a, "is of type", type(a))

a = 1+2j
print(a, "is complex number?", isinstance(1+2j,complex)) # isinstance() function is used to check if an object belongs to a particular class.

''' Output
5 is of type <class 'int'>
2.0 is of type <class 'float'>
(1+2j) is complex number? True
'''


# String
str = 'Hello World!'

print (str)          # Prints complete string
print (str[0])       # Prints first character of the string
print (str[2:5])     # Prints characters starting from 3rd to 5th
print (str[2:])      # Prints string starting from 3rd character
print (str * 2)      # Prints string two times
print (str + "TEST") # Prints concatenated string

'''Output
Hello World!
H
llo
llo World!
Hello World!Hello World!
Hello World!TEST
'''

# List
list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']

print (list)          # Prints complete list
print (list[0])       # Prints first element of the list
print (list[1:3])     # Prints elements starting from 2nd till 3rd 
print (list[2:])      # Prints elements starting from 3rd element
print (tinylist * 2)  # Prints list two times
print (list + tinylist) # Prints concatenated lists

''' Output
[ 'abcd', 786 , 2.23, 'john', 70.2 ]
abcd
[786,2.23]
[2.23,'john',70.2]
[123, 'john',123, 'john']
['abcd', 786, 2.23, 'john', 70.2, 123, 'john']
'''

# Tuple
tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
tinytuple = (123, 'john')

print (tuple)           # Prints complete list
print (tuple[0])        # Prints first element of the list
print (tuple[1:3])      # Prints elements starting from 2nd till 3rd 
print (tuple[2:])       # Prints elements starting from 3rd element
print (tinytuple * 2)   # Prints list two times
print (tuple + tinytuple) # Prints concatenated lists

'''
('abcd', 786, 2.23, 'john', 70.2)
abcd
(786, 2.23)
(2.23, 'john', 70.2)
(123, 'john', 123, 'john')
('abcd', 786, 2.23, 'john', 70.2, 123, 'john')
'''

# Dictionary
dict = {}
dict['one'] = "This is one"
dict[2]     = "This is two"

tinydict = {'name': 'john','code':6734, 'dept': 'sales'}


print (dict['one'])       # Prints value for 'one' key
print (dict[2])           # Prints value for 2 key
print (tinydict)          # Prints complete dictionary
print (tinydict.keys())   # Prints all the keys
print (tinydict.values()) # Prints all the values

''' Output
This is one
This is two
{'name': 'john', 'code': 6734, 'dept': 'sales'}
dict_keys(['name', 'code', 'dept'])
dict_values(['john', 6734, 'sales'])
'''