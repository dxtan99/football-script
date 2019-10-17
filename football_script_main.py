import os
import random_script

def main():

    #creates a dictionary to hold menu options
    menu = {}
    menu['1'] = "Generate Random Play Script"
    menu['2'] = "Generate Play Script by Play Style"
    menu['3'] = "Placeholder"
    menu['4'] = "Exit"

    while True:

        os.system('clear')
        print('Hello! Please choose an option listed below.')

        options=menu.keys()
        sorted(options)

        #prints out menu keys using for loop
        for entry in options:
            print(entry, menu[entry])

        selection = input("Please select an option:")

        if selection == "1":

            random_script.random_script()
            continue

        if selection == '4':

            break
            
if __name__ == '__main__':
    main()