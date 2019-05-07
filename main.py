# Code to check if left or right mouse buttons were pressed
import sys
import win32api
from datetime import datetime
import time
import keyboard
import logging
from write_csv import WriteCSV

"""
    This is the Main Script to Capture Mouse Clicks
    Process: 
    1.	Read Command Line Arguments
    2.	Setup Logging
    3.	Setup final/ folder path
    4.	Start Capturing Mouse Clicks
    5.  Write Number of Clicks in CSV file

    Usage: `python main.py UserName_DateTime`
"""

state_left = win32api.GetKeyState(0x01)  # Left button down = 0 or 1. Button up = -127 or -128
state_right = win32api.GetKeyState(0x02)  # Right button down = 0 or 1. Button up = -127 or -128

# Read Commandline Arguments
fullCmdArguments = sys.argv
# Skip first Argument i.e. `program_name.py`
argumentList = fullCmdArguments[1:]
# Read Further Arguments
username = argumentList[0]

# Define Folder Paths for Read - Write Operations
logging.basicConfig(filename='logs/' + username + '.log', level=logging.DEBUG)
final_folder_path = '../../Reports/' + username + '/final/'
logging.info('Final Folder Path:\t' + final_folder_path)

# list of column headers required in csv file
column_headers = ['DATETIME', 'LC', 'RC']
csv_filename = final_folder_path + username + '_Clicks'

w = WriteCSV()
w.write_header(csv_filename, column_headers)
print('listening to mouse click events...')

while True:
    a = win32api.GetKeyState(0x01)
    b = win32api.GetKeyState(0x02)
    if a != state_left:  # Button state changed
        state_left = a
        print(a)
        if a < 0:
            dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
            payload = {'DATETIME': str(dt), 'LC': 1, 'RC': 0}
            print(payload)
            logging.info(payload)
            w.write_data(csv_filename, payload)
            print('Left Button Pressed')
        else:
            print('Left Button Released')

    if b != state_right:  # Button state changed
        state_right = b
        print(b)
        if b < 0:
            dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
            payload = {'DATETIME': str(dt), 'LC': 0, 'RC': 1}
            print(payload)
            logging.info(payload)
            w.write_data(csv_filename, payload)
            print('Right Button Pressed')
        else:
            print('Right Button Released')
    time.sleep(0.001)
    if keyboard.is_pressed('q'):
        print('exiting program')
        logging.info('exiting program')
        break
