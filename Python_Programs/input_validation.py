#|/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\|#
# Author: Cole Baker
# Date: October, 15, 2018
# Description: Method one for using .isdigit() - Input Validation
#|/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\|#

import sys

def main():
    # Input and Variables
    per_pound_cost = 1.99
    flat_shipping_rate = 7.50
    pounds_of_oranges_string = input("Enter pounds of oranges to ship: ") #NOTE: Not converted to int() yet
    pounds_of_oranges = 0

    # Validation
    if pounds_of_oranges_string,isdigit() == False:
        print("You must enter a whole number of pounds requested.")
        sys.exit() #NOTE: Ends the program - Do not over use

    # Processing
    pounds_of_oranges = int(pounds_of_oranges_string)
    if pounds_of_oranges >= 100:
        flat_shipping_rate = flat_shipping_rate - 1.50
    
    total = pounds_of_oranges * per_pound_cost + flat_shipping_rate

    # Output
    print("\nOrder: {} pounds of oranges with ${:.2f} shipping.".format(pounds_of_oranges,flat_shipping_rate))
    print("Total: ${:.2f}".format(total))


if __name__ == "__main__":
    main()