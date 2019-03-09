#|/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\|#
# Author: Cole Baker
# Date: November, 19, 2018
# Description: Note taker sent to file
#|/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\|#

import datetime

def main():
    new_note = ""
    file_name = "C:\\Users\\baker\\OneDrive\\Documents\\NSCC Semester 1\\Programming for Security\\Github Repository\\prog1015_cb\\InClass\\Nov_19\\notes.txt"
    access_mode = "a"

    # Open output file
    file_handle = open(file_name,access_mode)

    while new_note.upper() != "Q":
        new_note = input("Enter a note text ('Q' to quit): ")
        if new_note.upper() != "Q":
            date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
            file_handle.write("{},\n-{}\n".format(date,new_note))


    # Processing
    file_handle.close()

    # Output



if __name__ == "__main__":
    main()