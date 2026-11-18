# #**************
# #*********Functions

# # Writing to add two numbers 

def display_sum(num1,num2):
    sum = num1 + num2              # We are defining a function display_sum
    print('The sum of', num1 ,'and ',num2, 'is - ' , sum)                      

# # a function will have : 
# # 1. function name 
# # 2.input(s)
# # 3. Body of the function ( what the function actually does)
# # 4. output


# # while we definr input variable in the functon definition , we are
# # Creating new variales with scope within the function\

# # call the function / invoking the function
# # display_sum(8,7)
# # display_sum(2026,8)
# # display_sum(9.8, 6.6)
# # display_sum('Happy ', 'diwali')

# # display_sum(8,7,8) output : TypeError: display_sum() takes 2 positional arguments but 3 were given

def display_sum_custom():
    print('We will display the sum of two numbers : ')
    num1 = float(input('Enter the first number : '))
    num2 = float(input('Enter the second number : '))
    sum = num1 + num2
    print('The sum of', num1 ,'and ',num2, 'is - ' , sum)   

# display_sum_custom()



def display_name():
    user = input('Please enter Your Name - ')
    print('Hi, ',user , ' Good afternoon  ', ' How are you ? ')

# display_name()

#Generating multiplication table

num = 5 
print('Multiplication table of ', num)
print('*********************')
for i in range(1, 11):
    print(i, '*', num, '=', (i * num))

print('******************')

num = 8 
print('Multiplication table of ', num)
print('*********************')
for i in range(1, 11):
    print(i, '*', num, '=', (i * num))

print('************************')


# Function to display multiplication table of a number

def multiplication_table():
    print('We will display the multiplication table of the number you enter : ')
    num = int(input("Enter the number : "))
    print('------------------------')
    print('Multiplication table of  ', num )
    for i in range (1,11):
        # print(i , ' X ', num , " = ", (i * num) )
        print(f"{i} X {num} = { i* num}")
    print('------------------------')

# multiplication_table()


# #*****************
# #***************

# score1 = int(input(' PLease enter the score 1 - '))
# score2 = int(input(' PLease enter the score 2 - '))
# score3 = int(input(' PLease enter the score 3 - '))
# score4 = int(input(' PLease enter the score 4 - '))
# score5 = int(input(' PLease enter the score 5 - '))

# scores = (score1, score2, score3, score4, score5)
# print(scores)


# def calculate_sum(input_tuple):
#     sum = 0
#     for i in range(len(input_tuple)):
#         sum = sum + input_tuple[i]
#     print(f'The sum of scores = {sum}')
#     return sum                                      # output of the function

# total = calculate_sum(scores)                          # whenever their is an output we assign it to a variable


# def calculate_average(input_tuple):
#     total = calculate_sum(scores)
#     count = len(input_tuple) 
#     average = total / count
#     print(f'Average of  Scores = ', average)
#     return average


# calculate_average(scores)

# def find_large():
#     large = max(scores)
#     print(f'The largest score is - ', large)

# find_large()

# def find_small():
#     small = min(scores)
#     print(f"The lowest score is - ", small)

# find_small()


#********************
#*********Arguments***

# # Here exp is an optional input, default value is 2.
# def calculate_exponent(num, exp = 2):
#     print(num ** exp)

# # calculate_exponent(5)
# # calculate_exponent(5,3)

# #Here wish is an optional input , default value here is ' good day.
# def create_wish( name, wish = 'Good day'):
#     print(f"Hi {name},{wish}")

# create_wish("Akash")
# create_wish("Akash", "have a Nice ")        #Positional argument
# # We can give value of the argument explicitily.
# create_wish(wish = "have a Nice ", name = "Akash")


#*************************************
#*************************************
#*************************************


def divide(num,den):
    result = num / den
    print(f'The answer is {result}')

divide(40,5)
divide(1234,678)
divide(1234,6789)
# divide(1234,0) # gives error of zerodivision error 
# divide('a','b') # TypeError: unsupported operand type(s) for /: 'str' and 'str'

# output of above
# The answer is 1.8200589970501475
# The answer is 0.18176461923700102

print('****')

# Summary Table


# Error Type	Primary Cause	Quick Example
# TypeError	Incompatible data types in an operation	'age: ' + 25
# ValueError	Right data type, invalid content	int("hello")
# NameError	Undefined variable or function name	print(undeclared_var)
# IndexError	List or tuple index out of bounds	[1, 2][5]
# KeyError	Missing key in a dictionary	{'a': 1}['b']
# AttributeError	Invalid method or property on an object	(5).upper()
# ZeroDivisionError	Dividing or taking modulo by zero	5 / 0
# FileNotFoundError	Missing file or directory path	open("missing.txt")



# exception handling.
# We write specific criteria so that code flow is not interruptted
# we write potensial runtime errord making code inside try block
# and the expection will be caught on expect block.
# rewriting the function with expection block

def divide_new(num,den):
    try:
        result = num / den
        print(f'The answer is {result}')
    except:
        print('There is a problem')


divide_new(40,5)
divide_new(1234,678)
divide_new(1234,6789)
divide_new(1234,0) # when using try the program will continue to move on unlike the before program stops on error 
divide_new('a','b')

# output of above: 
# The answer is 8.0
# The answer is 1.8200589970501475
# The answer is 0.18176461923700102
# There is a problem
# There is a problem
print('*******')


def divide_new1(num,den):
    try:
        result = num / den
        print(f'The answer is {result}')
    except Exception as e:
        print(f'There is a problem : {e}')
    print('The end')

divide_new1(40,5)
divide_new1(1234,678)
divide_new1(1234,6789)
divide_new1(1234,0) # when using try the program will continue to move on unlike the before program stops on error 
divide_new1('a','b')

# output of above:
# The answer is 8.0
# The end
# The answer is 1.8200589970501475
# The end
# The answer is 0.18176461923700102
# The end
# There is a problem : division by zero
# The end
# There is a problem : unsupported operand type(s) for /: 'str' and 'str'
# The end

print("*****")
# rewriting the function with expection block displaying the apporopriates

def divide_new2(num,den):
    try:
        result = num / den
        print(f'The answer is {result}')
    except TypeError:
        print(f'Please make sure you are entering a number ')
    except ZeroDivisionError:
        print('Please enter a non zero value as denominator ')
    except Exception as e:
        print(f'There is a problem : {e}')
    
    print('The end')


divide_new2(40,5)
divide_new2(1234,678)
divide_new2(1234,6789)
divide_new2(1234,0) # when using try the program will continue to move on unlike the before program stops on error 
divide_new2('a','b')