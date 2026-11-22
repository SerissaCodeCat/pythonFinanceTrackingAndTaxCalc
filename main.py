# This program should take weekly financial updates from a user, store them in a database. 
# it will also ask for the tax brackets for federal and provingial tax, and keep a running total
# of the users income, business expenses, and tax owed come end of tax-year.

# This program MUST be able to run on a Linux machine.
# This program MUST be able to run in Wayland.
# This Program MUST be able to run on command line (i.e. a TUI)
# This Program MUST save data to a database.
# This Program MUST be able to run on a Desktop / laptop computer.
# This Program MUST be able to take user input of income, business expenses, Federal and Provincial tax brackets.
# This program MUST be able to calculate the tax owed by the user at the end of the tax year.
# This Program MUST be able to display the data in a table format.
# This program MUST be able to load data from a file. 
# This program SHOULD be able to run in X11. (i.e. not just wayland!)
# This program SHOULD be able to run on a Raspberry Pi.
# This Program SHOULD be able to run in a GUI.
# This Program SHOULD use only open source libraries.
# This Program SHOULD be able to display the data in Graph format.


import string
import pandas as pd
import PyQt6 as qt
from decimal import Decimal, getcontext 

# A functions that takes two intergers, and checks that the second one is 2 digits long, the first is put into the 
# Dollar / pound / main delimination of currency place. the second interget should be for the "pennies" place
def add_to_income( a, b ):
    """
    add income to the database. variable a is the dollar / pound / euro, etc. part. 
    where as the b variable is the pennies. 
    """
    print(f"the input amount to add to income is: {a}.{b}")
    print("This is a stub")

# A functions that takes two intergers, and checks that the second one is 2 digits long, the first is put into the 
# Dollar / pound / main delimination of currency place. the second interget should be for the "pennies" place
def add_to_expenses( a, b):
    """
    add expense to the database. variable b is the dollar / pound / euro, etc. part.
    were as b is the variable representing pennies.
    """
    print(f"the input amount to add to expenses is: {a}.{b}")
    print("This is a stub")

# The function that will write to the data-file with the date being a Key field.
# The function takes the date, the colum header name, and either adds the data to that row
# or makes the new row if one is not pressent. If the passed header is not pressent in the data-file
# the write request will be rejected.
def write_to_data_file(date, column_name, value):
    print(f"input date is {date}, the column name is {column_name}, and the value passed is {value}")
    print("This is a stub.")

# Function that creates the folder in the relative path to store the data file.
def create_folder_structure():
    print("This is a stub") 

# Function to check that the input value is a valid currency format.
def check_input_is_valid_currency(currency_to_check):
    #test that value is numerical and can be converted to a floating point value.
    try:
        converted_to_float = float(currency_to_check)
    except ValueError:
        print("please enter numeric values only, with a decimal point followed by 2 numerics, I.E \"3.50\" ")
        return False

    # check if currency contains a decimal point.
    if "." in currency_to_check:
        #reject if there is more than one decimal point.
        if currency_to_check.count(".") != 1:
            print("please enter a valid currency format.")
            return False
        else:
            income_before_decimal = currency_to_check.split(".")[0]
            income_after_decimal = currency_to_check.split(".")[1]
            if len(income_after_decimal) != 2:
                print(f"please enter a 2 number trailing amount, current value after decimal is {income_after_decimal} ")
                return False
            print(f"you have entered {income_before_decimal} DOLLARS, and {income_after_decimal} CENTS")
        return True
    else:
        print("Please enter a valid currency value. including the decimal.")
        return False

def check_if_date_to_write_currently_exists(date_to_check):
    print("This is a stub")

def main():
    print("Welcome to this tax calculator thingy.")
    print("This program will calculate your tax for the year.")
    print("First we need some information from you.")
    while True:
        income = input("Enter your income as numerical value: ")
        if check_input_is_valid_currency(income) == True:
            break
        continue
        
    income = float(income)
    while True:
        business_expenses = input("Enter your business expenses as a numerical value: ")
        if check_input_is_valid_currency(business_expenses) == True:
            break
        continue
    business_expenses = float(business_expenses)

if __name__ == "__main__":
    main()


