from nucleus import Nucleus
from openpyxl import Workbook

u = 4 * 3.14159 * 10**-7
N = Nucleus.openab(10, 11)[0][0]
R_a = Nucleus.openab(11, 12)[0][0]
l = Nucleus.openab(12, 13)[0][0]
m_e =[]

for i in range(0, 3):
    data = Nucleus.openab(1 + 3*i, 4 + 3*i)
    data_table = Nucleus.connect([data[1], data[2]])
    wb = Workbook()
    ws = wb.active
    for g in data_table:
        ws.append(g)
    wb.save('data/laba_2.08/output/table_' + str(i+1) + '.xlsx')
    i_k = int(input('Введите значение критического тока: '))
    B_k = u * i_k * N / l
    print('Магнитная индукция внутри соленоида: ' + str(B_k))
    m_e_i = 8 * data[0][0] / (B_k**2 * R_a**2)
    print('Удельный заряд электрона: ' + str(m_e_i))
    m_e.append(m_e_i)
data_m_e = Nucleus.dm(m_e, 'data_table')
