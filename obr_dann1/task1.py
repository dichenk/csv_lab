import csv
import math
import time

'''Задание 1'''
'''1 способ'''
results1 = []
with open ('add.csv') as file:
    reader = csv.reader(file)
    for row in reader:
        results1.append(row)

'''2 способ'''
results2 = []
with open('add.csv') as file:
    reader = csv.DictReader(file)
    for row in reader:
        results2.append(row)

print('   задание 1')
print('\n1 способ')
for i in results1:
    print(i)

print('\n2 способ')
for i in results2:
    print(i)

'''задание 2'''
name = input('введите имя ')
for index, item in enumerate(results1):
    if item[0] == name:
        print(item)
        print('номер строки:', index + 1)

'''задание 3'''

result3 = []
result4 = []
print('\nЗадание 3')
for i in range(-200, 60): ## такое же количество шагов
    j = i / 10
    try:
        f1 = j + math.log(j) + math.sin(0.5)
    except:
        f1 = None
    try:
        f2 = (math.cos(3 * j) + 1 / math.sin(math.pi)) / j
    except:
        f2 = None
    result3.append([[f1], [f2]])
    result4.append({'x': j, 'f1': f1, 'f2': f2})


'''csv.writer'''
with open('csvwriter.csv', 'w') as file:
    csvwriter = csv.writer(file)
    csvwriter.writerows(result3)

'''csv.Dictwriter'''
with open('csvDictwriter.csv', 'w') as file:
    writer = csv.DictWriter(file, fieldnames = ['x', 'f1', 'f2'])
    writer.writeheader()
    writer.writerows(result4)

'''задание 4'''
'''a'''
results5 = []
with open ('snakes.csv') as file:
    schet = 0
    reader = csv.reader(file)
    for row in reader:
        results5.append(row)
        i = i + 1
        if i == 1000: break

'''b'''
results6 = []
with open('snakes.csv') as file:
    reader = csv.DictReader(file)
    for row in reader:
        results6.append(row)

'''печатаем а'''
for i in range(20):
    print('первые 20 строк а: ', results5[i])

'''печатаем б'''
for i in range(20):
    print('первые 20 строк б: ', results6[i])

print()
results7 = []
with open ('prices.csv') as file:
    reader = csv.reader(file)
    for row in reader:
        results7.append(row)

results7_sum = 0
for i in results7:
    results7_sum += int(i[2]) * int(i[1])
print('общая стоимость заказа: ', results7_sum)

