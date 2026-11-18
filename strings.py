#***********************Slicing
#***************************
#**********

S1 = 'Trivandrum'
print(S1[-4])        # will display 7thn character
print(S1[-6])

print(S1[0:5])     #Slicing start index = 0, end indeex = 4. 'TRIVA'
print(S1[6:10])     #Slicing 'DRUM'

# print(S1[10])    ** Error will pop up like out of range 

print(S1[4:7])       # slicing 'AND'

print(S1[:5])      # start index to till 5                
print(S1[6:])      # from the 6th index till the last index

print(S1[0:5:2]) # step slicing TRIVANDRUM 0= 'T' THEN SLICE BY +2 THAT 'TI' AND AGAIN +2 THAT IS 'TIA'. AND IT WILL STOP HERE BEACUSE THE END INDEX IS 5 THAT WE HAVE GIVEN IN THE MIDDLE. 
print(S1[:5:2])   # EMPTY BEFORE COLON IS CONSIDERED AS 0 SO AGAIN SAME OUTPUT.
print(S1[0:8:3]) # STEP UP SLICED +3 TILL INDEX 8 AS END.

string_demo = "join our official programs in kerala's IT park."
#*****************************Syntax: string[start:stop:step]*********
#************************************
print(string_demo[5:])  #Skip the first 5 characters and print everything else
print(string_demo[5::2]) #Start at index 5, go to the end, and skip every other character (step of 2)

#Reverse the string
print(S1[::-1]) # Reverses the entire string (Starts at the end and steps backward by 1)
print(S1[::-2]) # reverse the entire string ( starts at the end and stops backward by 2)
print("******************")

#*********************************************
#****************Functions*************
#****************************

print(S1)
print(S1.lower())  # Return a copy of the string converted to lowercase.
print(S1.upper())   # Return a copy of the string converted to uppercase.
print(S1.swapcase()) # Convert uppercase characters to lowercase and lowercase characters to uppercase.
print(S1.capitalize()) # make the first character have upper case and the rest lower case.

