import random

def buildChoices(gmDict):
	for i in range(4):
		if len(gmDict['choices_list']) == 4:
			gmDict['choices_list'].pop(i)
			gmDict['choices_list'].append(random.randint(1, 9))
			print(gmDict['choices_list'])
			print('Rewriting a filled illegal list...')
		elif len(gmDict['choices_list']) != 4:
			gmDict['choices_list'].append(random.randint(1, 9))
			print('Filling an empty list...')


