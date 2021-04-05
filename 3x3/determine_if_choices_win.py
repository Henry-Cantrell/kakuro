#0 is a top column position, while 1 is a bottomn column position, out of a column of height 2

def winnerEval(leftColumnPos, rightColumnPos, gmDict):

	top_left_satisfied = leftColumnPos[0] + leftColumnPos[1] == gmDict['positional_list'][0]

	top_right_satisfied = rightColumnPos[0] + rightColumnPos[1] == gmDict['positional_list'][1]

	left_top_satisfied = leftColumnPos[0] + rightColumnPos[0] == gmDict['positional_list'][2]

	left_bottom_satisfied = leftColumnPos[1] + rightColumnPos[1] == gmDict['positional_list'][3]

	no_illegal_top_left_vertical = leftColumnPos[0] != leftColumnPos[1]

	no_illegal_top_left_horizontal = rightColumnPos[0] != rightColumnPos[1]

	no_illegal_top_right_vertical = leftColumnPos[0] != rightColumnPos[0]

	no_illegal_bottom_left_horizontal = leftColumnPos[1] != rightColumnPos[1]

	no_illegal_choices = no_illegal_bottom_left_horizontal and no_illegal_top_left_horizontal and no_illegal_top_left_vertical and no_illegal_top_right_vertical

	all_states_satisfied = top_left_satisfied and top_right_satisfied and left_top_satisfied and left_bottom_satisfied and no_illegal_choices
	
	if all_states_satisfied:
		return True
	else:
		return False

