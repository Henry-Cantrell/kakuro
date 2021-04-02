#Psuedocode
#Scenario is TL position = 15:
#Generate two lists of ints 1-15
#Loop over one list and add each num against num from other list one at a time
#Determine nums that equal 15
#Check discard list for pair
#If not in discard list, add to solution list
#Repeat process for TR
#Check solution list for some list pair that satisfies determine_if_choices_win conditions
#If any pair fails the above check, move to discard list
#Once viable solution set identified, empty discard sets

def selectChoices(gmDict):
	discardListTopRight = []
	discardListTopLeft = []
	solutionListTopRight = []
	solutionListTopLeft = []

	#def createAndSortChoices:
