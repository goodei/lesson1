import random
some_list = [random.randint(0,100) for i in range(10)]
message = 'Генерируемый список : %s' % some_list
print(message)
for i in some_list:
	i+=1
	print(i)
lists = [i+1 for i in some_list]
message_1 = 'Новый список,в котором члены списка увеличены на единицу : {}'.format(lists)
print(message_1)
some_list_2 = str(input('enter a letter: '))
for i  in some_list_2:
	print(i)
lists_2 = [i for i in some_list_2]
print(lists_2)