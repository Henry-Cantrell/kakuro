#Psuedocode

#Check solutions in build_choice_list
#So, topLeft are 0, 2 in gmDict for 0, 1 and topRight are 1, 3 in gmDict for 2, 3 for indexes in winning_conds_dict dictionary choices list
#Check against determine_if_choices_win func
#If failed, discard first index of topLeft and topRight into respective lists and continue with next choice

def selectChoices(gmDict):
	selectionsDictionary={
	'discardListTopRight' : [],
	'discardListTopLeft' : [],
	'solutionListTopRight' : [],
	'solutionListTopLeft' : [],
	'numbersOne' : [],
	'numbersTwo' : []
	}

	def createAndSortChoices(selectionsDictionary, gmDict):
		selectionsDictionary['numbersOne'] = list(range(1, 10))
		selectionsDictionary['numbersTwo'] = list(range(1, 10))

		for i in selectionsDictionary['numbersOne']:
			for n in selectionsDictionary['numbersTwo']:
				if i + n == gmDict['positional_list'][0]:
					selectionsDictionary['solutionListTopLeft'].append([i, n])
				elif i + n == gmDict['positional_list'][1]:
					selectionsDictionary['solutionListTopRight'].append([i, n])
	
	createAndSortChoices(selectionsDictionary, gmDict)

	#gmDict['choices_list'].append(selectionsDictionary['solutionListTopRight'][0])
	#gmDict['choices_list'].append(selectionsDictionary)['solutionListTopRight'][2])
	#gmDict['choices_list'].append(selectionsDictionary['solutionListTopLeft'][1])
	#gmDict['choices_list'].append(selectionsDictionary)['solutionListTopLeft'][3])

