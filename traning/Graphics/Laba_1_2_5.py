from matplotlib import pyplot
import numpy
# x = [float(number) for number in input().split()]
# y = [float(number) for number in input().split()]
# y_1 = [float(number) for number in input().split()]
# y_2 = [float(number) for number in input().split()]
x = [1, 2, 3, 4, 5, 6]
y = [3.3, 6.6, 9.7, 13, 16.2, 19.4]
y_1 = [4.1, 8.3, 12.4, 16.5, 20.6, 24.9]
y_2 = [4.3, 8.6, 12.8, 17, 21.2, 25.5]

coeffs = numpy.polyfit(x, y, 1)
coeffs_1 = numpy.polyfit(x, y_1, 1)
coeffs_2 = numpy.polyfit(x, y_2, 1)
k = coeffs[0]
b = coeffs[1]
k_1 = coeffs_1[0]
b_1 = coeffs_1[1]
k_2 = coeffs_2[0]
b_2 = coeffs_2[1]
line_points = [k * number + b for number in x]
line_points_1 = [k_1 * number + b_1 for number in x]
line_points_2 = [k_2 * number + b_2 for number in x]
pyplot.scatter(x, y, color='r')
pyplot.scatter(x, y_1, color='b')
pyplot.scatter(x, y_2, color='k')
# pyplot.plot(x, y, color='r')
pyplot.plot(x, line_points, color='b')
pyplot.plot(x, line_points_1, color='g')
pyplot.plot(x, line_points_2, color='m')
pyplot.xlabel('n')
pyplot.ylabel('f, кГц')
pyplot.xlim(0, 7)
pyplot.ylim(0, 27)
pyplot.grid()
pyplot.title('График зависимости f(n)')
# pyplot.show()
pyplot.savefig('laba_1_4_8')