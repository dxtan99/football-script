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