# #************************************************
# #*****************SET********************
# #***************************

# # declaraing a set

# # Method 1
# set1 = {}                     # This is not a seet but it is a Dictionary

# # Method 2
# set2 = {12,55,88,2026, True, 'BSNL',2026.0,2026, '2026'}

# # Method 3
# set3 = set()                 # set


# print(type(set1))                   #<class 'dict'>
# print(type(set2))                   #<class 'set'>
# print(type(set3))                   #<class 'set'>

# print(set2)         #Differnt from original set(NOT IN ORDER) . they dont store the crct index position like list, tuple or string
# # sET SUPPORTS ALL datatypes thst is hetrogenenous.
# #Duplicates are not allowed, and are deleted


# print('*****************************Functions***************************************')


# roll = {1,2,3,4,5,6}
# roll_odd = {1,3,5}
# roll_even = {2,4,6}
# random = {1,5,9,4}

# random.add(2026)        # adding a new number to the set with add()
# print('after adding ', random)


# print(random.difference(roll_odd))   # Present in random but not in roll_odd   {9, 2026, 4}
# print(roll_odd.difference(random))   # Present in roll odd but not in random    {3}

# print(roll.issuperset(roll_odd))            #TRUE
# print(roll.issubset(roll_odd))           # FALSE
# print(roll.issuperset(random))       # FALSE

# print(random.intersection(roll_even))      #{4}

# random.discard(5)
# print(random)


# # add()                   # Add one item
# # update()                # Add many items
# # remove()                # Remove (error if absent)
# # discard()               # Remove safely
# # pop()                   # Remove random item
# # clear()                 # Remove all
# # copy()                  # Copy set

# # union()                 # Combine sets
# # intersection()          # Common values
# # difference()            # A - B
# # symmetric_difference()  # Non-common values

# # issubset()              # Is inside another set?
# # issuperset()            # Contains another set?
# # isdisjoint()            # No common elements?


# # supports hetrogenenous datatype
# #cannot access data using index 
# #duplication are  not allowed
# # mutable


#***********************
#************DICTIONARY***********
#*************************

# # declaraing a set

# Method 1
dict1 = {}                     # This is not a seet but it is a Dictionary

# Method 2
dict2 = {'Key1': 'Value1', 'Key2': 'Value2', 8: 2027, True: 'Yes it works'}

# Method 3
dict3 = dict()                 # set

print(type(dict1))
print(type(dict2))
print(type(dict3))

print(dict2)   # dictionary have a key value pair
# a dictioneries keys and values can be of any datatype

sample_dictionary = {1: 'One', 0:'Zero', 1:'True', 1: 'ICT'} # keys are duplicate
print(sample_dictionary)
#key wil take the latest assigned value as its value
# {1: 'ICT', 0: 'Zero'} because 'ICT is the latest value given to key 1
#Duplication of keys are not allowed


print(dict2['Key2']) # dictonary[key] = valu assosiated with the 'key'


student_dict = {
    'name': 'Akash Anil',
    'age': 24,
    'university': 'MG',
    'district': 'Kottayam'
}

#printing the whole dicctionary

print('Whole Dictionary')
print(student_dict)

#print value alone 
print('Values are')
print (student_dict.values())

print('Items are ')
print(student_dict.items())  #dict_items([('name', 'Akash Anil'), ('age', 24), ('university', 'MG'), ('district', 'Kottayam')])
#we got ouput as multiple tuples


# Modifing values of Key
student_dict['university'] = 'Kerala University'
print(student_dict)


name_dict = {
    'name': 'Akash Anil',
    'phone': 9947091737,
    'email': 'spillerkey@gmail.com',
    "Home": 'Mundakayam'

}

print('Whole Dictionary')
print(name_dict)   #{'name': 'Akash Anil', 'phone': 9947091737, 'email': 'spillerkey@gmail.com', 'Home': 'Mundakayam'}

#print value alone 
print('Values are')
print (name_dict.values())

print('Items are ')
print(name_dict.items())  #dict_items([('name', 'Akash Anil'), ('phone', 9947091737), ('email', 'spillerkey@gmail.com'), ('Home', 'Mundakayam')])
#we got ouput as multiple tuples


# Modifing values of Key
key_dict = input('Enter the key value that is to be changed - ')
user_dict = input('Please enter the new value -')

name_dict[key_dict] = user_dict
print(name_dict)        #{'name': 'Akash Anil', 'phone': 8921267901, 'email': 'spillerkey@gmail.com', 'Home': 'Mundakayam'}


