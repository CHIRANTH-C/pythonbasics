# Assignment 1
# 1. Write a function, persistence, that takes in a positive parameter num and returns 
# its multiplicative persistence, which is the number of times you must multiply the digits 
# in num until you reach a single digit.
# For example (Input --> Output):
# 39 --> 3 (because 3*9 = 27, 2*7 = 14, 1*4 = 4 and 4 has only one digit)
# 999 --> 4 (because 9*9*9 = 729, 7*2*9 = 126, 1*2*6 = 12, and finally 1*2 = 2)
# 4 --> 0 (because 4 is already a one-digit number)

def mul_persistance(number): # define the function to take input number 
    pers_value = 0 # initialise the persistance value to 0
    input_number = int(number) # get the number from console
    print("the number to be multiplied is : "+number) # print the input number
    while input_number >= 10: # looping untill the input number is less that 10
        pers_value += 1 # increament the persistance value
        input_number = mul_nos_of_this(input_number) # save the number to input_number variable
    return pers_value # retunr the persistance value

def mul_nos_of_this(input_number): # define the function to multiple all the numbers in the input number
    mul_value = 1 # initialise the mul value to 1
    for i in str(input_number): # itterate over the input number as a string
        mul_value = mul_value * int(i) # multiple all the numbers in the input number
    return mul_value # return multiplied value

pers_value = mul_persistance(input("Enter the number to find its mul persistance value : ")) # call the mul_persistance and store the persistance value in pers_value
print(pers_value) # print the pers_value in console