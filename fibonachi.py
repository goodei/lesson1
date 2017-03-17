from answers import get_answer
def ask_user():
	while True:
		ask = str(input('How are you? '))
		get_answer(ask)
		if ask == 'Good':
			print('Goodbye')
			break
ask_user()