import os
import random
import constants

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
				playType_selection_text = constants.playTypeList[playType_selection]

				#error checking
				#input(playType_selection_text)

				if playType_selection == 0:

					play_selection = constants.runList[random.randrange(len(constants.runList))]
					#input(play_selection)

				if playType_selection == 1:

					play_selection = constants.passList[random.randrange(len(constants.passList))]
					#input(play_selection)

				if playType_selection == 2:

					play_selection = constants.optionList[random.randrange(len(constants.optionList))]
					#input(play_selection)

				print('Play #{}: {}, {}'.format(counter, playType_selection_text, play_selection))

				counter = counter + 1

			input('\nPress ENTER to continue.')

		except ValueError:
			#try statement is needed for the case in which user does not input Q or q to quit and also does not input a number.
			input('\nThe selection entered did not match any options. Please press ENTER to try again.')

	return


def print_option2_title():

	os.system('clear')
	print('\t************ Playscript Generator By Style ************\n')

def probability_play_selection(run_percentage, pass_percentage, option_percentage):
	
	#makes sure that each of the passed numbers are ints and then converts to probability
	run_percentage_wt = int(run_percentage) * 0.1
	pass_percentage_wt = int(pass_percentage) * 0.1
	option_percentage_wt = int(option_percentage) * 0.1

	wt_list = [run_percentage_wt, pass_percentage_wt, option_percentage_wt]

	return random.choices(constants.playTypeList, wt_list)

def style_script():

	while True:

		print_option2_title()

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

					else:
						input('\nThe total percentage did not add up to 100. Press ENTER to try again.')
						value_error_check = 0
						break


				except ValueError:
					input('\nOne of the selections entered was not a number. Please press ENTER to try again.')
					value_error_check = 0
					break
					
			if value_error_check == 0:
				continue

			counter = 1
			''' error testing
			run_count = 0
			pass_count = 0
			option_count = 0
			'''

			while counter < num + 1:

				playType_selection_text = probability_play_selection(run_percentage_int, pass_percentage_int, option_percentage_int)[0]

				'''error testing
				input(playType_selection_text)'''

				if playType_selection_text == 'Run':
					play_selection = random.choice(constants.runList)

				if playType_selection_text == 'Pass':
					play_selection = random.choice(constants.passList)

				if playType_selection_text == 'Option':
					play_selection = random.choice(constants.optionList)

				if counter == 1:
					print("\n")

				print('Play #{}: {}, {}'.format(counter, playType_selection_text, play_selection))

				if counter == num:
					input('\nPress ENTER to continue.')

				counter += 1

				'''error testing
				if playType_selection_text == 'Run':
					run_count += 1
				if playType_selection_text == 'Pass':
					pass_count += 1
				if playType_selection_text == 'Option':
					option_count += 1


			input ('runs: {}, passes: {}, options: {}'.format(run_count, pass_count, option_count))'''

		except ValueError:
			input('\nThe selection entered did not match any options. Please press ENTER to try again.')














