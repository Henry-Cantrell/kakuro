def winnerEval(winningConditionsDict):

	top_left_satisfied = (winningConditionsDict['top_left_choice'] + winningConditionsDict['bottom_left_choice'] == top_left_position)

	top_right_satisfied = (winningConditionsDict['top_right_choice'] + winningConditionsDict['bottom_right_choice'] == top_right_position)

	left_top_satisfied = (winningConditionsDict['top_left_choice'] + winningConditionsDict['top_right_choice'] == left_top_position)

	left_bottom_satisfied = (winningConditionsDict['bottom_left_choice'] + winningConditionsDict['bottom_right_choice'] == left_bottom_position)

	all_states_satisfied = top_left_satisfied and top_right_satisfied and left_top_satisfied and left_bottom_satisfied
	
	if all_states_satisfied:
		return True
	else:
		return False

