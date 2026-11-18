# # we normally assign values to variable. but in  input we take data from user.

# username = input('Please enter your username : ') # we are waiting for the user to enter the value. we use input () for thr user tto assign the username 
# password = input('Please enter your password : ') # When we give a message in input() we get a pop up msg, so the user using the code will be able to understand what is to be done

# print ( 'the username you entered is', username)
# print ( 'the password you entered is', password)

# print('The username datatype is : ', type(username))     # type() shows which typw of data type is given as the input.
# print('The password datatype is : ', type(password))  # we can add a msg in the box '' 

# # if we give a number as input also we will get the data type as string, what ever value we input to input() it will only give output string.
# # we have to explicitily convert into numerical datatype if needed
# # int(variable_name) # interger
# # float(variable values) # float

#*****************************************************
#*****

# age = input('Enter your age : ')      # input from the user age.
# height = input('Enter your height :') # input from the user height.

# age = int(age)      # we converted the string to integer age.
# height = float(height) # we converted the string to float height.

# print('The age of user is -', age) # shows the output age. 
# print('The height of the user is -', height) # shows the output height the user entered. 

# print('The datatype of age is - ', type(age))  # shows the datatype after we explicitily converted to the integer.
# print('The datatype of height is - ', type(height)) # the the datatype after we explicitily converted to float.

# #**********************
# #****************



#below are all the inputs by the user
name = input('Enter your name - ')
dob = input('Please enter your date of birth - ')
course = input('please enter the course that you have pursed - ')
place = input('please enter your place - ')
college = input('Please enter the college thst you have studied -')
interest = input('Please enter your interesting field of job - ')

#printing the combined self introduction of the user
print('Good Morning, My name is ', name, ' was born on' , dob, 'have completed a graduation in ', course,  'and i am from ', place, '. The college were i completed my graduation is ', college,'. The job feild that i am mostly interested is ', interest )



