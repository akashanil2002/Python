# # List is a datatype which stores a collection of values.
# # Since it is a combination of other data types (int, float,string, boolean ), we call it a derrived datatypes


# #There is no resticttion in terms of datatype in a list 
# # A list can contain various amount of data . Hetrogenous

# #unerstanfd jargon


# name = ""
# name = "Akash Anil"
# print(type(name))

# #declaring a list

# #Method 1
# lst_name =[]                    #empty list
# print(type(lst_name))

# #Method 2
# lst_name2 = ['vishnu', 'Akash' , 'Ajith ']           # list with some values in it
# print(type(lst_name2))

# #METHOD 3
# lst_name3 = list()                     # just a list
# print(type(lst_name3))


# #Fetching values from index from a list.
# print(lst_name2[0])
# print(lst_name2[1])
# print(lst_name2[2])

# # print(lst_name2[5])           # this will error of index out of range


# # List containg multiple datatypes

# # personal info as a list : name, age, graduation year, university, height, friends
# amar_info =['Amar', 22, 2026, 'CUSAT', 172.5, lst_name2]               # list can contain any datatype list inside a list
# print(type(amar_info))

# print(amar_info[0])                      #dispaly values at the index 0
# print(type(amar_info[0]))                # display the datatype of index 0

# print(amar_info[1])                     #dispaly values at the index
# print(type(amar_info[1]))               # display the datatype of index 1

# print(amar_info[2])                     #dispaly values at the index 1
# print(type(amar_info[2]))               # display the datatype of index 2

# print(amar_info[3])                      #dispaly values at the index 3
# print(type(amar_info[3]))               # display the datatype of index 3

# print(amar_info[4])                     #dispaly values at the index
# print(type(amar_info[4]))               # display the datatype of index 4

# print(amar_info[5])                     #dispaly values at the index 5
# print(type(amar_info[5]))               # display the datatype of index 5


#*************
#***********
# Adding two list together

list_1 = [1,2,3]
list_2 = [False, True,False]

# list_1 = list_1 + list_2                    # adding list, we assign a new value to list so the output list will give new added list_1.
# # above is callled list concatenation

# print(list)                             # printing the new list

lst_name2 = ['Arjun', 'Akash' , 'Gowtham'] 

print(list_1)   #unsorted
list_1.sort()       #sorting is done
print(list_1)       #Sorted             [1,2,3]  acending order

print(lst_name2)    #Unsorted
lst_name2.sort()    #sorig is  done
print(lst_name2)    #sorting

list_1.sort(reverse= True)        # sort the other way (descending)
print(list_1)                   # [3,2,1]


# lst_name2 = ['Akash', 'Arjun', 'Gowtham' 3, 2, 1]

lst_name2.extend(list_1)                     # gets extended with value of list_1
print(lst_name2)          # ['Akash', 'Arjun', 'Gowtham', 3, 2, 1]
print(lst_name2[3])             # output will be 3

list_2.append(list_1)           # list_1 was added as the last value of list_2
print(list_2)                   #[False, True, False, [3, 2, 1]]
print(list_2[3])                   # output : [3, 2, 1]


list_1.append('A')
print(list_1)                   # output :[ 3, 2, 1, 'A']

list_1.reverse()                #reversing a list
print(list_1)                   # output : ['A', 1, 2, 3]

print('The no of times false appear in the list = ',list_2.count(False))         # check for count of value false
print('The no of times True appear in the list = ',list_2.count(True))           # check for count of value True
print('The no of times X appear in the list = ',list_2.count('X'))                   # check for count of value X
print(list_2)

#value at last index
print(list_2[-1])

#Fetch number of items in the list
len(list_2)
print('Totsl number of elements in ', list_2, 'is', len(list_2))

# Value at last index
print(list_2[-2])
print(list_2[len(list_2) -2])

print('***************************************************************************')

print('Before clear')
print(list_2)                   #[False, True, False, ['A', 1, 2, 3]]

list_2.clear()                  #clears all value from th variable

print('After clear')
print(list_2)                   # output : []

print('************************************************************')



# target #[3, 2 ,1 ,'A']
#IN ORDER TO DO  [3, 2 ,1 ,'A'] TO [3, 2 ,100, 1 ,'A']
# IS inversting 100

print(list_1)     

list_1.insert(2,100)                                    # Inserting 100 at index 2
print('After inserting the value ', list_1)             # After inserting the value  ['A', 1, 100, 2, 3]

print('************************************************************')


print('Before moving 3 - ', list_1)      # Before moving 3 -  ['A', 1, 100, 2, 3]
list_1.remove(3)
print('After removing 3 ', list_1)          #Before moving 3 -  ['A', 1, 100, 2, 3]


print('************************************************************')


list_1.pop()
print(list_1)

# queue : first in first lot
# stack : last at first

print('************************************************************')

#*************
#***********
#****Tuple***

# also cointain hetrogeous datatype.. the differecence beteween tuple and list is bracket 
tuple1 = ()
tuple2 = (2026, "nov", 3.75, False, [8, True, 9.8])
tuple3 = tuple()

print(type(tuple1))   
print(type(tuple2))
print(type(tuple3))

#output
# <class 'tuple'>
# <class 'tuple'>
# <class 'tuple'>

print(tuple2[2])                        #we can fetch using index : 3.75 


print(tuple2.count('nov'))
print(tuple2.index('nov'))


# once a tuple is we cannot make changes to it.
# list -> mutable   ( can make changes to the value)
# Tuple -> immutabble ( cannot make changes to the value)

del(tuple2)             # THAT MEANS WE ARE DELETING variable tuble2
del(list_2)             #deleting variable of list 2

# print(tuple2)                       # NameError: name 'tuple2' is not defined. Did you mean: 'tuple1'?
# print(list_2)                          # NameError: name 'list_2' is not defined. Did you mean: 'list_1'?