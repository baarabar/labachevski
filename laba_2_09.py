from nucleus import Nucleus
from openpyxl import Workbook
import math

e = 2.71828182846
m_e = 9.1093837 * 10 ** -31
el = 1.60217663 * 10 ** -19
k = 1.38 * 10 ** -23
s = 6 * 10 ** -6
p = 66.661
data = Nucleus.openab(1, 7)  # Открываем файл
data_mnk = Nucleus.method_min_sqrt(4, 5)  # Делаем метод наименьших квадратов для того, чтобы узнать коэффициенты
data_mnk = [data_mnk['a'], data_mnk['b']]  # a и b для продолжения линии ионного тока
a = data_mnk[0]
b = data_mnk[1]
data_ii = []
for i in range(0, len(data[1])):  # Продолжаем линию ионного тока благодаря найденным коэффициентам
    x = data[1][i]
    y = a * x + b
    data_ii.append(y)
main_table = []
data_ii = data_ii + data[5]  # Соединяем полученные значения со старой информацией и компилируем все в один массив
data_u = data[1] + data[4]
data_i3 = data[2] + data[5]
for i in range(0, len(data_ii)):
    main_table.append([i + 1, data_u[i], data_i3[i], data_ii[i], data_i3[i] - data_ii[i], '-'])
for i in range(0, len(main_table)):  # Добавляем значение логарифма в массив
    if main_table[i][4] != 0:
        main_table[i][5] = math.log(main_table[i][4], e)
wb = Workbook()  # Создаем главную таблицу
ws = wb.active
for g in main_table:
    ws.append(g)
wb.save('data/laba_2.09/output/main_table.xlsx')
data_pair_point = []
for i in range(0, len(main_table)):  # Создаем массив для метода парных точек
    if (main_table[i][4] < 500) and (main_table[i][4] > 0):
        data_pair_point.append([main_table[i][1], main_table[i][5]])
data_pair_point = Nucleus.connect(data_pair_point)
data_pair_point = Nucleus.paired_point_method(data_pair_point, 'pair_point')  # Метод парных точек
data_pair_point = [data_pair_point['sr'], data_pair_point['pogr']]
T_e = el / (data_pair_point[0] * k)  # Далее идет вычисление всяких значений
pogr_T_e = T_e * data_pair_point[1] / data_pair_point[0]
print('Температура электронов: ' + str(T_e))
T = Nucleus.openab(7, 8)[0][0]
n = p / (k * T)
print('Концентрация атомов газа: ' + str(n))
i_e = int(input('Введите значение тока невозмущенной плазмы: '))  # 1480 Надо самостоятельно провести линию и ввести значение тока
V_e = (8 * k * T_e / (3.14159 * m_e)) ** 0.5
print('Скорость электронов: ' + str(V_e))
n_e = 4 * i_e * 10 ** -6 / (el * V_e * s)
print('Концентрация электронов: ' + str(n_e))
b = n_e / n
print('Степень ионизации газа: ' + str(b))
