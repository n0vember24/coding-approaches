import random

SUIT_TUPLE = ('Spades', 'Hearts', 'Clubs', 'Diamonds')
RANK_TUPLE = ('Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King')
NCARDS = 8


def get_card(list_in):
	current_card = list_in.pop()
	return current_card


def shuffle_card(list_in):
	list_out = list_in.copy()
	random.shuffle(list_out)
	return list_out


print('Welcome to higher or lower procedural!')
print('U have to choose whether the next card to be shown will be higher or lower than the current card ')
print('Getting it right adds 20 points, get it wrong and u lose 15 points')
print('U have 50 points to start')

starting_list = []
for suit in SUIT_TUPLE:
	for value, rank in enumerate(RANK_TUPLE):
		card_dict = {'rank': rank, 'suit': suit, 'value': value + 1}
		starting_list.append(card_dict)
score = 50

while True:
	print()
	game_list = shuffle_card(starting_list)
	current_card_dict = get_card(game_list)
	current_card_rank = current_card_dict['rank']
	current_card_value = current_card_dict['value']
	current_card_suit = current_card_dict['suit']
	print('Starting card is %s1 of %s2\n' % (current_card_rank, current_card_suit))

	for card_number in range(0, NCARDS):
		answer = input(
			'Will the next car be higher or lower than %s1 of %s2 (h/l): ' % (current_card_rank, current_card_suit))

		answer = answer.lower()
		next_card_dict = get_card(game_list)
		next_card_rank = next_card_dict['rank']
		next_card_suit = next_card_dict['suit']
		next_card_value = next_card_dict['value']
		print('Next card is %s1 of %s2\n' % (next_card_rank, next_card_suit))

		if answer == 'h':
			if next_card_value > current_card_value:
				print('Correct! +20 points')
				score += 20
			else:
				print('Incorrect! -15 points')
				score -= 15
		elif answer == 'l':
			if next_card_value < current_card_value:
				print('Correct! +20 points')
				score += 20
			else:
				print('Incorrect! -15 points')
				score -= 15
		else:
			print('You can answer only "h" or "l"')
		print('Score is %d\n' % score)

		current_card_rank = next_card_rank
		current_card_value = next_card_value
	print('\n_______________________________________\nТы проиграл :(')
	go_again = input('Would you like to go again? If yes, press enter, otherwise press "q": ')

	if go_again.lower() == 'q':
		break

print('Ok, bye')
