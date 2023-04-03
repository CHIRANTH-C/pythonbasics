# Assignment 3
# 3. Suppose you are developing a program to simulate a restaurant ordering system. 
# You have a base class Menu that has a method called get_total() which calculates the total cost of all the menu items.
# You then have two child classes LunchMenu and DinnerMenu that inherit from Menu. 
# Both LunchMenu and DinnerMenu have a method called set_discount() which sets a rate of discount for all items for that particular menu, 
# so that their get_total() functions calculates the total of all the items and applies the discount.
# Your task is to create the Menu, LunchMenu, and DinnerMenu classes, 
# add the relevant methods, attributes and override the necessary methods so that they work as described above.

class menu: # create a menu class
    lunch_item_1 = 10 # set the price for lunch item 1
    lunch_item_2 = 30 # set the price for lunch item 2
    lunch_item_3 = 50 # set the price for lunch item 3
    dinner_item_1 = 20 # set the price for dinner item 1
    dinner_item_2 = 40 # set the price for dinner item 2
    dinner_item_3 = 60 # set the price for dinner item 3
    total_cost = 00 # set the total price to zeron
    discount = 0
    def get_total(self): # create a get total cost function
        total_cost = menu.lunch_item_1 + menu.lunch_item_2 + menu.lunch_item_3 + menu.dinner_item_1 + menu.dinner_item_2 + menu.dinner_item_3 # add price of all the item in menu and save it in total cost
        print("And the total is : "+str(total_cost)) # print the total cost

class LunchMenu(menu): # inherit the LunchMenu class from menu super class
    def get_total(self): # override the get_total metod
        total_cost = menu.lunch_item_1 + menu.lunch_item_2 + menu.lunch_item_3 # update the total_cost calculation formula for lunch menu
        total_cost_with_disc = total_cost - (total_cost * LunchMenu.discount)/100 # update the total_cost calculation formula for lunch menu with lunch discount
        print("And the total lunch cost is : "+str(total_cost_with_disc)) # print the total lunch cost
    def set_discount(self): # define the set discount for the lunch menu class
        menu.discount = 5 # set the discount for the menu
class DinnerMenu(menu): # inherit the DinnerMenu class from menu super class
    def get_total(self): # override the get_total metod
        total_cost = menu.dinner_item_1 + menu.dinner_item_2 + menu.dinner_item_3 # update the total_cost calculation formula for dinner menu
        total_cost_with_disc = total_cost - (total_cost * LunchMenu.discount)/100 # update the total_cost calculation formula for dinner menu with lunch discount
        print("And the total dinner cost is : "+str(total_cost_with_disc)) # print the total dinner cost
    def set_discount(self): # define the set discount for the dinner menu class
        menu.discount = 10 # set the discount for the menu

def my_restaurant():# define the my restaurant method
    print("Do you want to get lunch or dinner or both ?") # print for asking lunch option
    print("provide input 1 for lunch , 2 for dinner , 3 for both : ") # ask for menu option
    menu_option = int(input()) # get the menu option from the console
    if menu_option == 1: # if the menu option is 1
        my_lunch_order = LunchMenu() # create lunch order object
        my_lunch_order.set_discount() # set the discount of the lunch
        my_lunch_order.get_total() # get the total of the lunch
    elif menu_option == 2: # if the menu option is 2
        my_dinner_order = DinnerMenu() # create dinner order object
        my_dinner_order.set_discount() # set the discount of the dinner
        my_dinner_order.get_total() # get the total of the dinner
    elif menu_option == 3: # if the menu option is 3
        my_order = menu() # create menu order object
        my_order.get_total() # get total of the lunch
    else:
        print("chose the right menu please") # print to choose the right option
        my_restaurant() # call the restaurant function again


my_restaurant() # call the restaurant function again