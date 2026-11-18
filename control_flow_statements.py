#*************************************
#***********************
#****   Checking whether a number is bigger than 50
#***********************

# number = input('Please enter a number - ')  # gets input from the user
# number_int = int(number)  # converting integer to number

# # number>50 # The number entered is bigger than 50
# # number<=50 # THE num not bigger than 50

# if(number_int > 50):           # if is conditional statement and we should put : collon for proper intentation of the lines  
#     print("The number entered is bigger than 50")

# if(number_int < 50):
#     print('The numeber entered is less than 50')

# print('End of program')




# #******************* we can use python tutor to visualise the python code
# ****************

# number = input('Please enter a number - ')  # gets input from the user
# number_int = int(number) 


# if(number_int > 50):           # if is conditional statement and we should put : collon for proper intentation of the lines  
#     print("The number entered is bigger than 50")
# else:                           # use: collon after else to proper intentation
#     print('The numeber entered is less than 50')



# print('End of program')

#***************************
#*******************

# number = input('Enter the number that we need to check as even or odd - ')   # Took the number to check from the user
# number = int(number)              # made it to an integer

# if( number % 2 == 0 ):                              # when reminder is zero it is an even number
#     print('The entered number is an even number')
# else:
#     print('The entered number is an odd number')

#*********************************
#*************************


# temp = input('Please enter the current twmpwrature in celsius - ') # we can also right as temp = float(input('Please enter the current twmpwrature in celsius - '))
# temp = float(temp)     # remember to change an input to a number because string cannot be in calculation

# # >=35 :  very hot
# # 25 - 35 : warm
# # 15 - 25 : good
# # <= 15 : freezing


# if(temp >= 35):
#     print('It is a very hot day')
# else:
#     if(temp >= 25 ):
#         print('I t is a warm day')
#     else:
#         if(temp >= 15):
#             print('It is a good temperature' )
#         else:
#             print('It is a freezing day')

#***********************************
#****************************
#********************
# # nested if else loop 

# temp = input('Please enter the current twmpwrature in celsius - ') # we can also right as temp = float(input('Please enter the current twmpwrature in celsius - '))
# temp = float(temp) 

# if(temp >= 35):                                         
#     print('It is a very hot day')
# elif(temp >= 25 ):
#     print('I t is a warm day')                      # we here use else + if that is elif so
# elif(temp >= 15):
#     print('It is a good temperature' )
# else:
#      print('It is a freezing day')

####*****************
#*******************
#*********ITERATIVE STATEMENT
#***************
# Iterative statements are used when certain tasks are to be excecuted multiple times.
#*******
# For - loop : When number iteration are  known
# While - loop : NO OF ITERATIONS ARE UNKOWN,  but stopping condition is known.
#*********************
#*************


#print your names 10 times

# for i in range(10):     # we are giving numbe of iteration.
#     print(i, 'Akash Anil')     #iterative repetitive task


# print('Using step Operator')
                
# for i in range(0,10,2):     # we are giving numbe of iteration.
#     print(i, 'Akash Anil')

# print(' step operator next example')



# #*
#  # range(start,end, stop) if stop is not metioned , it takes step 1
# #*



# for i in range(3,10,3):     # we are giving numbe of iteration.
#     print(i, 'Akash Anil')     

# print(' eg1')
# for i in range(3,10):     # we are giving numbe of iteration.
#     print(i, 'Akash Anil')    # 3,4,5,6,7,8,9 

# #giving step as a negative value


# print('giving step as a negative value')
# for i in range(10,3,-1):     # we are giving number of iteration.
#     print(i, 'Akash Anil')     #10 , 9,8,7,6,5,4


# #print all odd numbers < 50

# for i in range(1,50,2):
#     print(i)

# print('all odd number between 20 and 50')

# for i in range(21,50,2):
#     print(i)


num = 1
while( num < 10 ):
    print(num )
    num = num + 1
print('End of while loop ')


print(' odd Numbers below 50 ')

num = 1
while(num< 50):
    print(num)
    num = num + 2


print('Odd numbers between 20 and 50')

num = 21
while(num< 50):
    print(num)
    num = num + 2

#********************
# ******** we can use end = ','  for a straight and comma output
#***************
print(' odd Numbers below 50 ')

num = 1
while(num< 50):
    print(num, end=',')
    num = num + 2


print('\n', 'Odd numbers between 20 and 50')

num = 21
while(num< 50):
    print(num, end=',')
    num = num + 2

#************************
#logical operators in control flow 
#*******************************
#*********************
#**********
age = int(input('Please enter your age - '))
valid_id = input('Do you have a valid id (y/n) - ')

if(valid_id =='y'):
    valid_id = True     #only if the user types y
else:
    valid_id = False # your types anything other than y

#verifing eligibility to vote

print("we are checking your eligibility to vote")


if(age >=18):
    if(valid_id):
        print('You are eligible to vote')
    else:
        print('You are not eligible to vote')
        print('You need a valid id to be eligible to vote')

else:
    print('you are not eliggible to vote')
    print('you should be 18 or above to be eligible ')


print('**********************************')


#doing the same process using logical operators 

if(age>=18) and (valid_id):
    print('you are eligible to vote')
else:
    print('You are not eligible to vote')

