# task 1  

first_name = input("First Name: ")
last_name = input("Last Name: ")

def check_name_length(name): 
    length = len(name)
    return length 

if check_name_length(first_name) <= 2: 
    print("ERROR: Length of first name is too short")
if check_name_length(last_name) <= 2: 
    print("ERROR: Length of last name is too short")
else: 
    print("Names look good")

