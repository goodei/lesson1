name_list = ["Вася", "Петя", "Маша", "Костя","Даша", "Марина", "Алеша", "Никита"]
name = str(input('Enter name please: '))
def find_name(name,list_share):
		while list_share:
			if name.capitalize() == list_share.pop(0):
				print('%s is founded!' %name.capitalize())
				break
		else:
			print('%s not founded' %name)
find_name(name,name_list)