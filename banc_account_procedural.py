from pwinput import pwinput

account_name = 'Хабиб'
account_balance = 950000
account_depo = 0
account_password = '12345'

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

while True:
	action = input('Which of these operations would you like to perform?: ').lower()[0]

	if action == 'b':
		pswd = pwinput('\nEnter your password: ', mask='*')
		if pswd == account_password:
			print('Your bank account balance is', account_balance)
		else:
			print('Incorrect password')

	elif action == 'd':
		depo_amount = int(input('\nEnter your deposit amount: '))
		pswd = pwinput('\nEnter your password: ', mask='*')
		if pswd == account_password:
			if 0 < depo_amount < account_balance:
				account_balance -= depo_amount
				account_depo += depo_amount
				SUCCESS_TEXT = 'Successful deposit\nYour account balance is: %s\nDeposit amount: %s' % (
					account_balance, depo_amount)
				print(SUCCESS_TEXT)
			else:
				print('Incorrect deposit amount')

		else:
			print('Incorrect password')

	elif action == 'w':
		withdrawal_amount = int(input('\nEnter your withdrawal amount: '))
		pswd = pwinput('\nEnter your password: ', mask='*')
		if pswd == account_password:
			if 0 < withdrawal_amount < account_balance:
				account_balance -= withdrawal_amount
				SUCCESS_TEXT = 'Successful withdrawal\nYour account balance is: %s\nWithdrawal amount: %s' % (
					account_balance, withdrawal_amount)
				print(SUCCESS_TEXT)
			else:
				print('Incorrect withdrawal amount')
		else:
			print('Incorrect password')

	elif action == 's':
		INFO_TEXT = f"""
Account name: {account_name}
Account balance: {account_balance}
Account deposit amount: {account_depo}
Account password: {'*' * len(account_password)}
		"""
		print(INFO_TEXT)
	elif action == 'h':
		print(INSTRUCTIONS_TEXT)
	elif action == 'q':
		break
	else:
		print('Incorrect action.')

print('Done!')
