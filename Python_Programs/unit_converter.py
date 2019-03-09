#|/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\|#
# Author: Cole Baker
# Date: (Start date - Sept, 17, 2018) (Finish date - Sept, 20, 2018)
# Due Date: Sept, 25, 2018
# Description: Write a console program that converts a weight given in tons 
# (imperial), stones, pounds, and ounces to the metric equivalent in metric tons, kilograms, and grams. 
# Begin by designing your solution to this problem in pseudocode, which will be submitted along with the program.  
#|/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\|#

def main():
    # Input and Variables
    print("Imperial To Metric Conversion \n")
    tons = input("Enter the number of tons: ")
    stones = input("Enter the number of stones: ")
    pounds = input("Enter the number of pounds: ")
    ounces = input("Enter the number of ounces: ")


    # Processing
    total_ounces = (35840 * int(tons)) + (224 * int(stones)) + (16 * int(pounds)) + int(ounces)
    total_kilos = int(total_ounces/35.275) # Or get the correct number of kilos
    metric_tons = int(total_kilos/1000)
    kilos = int(total_kilos % 1000)
    total_grams = int(total_kilos * 1000000 % 1000000) / 1000

    # Output
    print("The metric weight is {} metric tons, {} kilos, and {:.1f} grams,".format(metric_tons, kilos, total_grams))


if __name__ == "__main__":
    main()