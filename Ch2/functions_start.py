#
# Example file for working with functions
#

# define a basic function
def func1():
    print("I am a function!")

# function that takes arguments
def func2(args1, arg2):
    print(args1, " ",args2)
# function that returns a value

def cube(x):
    return x*x*x

# function with default value for an argument
def power(num,x=1):
    result = 1
    for i in range(x):
        result = result * num
    return result

#function with variable number of arguments
def multi_add(*args):
    result = 0
    for x in args:
        result = result + x
    return result

# func1()
# print(func1())
# print(func1)
print ("Cube is ",cube(3))
print("Power is ",power(2,3))

print("Multi add results is ",multi_add(2,3,4,5,6,7,8))
