#These conds need to be redone to simply calc quantity

def winnerEval(winningConditionsDict):

	top_left_satisfied = winningConditionsDict['top_left_choice'] + winningConditionsDict['bottom_left_choice'] == winningConditionsDict['top_left_position']

	top_right_satisfied = winningConditionsDict['top_right_choice'] + winningConditionsDict['bottom_right_choice'] == winningConditionsDict['top_right_position']

	left_top_satisfied = winningConditionsDict['top_left_choice'] + winningConditionsDict['top_right_choice'] == winningConditionsDict['left_top_position']

	left_bottom_satisfied = winningConditionsDict['bottom_left_choice'] + winningConditionsDict['bottom_right_choice'] == winningConditionsDict['left_bottom_position']

	no_illegal_top_left_vertical = (winningConditionsDict['top_left_choice']/2) != winningConditionsDict['top_left_position'] 

	no_illegal_top_left_horizontal = (winningConditionsDict['top_left_choice']/2) != winningConditionsDict['left_top_position'] 

	no_illegal_top_right_vertical = (winningConditionsDict['top_right_choice']/2) != winningConditionsDict['top_right_position']

	no_illegal_bottom_left_horizontal = (winningConditionsDict['top_right_choice']/2) != winningConditionsDict['top_right_position']

	no_illegal_choices = no_illegal_bottom_left_horizontal and no_illegal_top_left_horizontal and no_illegal_top_left_vertical and no_illegal_top_right_vertical

	all_states_satisfied = top_left_satisfied and top_right_satisfied and left_top_satisfied and left_bottom_satisfied and no_illegal_choices
	
	if all_states_satisfied:
		return True
	else:
		return False

#To-do list:
