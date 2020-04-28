# Basic understanding of Decision making in Python 

#If Else, If Elif Else, Nested If
x = 10
y = 20
z = 30

print("Start")
if x == 10:
    print(" Nested If")
    if y == 20:
        print(" End of Nested If Block ")
    else:
        print(" End of Nested If-Else Block ")
elif y == 20:
    print(" Elif block ")
else:
    print(" Nested If")
    if z == 30:
        print(" End of Nested If Block ")
    else:
        print(" End of Nested If-Else Block ")
print("Stop")
# Using Not operator
if not x > y :
    print("The number %d is less than %d" %(x, y))

''' Output
Start
 Nested If
 End of Nested If Block
Stop
The number 10 is less than 20
'''

# For loop
int_list = [1, 2, 3, 4, 5, 6]
sum = 0
for iter in int_list:
    sum += iter
print("Sum =", sum)
print("Avg =", sum/len(int_list))

#output - Sum = 21
#Avg = 3.5

for iter in range(0, 3):
    print("iter: %d" % (iter))

'''output
iter: 0
iter: 1
iter: 2 '''

#For Else loop
birds = ['Belle', 'Coco', 'Juniper', 'Lilly', 'Snow']
ignoreElse = False

for theBird in birds:
    print(theBird )
    if ignoreElse and theBird is 'Snow':
        break
else:
    print("No birds left.")

''' Output
Belle
Coco
Juniper
Lilly
Snow
No birds left.'''

# Use of break statement inside the loop
for val in "string":
    if val == "i":
        break
    print(val)

print("The end")

'''Output
s
t
r
The end'''

# Program to show the use of continue statement inside loops
for val in "string":
    if val == "i":
        continue
    print(val)

print("The end")

''' Output
s
t
r
n
g
the end'''

# While loop with else
def while_else_demo():

    count = 0
    while count < 5 :
        num = int(input("Enter number between 0-100?"))
        if (num < 0) or (num > 100):
            print("Aborted while: You've entered an invalid number.")
            break
        count += 1
    else:
        print("While loop ended gracefully.")

while_else_demo()

'''output 
Enter number between 0-100?1
Enter number between 0-100?2
Enter number between 0-100?3
Enter number between 0-100?4
Enter number between 0-100?5
While loop ended gracefully.'''

#Switch case
# Implement Python Switch Case Statement using Dictionary

def monday():
    return "monday"
def tuesday():
    return "tuesday"
def wednesday():
    return "wednesday"
def thursday():
    return "thursday"
def friday():
    return "friday"
def saturday():
    return "saturday"
def sunday():
    return "sunday"
def default():
    return "Incorrect day"

switcher = {
    1: monday,
    2: tuesday,
    3: wednesday,
    4: thursday,
    5: friday,
    6: saturday,
    7: sunday
    }

def switch(dayOfWeek):
    return switcher.get(dayOfWeek, default)()

print(switch(1))
print(switch(0))

'''output
Monday
Incorrect day'''

# Implement Python Switch Case Statement using Class

class PythonSwitch:

    def switch(self, dayOfWeek):
        default = "Incorrect day"
        return getattr(self, 'case_' + str(dayOfWeek), lambda: default)()

    def case_1(self):
        return "Monday"
 
    def case_2(self):
        return "Tuesday"
 
    def case_3(self):
        return "Wednesday"

s = PythonSwitch()

print(s.switch(1))
print(s.switch(0))

''' Output
Monday
Incorrect day'''