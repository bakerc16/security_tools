#|/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\|#
# Author: Cole Baker
# Date: October, 29, 2018
# Description: Hogwarts sorting hat with loop
#|/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\|#

import random
import sys
import re

def assign_house(in_house):
    is_assigned = "unassigned"

    if in_house.upper() == "POTTER":
        final_assigned = "Gryffindor"
    elif in_house.upper() == "MALFOY":
        final_assigned = "Slytherin"
    else:
        is_assigned_number = random.randint(1,4)
        if is_assigned_number == 1:
            final_assigned = "Gryffindor"
        elif is_assigned_number == 2:
            final_assigned = "Hufflepuff" 
        elif is_assigned_number == 3:
            final_assigned = "Ravenclaw"
        elif is_assigned_number == 4:
            final_assigned = "Slytherin"

    return final_assigned

def main():
    # Variables for house counter
    gryffindor_count = 0 
    slytherin_count = 0
    hufflepuff_count = 0
    ravenclaw_count = 0

    # Variables for house list
    gryffindor_list = []
    slytherin_list = []
    hufflepuff_list = []
    ravenclaw_list = []

    last_name = ""
    while last_name.upper() != "Q":

        last_name = input("What is the wearers name? (First letter capital): ")
        validation_pattern = re.compile("[A-Z][a-z]{1,24}")

        if last_name.upper() != "Q":
        
            # Validation
            if validation_pattern.fullmatch(last_name) == None:
                print("You must enter a last name with at least 1 upper case letter and at least 1 lower case right after.")
                sys.exit() #TODO Make Loop


            # Processing

            final_assigned = assign_house(last_name)

            if final_assigned ==  "Gryffindor":
                gryffindor_count = gryffindor_count + 1
                gryffindor_list.append(last_name)
            elif final_assigned == "Hufflepuff":
                hufflepuff_count = hufflepuff_count + 1
                hufflepuff_list.append(last_name)
            elif final_assigned == "Ravenclaw":
                ravenclaw_count = ravenclaw_count + 1
                ravenclaw_list.append(last_name)
            elif final_assigned == "Slytherin":
                slytherin_count = slytherin_count + 1
                slytherin_list.append(last_name)

            gryffindor_list.sort()
            slytherin_list.sort()
            hufflepuff_list.sort()
            ravenclaw_list.sort()
            
            # Output
            print("You have been assigned to {} house!".format(final_assigned))

    # print()
    # print("Numbrt of students in Gryffindor: {}".format(gryffindor_count))
    # print("Numbrt of students in Hufflepuff: {}".format(hufflepuff_count))
    # print("Numbrt of students in Ravenclaw: {}".format(ravenclaw_count))
    # print("Numbrt of students in Slytherin: {}".format(slytherin_count))
    print("-" * 50)

    # Print for house list
    print("The sorted list for the {} students in Griffindor: ".format(gryffindor_count))
    for steps in range(len(gryffindor_list)):
        print(gryffindor_list[steps])

    print("-" * 50)

    print("The sorted list for the {} students in Hufflepuff: ".format(hufflepuff_count))
    for steps in range(len(hufflepuff_list)):
        print(hufflepuff_list[steps])

    print("-" * 50)

    print("The sorted list for the {} students in Ravenclaw: ".format(ravenclaw_count))
    for steps in range(len(ravenclaw_list)):
        print(ravenclaw_list[steps])

    print("-" * 50)

    print("The sorted list for the {} students in Slytherin: ".format(slytherin_count))
    for steps in range(len(slytherin_list)):
        print(slytherin_list[steps])

    print("-" * 50)


if __name__ == "__main__":
    main()