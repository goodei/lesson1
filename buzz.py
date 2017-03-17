def f_buzz(arg):
    if arg %5 == 0 and arg %3 == 0:
        return 'FizzBuzz'
    elif arg %5 == 0:
        return 'Buzz'
    elif arg %3 == 0:
        return 'Fizz'
    else:
        return str(arg)
for i in list(range(1,101)):
    print(f_buzz(i))