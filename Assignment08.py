# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
#EChapman,3.3.2021, added Starter Assignment08
#EChapman, 3.7.2021,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #
import pickle
# Data -------------------------------------------------------------------- #

file_name = "products.dat" #Changed from txt to dat for pickling
list_of_product_objects = []

class Product(object):
    """Stores data about a product:

    properties:
        product_name: (string) with the product  name
        product_price: (float) with the product standard price
    methods:
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        EChapman, 3.7.2021,Modified code to complete assignment 8
    """

    # --------------fields----------------------
    StrProduct = ""
    FloatPrice = 0
    # ---------------Constructor---------------
    def __init__(self, product='', price=0):
        print("This is a class")
        self.StrProduct = product  #Attribute
        self.FloatPrice = price   #Attribute

    @property
    def product_name(self):  # accessor
        return str(self.product_name)

    @property
    def product_price(self):  # accessor
        return float(self.product_price)

# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):

        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
         EChapman, 3.6.2021, added to FileProcessor
    """

    @staticmethod
    def read_data_from_file(file_name, list_of_product_objects):
        # Reads data from the binary file
        try:
            f = open(file_name, "rb")
            freshly_pickled = pickle.load(f)
            list_of_product_objects += freshly_pickled
            f.close()
        except:
            print("file not found")

    @staticmethod
    def save_data_to_file(file_name, list_of_product_objects):    #added list_of
        """Writes data to a binary file"""
        file = open(file_name, "wb")
        b = pickle.dump(list_of_product_objects, file)
        file.close()

# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    @staticmethod
    def print_menu_tasks():
        """display menu of choices"""
        print(
            '''
           Menu of Options
           1) Display Current Data in list of products
           2) Add Data to list of products
           3) Save Data to File and exit program
           ''')
        return "\n"

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user"""
        choice = str(input("Which option would you like to perform? [1 to 3] - "))
        return choice

    @staticmethod
    def input_get_product_data():
        """"get product data from user"""
        product = str(input("Enter a product: "))
        price = float(input("Enter it\'s price: "))
        new_row = [product, price]
        list_of_product_objects.append(new_row)

    @staticmethod
    def print_list_products(list_of_product_objects):  # WORKS
        try:
            for row in list_of_product_objects:
                print(row)
        except:
            print("objects not found")
        return "\n"

# Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #
FileProcessor.read_data_from_file(file_name,list_of_product_objects)
# Load data from file into a list of product objects when script starts
print("***** Previous Data ******")
IO.print_list_products(list_of_product_objects)
print("****************")
while True:
    IO.print_menu_tasks()  # Show user a menu of options
    user_choice = IO.input_menu_choice()  # Get user's menu option choice
    if user_choice.strip() == '1':
        """Show user current data in the list of product objects"""
        print("*** Displaying Current Data: ***")
        IO.print_list_products(list_of_product_objects)
        continue

    elif user_choice.strip() == '2':  # Let user add data to the list of product objects
        IO.input_get_product_data()
        print("*** Displaying Current Data: ***")
        IO.print_list_products(list_of_product_objects)  # WORKS 3.6
        continue

    elif user_choice.strip() == '3':
        print("Saving data to file")
        print("...")
        FileProcessor.save_data_to_file(file_name, list_of_product_objects)
        print("Goodbye")
        break

# Main Body of Script  ---------------------------------------------------- #

