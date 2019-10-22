import os
import random_script

def main():

    #creates a dictionary to hold menu options
    menu = {}
    menu['1'] = "Generate Random Play Script"
    menu['2'] = "Generate Play Script by Play Style"
    menu['3'] = "Exit"
    #menu['4'] = "Exit"

    while True:

        os.system('clear')
        print('\t************ Playcalling Script Generator ************\n')

        options=menu.keys()
        sorted(options)

        #prints out menu keys using for loop
        for entry in options:
            print(entry, "-", menu[entry])

        selection = input("\nPlease select an option:")

        if selection == "1":

            random_script.random_script()
            continue

        elif selection == "2":

            random_script.style_script()
            continue

        elif selection == '3' or selection == 'q' or selection == 'Q':
            
            os.system('clear')
            break

        else:

            input("\nThe selection entered did not match one of the options. Please press ENTER to try again.")
            continue
if __name__ == '__main__':
    main()