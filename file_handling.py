print('****************************************FILE HANDLING*********************************************************')



#
filepath = 'D:/PGP_AIML/Python/sample.txt'
relative_filepath = 'Python/sample.txt'


# we use the entire filepath to read a file
def read_file_filepath():
    file = open(filepath, 'r')          #assign a file in reading mode

    content = file.read()           #content of the file is assigned to 'content'
    print(content)

print('*********')


#trying using relative file path
def read_file_rel_filepath():
    file_1 = open(relative_filepath, 'r')
    content_1 = file_1.read() 
    print(content_1)
    print(type(content_1))              #a single string

#file.read()will return all the values as a single string




def read_line_by_line():
    file = open(relative_filepath, 'r')
    content = file.readline() 
    print(content)                          # read only the first line
    print(type(content)) 

read_line_by_line()




def read_lines():
    file = open(relative_filepath, 'r')
    content = file.readlines() 
    print(content)                      # reads all lines and populates the list content
    for line in content:
        print(line)
    print(type(content)) 

read_lines()
