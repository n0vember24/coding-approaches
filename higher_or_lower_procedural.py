import random

SUIT_TUPLE = ('Пики', 'Черви', 'Трефы', 'Бубны')
RANK_TUPLE = ('Туз', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Валет', 'Дама', 'Король')
NCARDS = 8


def get_card(list_in):
	current_card = list_in.pop()
	return current_card


def shuffle_card(list_in):
	list_out = list_in.copy()
	random.shuffle(list_out)
	return list_out


WELCOME_TEXT = """
Добро пожаловать в игру "Больше или Меньше" написанный с использованием процедурного подхода Python
Вам нужно выбрать, будет ли следующая показанная карта выше или ниже текущей карты.
Если вы угадали, то получаете 20 очков. А если нет, то потеряете 15.
Игра продолжится до тех пор пока вы не потеряете все очки
У вас есть 50 очков для начала
"""

print(WELCOME_TEXT)

starting_list = []
for suit in SUIT_TUPLE:
	for value, rank in enumerate(RANK_TUPLE):
		card_dict = {'rank': rank, 'suit': suit, 'value': value + 1}
		starting_list.append(card_dict)
score = 50

while True:
	game_list = shuffle_card(starting_list)
	current_card_dict = get_card(game_list)
	current_card_rank = current_card_dict['rank']
	current_card_value = current_card_dict['value']
	current_card_suit = current_card_dict['suit']

	for card_number in range(0, NCARDS):
		print('Начинающая карта: %s, %s\n' % (current_card_rank, current_card_suit))
		next_card_dict = get_card(game_list)
		next_card_rank = next_card_dict['rank']
		next_card_suit = next_card_dict['suit']
		next_card_value = next_card_dict['value']

		while True:
			INPUT_TEXT = 'Следующая карта будет больше или меньше текущей?\nТекущая карта: %s, %s\nВаш ответ (б/м): ' % (
				current_card_rank, current_card_suit)
			answer = input(INPUT_TEXT)
			answer = answer.lower()

			if answer == 'б':
				if next_card_value > current_card_value:
					print('\nВаш ответ правильный! +20 очков')
					score += 20
					break
				else:
					print('\nВаш ответ неправильный! -15 очков')
					score -= 15
					break
			elif answer == 'м':
				if next_card_value < current_card_value:
					print('\nВаш ответ правильный! +20 очков')
					score += 20
					break
				else:
					print('\nВаш ответ неправильный! -15 очков')
					score -= 15
					break
			else:
				print('\nВы можете ответить только "б" или "м"\n')


		print('Следующая карта: %s, %s' % (next_card_rank, next_card_suit))
		print('Ваши очки: %s\n' % score)

		current_card_rank = next_card_rank
		current_card_value = next_card_value

	LOSE_TEXT = 'Если хотите играть ещё раз, нажмите ENTER, если нет введите "q": '
	go_again = input(LOSE_TEXT)
	if go_again.lower() == 'q':
		break

print('Хорошо, пока!')
