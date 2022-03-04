# from matplotlib import pyplot
# import numpy
# x = [float(number) for number in input().split()]
# y = [float(number) for number in input().split()]
#
# coeffs = numpy.polyfit(x, y, 1)
# k = coeffs[0]
# b = coeffs[1]
# line_points = [k * number + b for number in x]
# pyplot.scatter(x, y, color='r')
# #pyplot.plot(x, y, color='r')
# pyplot.plot(x, line_points, color='b')
# pyplot.xlabel('x, см')
# pyplot.ylabel('y, с')
# pyplot.xlim(0, 50)
# pyplot.ylim(0, 3.5)
# pyplot.grid()
# pyplot.title('График зависимости иксов от их квадратов\nс линейной аппроксимацией')
# pyplot.show()
# # pyplot.savefig('first')
#
#

import numpy as np
import matplotlib.lines as mlines
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
with open('40 mmHg.txt', 'r') as mm40:
    tmp40 = mm40.read().split("\n")
    sums = 0
    tmp40_int = []
    for i in range(7, len(tmp40) - 1, 1):
        tmp40_int.append(int(tmp40[i]))
    for i in range(7, len(tmp40) - 1, 1):
        sums += int(tmp40[i])
    k40 = sums / (len(tmp40) - 8) / 40
with open('80 mmHg.txt', 'r') as mm80:
    tmp80 = mm80.read().split("\n")
    sums = 0
    for i in range(7, len(tmp80) - 1, 1):
        sums += int(tmp80[i])
    k80 = sums / (len(tmp80) - 8) / 80
with open('120 mmHg.txt', 'r') as mm120:
    tmp120 = mm120.read().split("\n")
    sums = 0
    for i in range(7, len(tmp120) - 1, 1):
        sums += int(tmp120[i])
    k120 = sums / (len(tmp120) - 8) / 120
with open('160 mmHg.txt', 'r') as mm160:
    tmp160 = mm160.read().split("\n")
    sums = 0
    tmp160_int = []
    for i in range(7, len(tmp160) - 1, 1):
        tmp160_int.append(int(tmp160[i]))
    for i in range(7, len(tmp160) - 1, 1):
        sums += int(tmp160[i])
    k160 = sums / (len(tmp160) - 8) / 160
k = (k160 + k80 + k40 + k120) / 4


def mm_to_pa(mm):
    return mm * 13596 / 100


pressure_calib_float = []
adc_calib_int = []
for i in range(min(tmp40_int), max(tmp160_int) + 1):
    adc_calib_int.append(i)
for i in range(min(tmp40_int), max(tmp160_int) + 1):
    pressure_calib_float.append(adc_calib_int[i - min(tmp40_int)] / k)
fig, ax = plt.subplots(figsize=(16, 10), dpi=400)
plt.title('Калибровочный график зависимости показаний АЦП от давления', fontsize=7, color='black')
ax.plot(pressure_calib_float, adc_calib_int, color='b', linewidth=1)
plt.axis([35, 165, min(tmp40_int) - 100, max(tmp160_int) + 100])
plt.xlabel('Давление, мм', fontsize=6)
plt.ylabel('Отсчеты АЦП', fontsize=6)
ax.xaxis.set_major_locator(ticker.MultipleLocator(20))
ax.yaxis.set_major_locator(ticker.MultipleLocator(200))
ax.tick_params(which='major', length=3, labelsize=3)
ax.tick_params(which='minor', length=1)
ax.grid(which='major', color='black', linewidth=0.2)
ax.minorticks_on()
ax.grid(which='minor', color='gray', linestyle=':', linewidth=0.2)
graph = mlines.Line2D([], [], color='blue', markersize=30, label='P = N * k')
plt.legend(handles=[graph])
plt.show()
fig.savefig("Pressure-calibration.png")
