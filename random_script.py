import os
import random

#Idea: Make 3 lists that each contain the different play categories: Run, Pass, Option. Within those lists,
#you could have the types of runs, types of passes, types of options, etc.
#The program would first pick number between 1 and 3 to decide if it's run/pass/option then randomly choose out of that list.
#All of this is in a loop with a counter for the number of plays selected.

#run list: inside, outside, pitch, counter, draw, fb run, qb run
#pass list: quick, standard, shotgun, play action, screen
#option list: read, speed, inverted veer, shovel, load, triple, QB slot, midline

playTypeList = ['Run', 'Pass', 'Option']
runList = ['Inside', 'Outside', 'Pitch', 'Counter', 'Draw', 'FB run']
passList = ['Quick', 'Standard', 'Shotgun', 'Play Action', 'Screen']
optionList = ['Read', 'Speed', 'Inverted Veer', 'Shovel', 'Load', 'Triple', 'QB Slot', 'Midline']

def random_script():

	while True:

		os.system('clear')
		print('\t************ Random Playscript Generator ************\n')

		numPlays = input('Enter the number of plays you would like to generate or "Q" to quit:')

		if numPlays == 'Q' or numPlays == 'q':
			break

		try:
			num = int(numPlays)
			input('\n{} was the selected number of random plays. Press ENTER to generate random play list.\n'.format(num))

			#loop through the random plays generated using the randrange() function
			counter = 1
			while counter < num + 1:

				playType_selection = random.randrange(3)
				playType_selection_text = playTypeList[playType_selection]

				#error checking
				#input(playType_selection_text)

				if playType_selection == 0:

					play_selection = runList[random.randrange(len(runList))]
					#input(play_selection)

				if playType_selection == 1:

					play_selection = passList[random.randrange(len(passList))]
					#input(play_selection)

				if playType_selection == 2:

					play_selection = optionList[random.randrange(len(optionList))]
					#input(play_selection)

				print('play #{}: {}, {}'.format(counter, playType_selection_text, play_selection))

				counter = counter + 1

			input('\nPress ENTER to continue.')

		except ValueError:
			#try statement is needed for the case in which user does not input Q or q to quit and also does not input a number.
			input('\nThe selection entered did not match any options. Please press ENTER to try again.')

	return

def style_script():

	while True:

		os.system('clear')
		print('\t************ Random Playscript Generator ************\n')

		numPlays = input('Enter the number of plays you would like to generate or "Q" to quit:')

		if numPlays == 'Q' or numPlays == 'q':
			break

		value_error_check = 1

		try:
			num = int(numPlays)
			print('\n{} was the selected number of plays.'.format(numPlays))

			total_percentage = 0

			while total_percentage != 100:

				run_percentage = input('\nPlease enter percentage of run plays:')
				pass_percentage = input('Please enter percentage of pass plays:')
				option_percentage = input('Please enter percentage of option plays:')

				try:
					run_percentage_int = int(run_percentage)
					pass_percentage_int = int(pass_percentage)
					option_percentage_int = int(option_percentage)

					total_percentage = run_percentage_int + pass_percentage_int + option_percentage_int

					if total_percentage == 100:
						break


				except ValueError:
					input('\nOne of the selections entered was not a number. Please press ENTER to try again.')
					value_error_check = 0
					break
					
			if value_error_check == 0:
				continue

			input('Error stop check')

		except ValueError:
			input('\nThe selection entered did not match any options. Please press ENTER to try again.')














