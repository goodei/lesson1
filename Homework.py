
import random
def score(a):
    return [random.randint(2,5) for x in range(a)]
pupls = 5 # Задаем кол-во учеников в классе
school = [{'sh_cl':'1a','sco':score(pupls)}, {'sh_cl':'1b','sco':score(pupls)}, {'sh_cl':'2a','sco':score(pupls)},{'sh_cl':'2b','sco':score(pupls)}]
all_scores = []
message = 'В каждом классе %s  учеников' % pupls
print(message)
for i in school:
    scores = i['sco'] #Список оценок класса
    classes = i['sh_cl'] #Номер класса
    print('Номер класса : ' + classes + ' ' + 'Оценки класса : ' + str(scores) + ' ' + 'Средняя оценка по классу: ' + str(sum(scores)/len(scores)))
    all_scores += scores
print( 'Средняя оценка по школе : '  +  str(sum(all_scores)/len(all_scores)))
    


