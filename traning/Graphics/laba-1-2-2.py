from matplotlib import pyplot
import numpy
x = [float(number) for number in input().split()]
y = [float(number) for number in input().split()]

coeffs = numpy.polyfit(x, y, 1)
k = coeffs[0]
b = coeffs[1]
line_points = [k * number + b for number in x]
pyplot.scatter(x, y, color='r')
#pyplot.plot(x, y, color='r')
pyplot.plot(x, line_points, color='b')
pyplot.xlabel('R^2 * 10^2, м^2')
pyplot.ylabel('I * 10^2, кг*м^2')
pyplot.xlim(0, 3)
pyplot.ylim(0, 3)
pyplot.grid()
# pyplot.legend(['I = 0.013 кг * м^2'])
pyplot.title('График зависимости момента инерции \n от расстояния до грузов в квадрате')
# pyplot.show()
# print(1/k / 100)
pyplot.savefig('laba-1-2-2_2')
# 2.89 0.95 2
# 1.5 0.8 1.3

