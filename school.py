#Условие
#В школе решили набрать три новых математических класса.
#Так как занятия по математике у них проходят в одно и то же время, было решено выделить кабинет для каждого класса и купить в них новые парты.
#За каждой партой может сидеть не больше двух учеников. Известно количество учащихся в каждом из трёх классов.
#Сколько всего нужно закупить парт чтобы их хватило на всех учеников?
#Программа получает на вход три натуральных числа: количество учащихся в каждом из трех классов.
print("number of people in the first class")
classroom1 = int(input())
print("number of people in the second class")
classroom2 = int(input())
print("number of people in the third class")
classroom3 = int(input())

print ((classroom1 // 2 + classroom1 % 2) + (classroom2 // 2 + classroom2 % 2) + (classroom3 // 2 + classroom3 % 2))