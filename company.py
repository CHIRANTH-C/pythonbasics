# Assignment 2
# 2. Create an Employee class that has Name, position, number of working days 
# and hourly pay as the attributes. Write the hourly pay to be set as a hidden variable.
# It should have 3 functions:
# 1. get_employee_details(): that prints all name, position and number of working days.
# 2. set_hourly_rate()
# 3. calculate_total_payout() assuming the employee works 8 hours a day, 
# calculate the total pay earned by the employee.
# Create a few objects to demonstrate the class attributes and methods.
# Comment your code to explain the steps.

class employee: # define a class by name employee
    name = "" # create name attribute and initialise it by empty string
    position = "" # create position attribute and initialise it by empty string
    no_of_working_days = 0 # create no_of_working_days attribute and initialise it by 0
    __hourly_pay = 0 # create __hourly_pay attribute and initialise it by 0

    def get_employee_details(self): # create a func for employee class that prints employee informations
        print("Employee name is : " + self.name) # statement to print the employee name
        print("Employee position is : " + self.position) # statement to print the employee position
        print("Number of working days of employee is : " + str(self.no_of_working_days)) # statement to print no of working days of the employee
    
    def set_hourly_rate(self , sallary): # create a func for employee class with sallary as a parameter
        self.__hourly_pay = sallary # set the hourly payed sallary of the employee
    
    def calculate_total_payout(self): # create a func for employee class to calculate total payout of the employee
        total_pay_earned = 8 * self.__hourly_pay * self.no_of_working_days # calculate the total payout and assign it to total_pay_earned
        return total_pay_earned # return total_pay_earned


emp_1 = employee() # create an emp_1 object
emp_1.name = input("Please provide employee 1 name : ") # fetch the employee name from te console and save it in emp_1.name
emp_1.position = input("Please provide the role of the employee : ") # fetch the employee position from the console and save it in emp_1.position
emp_1.no_of_working_days = int(input("provide the number of working days in this month : ")) # fetch the number of working days of the employee and save it in emp_1.no_of_working_days
emp_1.set_hourly_rate(int(input("What is the sallary of the employee per hour ? "))) # fetch the per day sallary of the employee ans set the __hourly_pay of the employee
emp_1.get_employee_details() # call the get_employee_details() metod to print the details of the employee
sallay = emp_1.calculate_total_payout() # call the calculate_total_payout() of the emp_1 and store the sallary in sallay variable
print("Employee : "+emp_1.name+'\'s '+"Sallary "+"is : "+str(sallay)) # print the sallary of the employee 1

emp_2 = employee() # create an emp_2 object
emp_2.name = input("Please provide employee 1 name : ") # fetch the employee name from te console and save it in emp_2.name
emp_2.position = input("Please provide the role of the employee : ") # fetch the employee position from the console and save it in emp_2.position
emp_2.no_of_working_days = int(input("provide the number of working days in this month : ")) # fetch the number of working days of the employee and save it in emp_2.no_of_working_days
emp_2.set_hourly_rate(int(input("What is the sallary of the employee per hour ? "))) # fetch the per day sallary of the employee ans set the __hourly_pay of the employee
emp_2.get_employee_details() # call the get_employee_details() metod to print the details of the employee
sallay = emp_2.calculate_total_payout() # call the calculate_total_payout() of the emp_2 and store the sallary in sallay variable
print("Employee : "+emp_2.name+'\'s '+"Sallary "+"is : "+str(sallay)) # print the sallary of the employee 2