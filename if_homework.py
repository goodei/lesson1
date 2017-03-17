"""
def strings(string_1,string_2):
    string_1 = str(string_1)
    string_2 = str(string_2)
    if string_2 == string_1:
        return 1
    elif len(string_1) > len(string_2):
        return 2
    elif  string_2 == 'learn':
        return 3
    else:
        return 0
i = 0
print('Сравниваем введенные строки 4 раза: ')
while i < 4:
    string_1 = input('Please enter first letter: ')
    string_2 = input('Please enter second letter: ')    
    print(strings(string_1,string_2))
    i += 1
    """
try:
    age = int(input('Введите ваш возраст: '))
    if age <= 0:
        print('Возраст не может быть меньше 0')
    elif  age <= 7:
        print( 'Ты должен быть в детском саду')
    elif age <=17:
        print ('Ты должен учиться в школе')
    elif age <= 25:
        print('Ты должен учиться в школе')
    elif 150 > age > 25:
        print('Ты должен работать')
    else:
        print('Неправильный ввод,попробуйте еще')
except ValueError:
    print("Incorrect age,try again")