#|/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\|#
# Author: Cole Baker
# Date Started: November, 6, 2018
# Date Finished: November, 13, 2018
# Description: Program 1 - Design and write a program that accepts the number of hours worked on each of five 
# work days from the user, then displays different information calculated about those entries as output. 
# Your solution should demonstrate an understanding of how to apply list and looping concepts in a program that should:
# •	Include a flowchart that clearly shows all the paths of execution that will exist within your designed solution 
#   to this problem.
# •	Prompt the user to enter the five daily hours worked amounts, and store them in the program. 
# •	Determine the day(s) on which the most hours were worked and display the day(s) and hours onscreen. 
# •	Calculate and display both the total and the daily average of hours worked.
# •	Display a list of all days that had insufficient hours, which is defined as less than 7 hours.
#|/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\|#

import re

#Function for average hours
def hours_worked(in_total_hours):
    hours = in_total_hours / 5

    return hours


def main():
    # Input and Variables
    hours_per_week = []
    highest_number = 0
    total_hours = ""

    #Loop for hours inputted
    for steps in range(5):
        current_day = input("Enter hours worked on day #{}: ".format(steps + 1))

    #Valiadtion
        while current_day.isdigit() == False:
            print("Please enter a number")
            current_day = input("Enter hours worked on day #{}: ".format(steps + 1))
        hours_per_week.append(int(current_day))

    # Processing
    # Loop for determining highest number of hours
    for hours in hours_per_week:
        if hours > highest_number:
            highest_number = hours

    # Determing total hours
    total_hours = sum(hours_per_week)

    # Calling function for determing average hours
    average_hours = hours_worked(total_hours)

    # Output
    print("-" * 50)
    # Print for the most hours worked using for loop
    print("You worked the most hours on: ")
    for steps in range(len(hours_per_week)):
        if hours_per_week[steps] == highest_number:
            print("Day #{}: when you worked {} hours." .format(steps + 1, highest_number))
    print("-" * 50)
    # Print for total hours and average hours
    print("Total number of hours you worked this week: {}".format(total_hours))
    print("Average number of hours you worked was: {:.1f} ".format(average_hours))
    print("-" * 50)
    # Print for days you slacked off using for loop
    print("Days you slacked off(i.e. worked less than 7 hours): ")
    for less_then_seven in range(len(hours_per_week)):
        if hours_per_week[less_then_seven] < 7:
            print("Day {}, Hours: {}".format(less_then_seven + 1,hours_per_week[less_then_seven]))


if __name__ == "__main__":
    main()