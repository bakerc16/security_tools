#|/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/|#
# Author: Cole Baker
# Start Date: October, 16, 2018
# Finished Date: October, 22, 2018
# Description: Program 1 - A landscaping company needs a program that computes the price of landscaping for a 
# new housing development. Work orders are based on: address, plot length and width in feet, type of grass 
# (“fescue”, “bentgrass” or “campus”), and number of trees. The price is computed as follows:  
# - There is a base labour charge of $1000. 
# -	If the surface (length * width) is over 5000 square feet, add $500. 
# -	The cost is calculated per square foot. If the grass is “fescue” the cost is $0.05; for “bentgrass” it is $0.02; “campus” is $0.01. 
# -	Each tree requested has a $100 charge. 
# First, create a flowchart that clearly shows all the paths of execution that will exist within your designed solution 
# to this problem. Write a console application that will input the address, property length and width, 
# type of grass and number of trees, and then output the corresponding price.
# Your solution must contain examples demonstrating your understanding of appropriate use of functions and core 
# assignment concepts (decision structures).
#|/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/|#
import re
import sys

    #Function for validating inputs on Address, Depth, Width, and Trees
def validation(in_number):
    validation_pattern = re.compile("\d{1,4}") #Validation set to allow for entries up to 9999

    if validation_pattern.fullmatch(in_number) == None:
        print("You must enter a number between 0 - 9999.")
        sys.exit()
    else:
        in_number = int(in_number)

    return in_number

def main():
    # Inputs with Input Validation
    print("Landscaping Cost Summary")
    print()
    address = input("What is the house number? ")
    address = validation(address)
    print()
    depth = input("What is the depth of the property? ")
    depth = validation(depth)
    print()
    width = input("What is the width of the property? ")
    width = validation(width)
    print()
    grass_type = input("What type of grass (fescue, bentgrass or campus)? ")
    print()
    trees = input("Enter number of trees requested: ")
    trees = validation(trees)
    print()

    # Variables
    labour_cost = 1000   
    tree_cost = 100

    # Processing
    surface_area = depth * width 

    #To determine cost of grass based on input
    if grass_type.upper() == "FESCUE":
        grass_cost = 0.05
    elif grass_type.upper() == "BENTGRASS":
        grass_cost = 0.02
    elif grass_type.upper() == "CAMPUS":
        grass_cost = 0.01

    #To calculate the total cost for grass
    total_area_cost = (surface_area * grass_cost)

    #For if surface area is over 5000, add $500
    if surface_area > 5000:
        total_area_cost = total_area_cost + 500

    #To calculate the total cost for trees
    total_tree_cost = trees * tree_cost

    #To calcualate the total cost for all landscaping
    total_cost = labour_cost + total_area_cost + total_tree_cost

    # Formatted Output
    print("Total cost for house {} is: ${:.2f}".format(address,total_cost))


if __name__ == "__main__":
    main()