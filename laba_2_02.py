from nucleus import Nucleus
from openpyxl import Workbook
import math
e = 2.71828182846
k = 1.38 * 10**-23
data = Nucleus.openab(1, 4)
data.append([])
table =[]
for i in range(0, 17):
    table.append([data[0][i], data[1][i], data[2][i], data[0][i] + 273, 1/(data[0][i] + 273), 1 / math.log(e, data[2][i])])
    data[3].append(1 / math.log(e, data[2][i]))
wb = Workbook()
ws = wb.active
for g in table:
    ws.append(g)
wb.save('data/laba_2.02/output/table_1.xlsx')
R_0 = Nucleus.method_min_sqrt()['b']
pogr_R_0 = Nucleus.method_min_sqrt()['pogr_b']
otn_pogr_R_0 = pogr_R_0/R_0
print('Сопротивление проводника при t=0:' + str(R_0))
print('Погрешность сопротивления проводника при t=0:' + str(pogr_R_0))
print('Относительная погрешность сопротивления проводника при t=0:' + str(otn_pogr_R_0))
pair_point_1 = [data[0], data[1]]
pair_point_1 = Nucleus.paired_point_method(pair_point_1, 'metal')
a = 1/R_0 * pair_point_1['sr']
print('Температурный коэффициент сопротивления: ' + str(a))
otn_pogr_p_1 = pair_point_1['pogr']/pair_point_1['sr']
print('Относительная погрешность углового коэффициента в графике Rm = Rm(T):' + str(otn_pogr_p_1))
pogr_a = a * (otn_pogr_R_0**2 + otn_pogr_p_1**2)*0.5
print('Погрешность температурного коэффициента сопротивления: ' + str(pogr_a))
pair_point_2 = [[], []]
for i in range(0, len(data[0])):
    if data[2][i] != 100:
        pair_point_2[0].append(1/(data[0][i] + 273))
        pair_point_2[1].append(1 / math.log(e, data[2][i]))
pair_point_2 = Nucleus.paired_point_method(pair_point_2, 'polymetal')
y = pair_point_2['sr']
pogr_y = pair_point_2['pogr']
E_g = 2 * y * k
print('Ширина запрещенной зоны:' + str(E_g))
pogr_E_g = pair_point_2['pogr']/pair_point_2['sr'] * E_g
print('Погрешность ширины запрещенной зоны:' + str(pogr_E_g))
