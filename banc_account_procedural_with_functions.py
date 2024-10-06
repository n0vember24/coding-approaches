from pwinput import pwinput

account_name = ''
account_balance = 0
account_password = ''

ACCOUNT_INFO = f"""
Account Name: {account_name}
Balance: {account_balance}
Password: {'*' * len(account_password)}
"""

INSTRUCTIONS_TEXT = """
Please press one of these following buttons to perform the corresponding operation:
B - Get balance
D - Make deposit
W - Withdrawal
S - Show account details
H - Show this text
Q - Quit
"""

print(INSTRUCTIONS_TEXT)


def new_account(name, balance, password):
	global account_name, account_balance, account_password
	account_name = name
	account_balance = balance
	account_password = password


def show_account():
	global account_name, account_balance, account_password, ACCOUNT_INFO
	print(ACCOUNT_INFO)


def get_balance(password):
	global account_name, account_balance, account_password
	if account_password != password:
		print('Incorrect password')
		return None
	return account_balance


def deposit(depo_amount, password):
	global account_name, account_balance, account_password
	if account_password == password:
		if 0 < depo_amount:
			account_balance += depo_amount
			return account_balance
		else:
			print('Incorrect deposit amount')
			return None
	else:
		print('Incorrect password')
		return None


def withdraw(withdraw_amount, password):
	global account_name, account_balance, account_password
	if account_password == password:
		if 0 < withdraw_amount:
			account_balance -= withdraw_amount
			return account_balance
		else:
			print('Incorrect withdraw amount')
			return None
	else:
		print('Incorrect password')


while True:
	action = input('Which of these operations would you like to perform?: ').lower()[0]

	if action == 'b':
		pswd = pwinput('Enter your password: ', mask='*')
		balance = get_balance(pswd)
		if balance:
			print('Your balance is', balance)
		else:
			print('Incorrect password or you have no account')
	elif action == 'd':
		depo_amount = int(input('Enter your deposit amount: '))
		pswd = pwinput('Enter your password: ', mask='*')
		new_balance = deposit(depo_amount, pswd)
		if new_balance:
			print('Successful deposit!\nYour new balance is', new_balance)
		else:
			...
	elif action == 'w':
		pswd = pwinput('Enter your password: ', mask='*')
		withdraw_amount = int(input('Enter your withdraw amount: '))
		if pswd == account_password:
			if withdraw_amount > 0:
				new_balance = withdraw(withdraw_amount, pswd)
				print('Your new balance is', new_balance)
			else:
				print('Incorrect withdraw amount')
		else:
			print('Incorrect password')
	elif action == 'q':
		break

print('Done!')
