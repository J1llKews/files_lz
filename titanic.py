import pandas as pd 
import matplotlib.pyplot as plt
import csv

#сохраняем данные из паркета в цсв
df = pd.read_parquet('titanic.parquet')
df.to_csv('titanic.csv')
#счетчики пассажиров каждого класса
3rd_class = 0
3rd_class_survived = 0
2nd_class = 0
2nd_class_survived = 0
1st_class = 0
1st_class_survived = 0

#открываем цсв файл
titanic_data = open('titanic.csv', 'r')
data = csv.reader(titanic_data)

#считаем количество пассажиров и выживших по классам
for column in data:
    match column[3]:  №определяем класс пассажира
        case '3':
            3rd_class += 1
            if column[2] == '1':  # если выжил
                3rd_class_survived += 1
        case '2':
            2nd_class += 1
            if column[2] == '1':
                2nd_class_survived += 1
        case '1':
            1st_class += 1
            if column[2] == '1':
                1st_class_survived += 1
#создаём списки для графика
labels = ['Первый класс', 'Второй класс', 'Третий класс']
survived = [1st_class_survived, 2nd_class_survived, 3rd_class_survived]
died = [1st_class - 1st_class_survived, 2nd_class - 2nd_class_survived, 3rd_class - 3rd_class_survived]

#строим диаграмму 
plt.title('Выживаемости пассажиров Титаника')
plt.bar(labels, died, label='Умерли')
plt.bar(labels, survived, bottom=died, label='Выжили')
plt.legend(loc='upper center')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
