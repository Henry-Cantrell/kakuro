from determine_if_choices_win import *

def selectChoices(gmDict, selectionsDictionary):

	#This generates possible solutions based on whether the columns add to the tl/tr values of the positional list

	for x in range(1, 10):
		for y in range(1,10):
			if x + y == gmDict['positional_list'][0]:
				selectionsDictionary['solutionListTopLeft'].append([x, y])
			elif x + y == gmDict['positional_list'][1]:
				selectionsDictionary['solutionListTopRight'].append([x, y])

	for i in selectionsDictionary['solutionListTopLeft']:
		for n in selectionsDictionary['solutionListTopRight']:
			if winnerEval(i, n, gmDict):
				gmDict['choices_list'][0] = i[0]
				gmDict['choices_list'][1] = n[0]
				gmDict['choices_list'][2] = i[1]
				gmDict['choices_list'][3] = n[1]
				print('The computer choices: ')
				print(gmDict['choices_list'])

	print('Here is the sl/tl: ')
	print(selectionsDictionary['solutionListTopLeft'])

	print('Here is the sl/tr: ')
	print(selectionsDictionary['solutionListTopRight'])



