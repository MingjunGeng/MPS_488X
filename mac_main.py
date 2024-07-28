import sys
import os
import time
from device.dev_mps488X import MPS_488X


def run_menu(menu, parent=None):
    while True:
        print_menu(menu)

        #if parent:
        #    print("99. go back to parent")
        getin = input("Plase enter you  choice: ")

        #if parent and getin =='99':
        #    return

        if not getin.isnumeric() or  int(getin) >= len(menu['options']):
            print()
            print("Invalid choice, please try again.")
            print()
            continue
            
        menu['options'][int(getin)]['command']()


def print_menu(menu):
    print(menu['title'])
    for i, option in enumerate(menu['options']):
        #print(i, option['text'])
        print(f"{i}. {option['text']}")
    print()

mps_488X = MPS_488X()
#print("test", mps_488X.test())
COMMAND = 'command'
main_menu = {
    'title':  'Main Menu',
    'options': [
        {'type': COMMAND, 'text': ' Update Device Normal Mode Fireware', 'command': mps_488X.Normal_Mode_Update },
        {'type': COMMAND, 'text': ' Update Device Recovery Mode Fireware', 'command': mps_488X.Recovery_Mode_Update},
        {'type': COMMAND, 'text': ' Change Mac Sddress and Serial Number', 'command': mps_488X.Mac_Update},
        {'type': COMMAND, 'text': ' Change Mac Sddress and Serial Number', 'command': mps_488X.Mac_Check},
        {'type': COMMAND, 'text': ' EXIT', 'command': mps_488X.exit},
        ]
    }
run_menu(main_menu)
