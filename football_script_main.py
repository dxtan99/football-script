import os

def main():
    
    #clears the screen
    os.system('clear')

    print('Hello! Please choose an option listed below.')

    #creates a dictionary to hold menu options
    menu = {}
    menu['1'] = "Generate Random Play Script"
    menu['2'] = "Placeholder"
    menu['3'] = "Placeholder"
    menu['4'] = "Exit"

    while True:
        options=menu.keys()
        sorted(options)

        for entry in options:
            print(entry, menu[entry])

        selection = input("Please select an option.")

if __name__ == '__main__':
    main()