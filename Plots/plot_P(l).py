import sgp4
import numpy as np
from matplotlib import pyplot

# P = [166.6, 147 + 166.6, 190.12 + 147 + 166.6, 196 + 190.12 + 147 + 166.6]
# l = [11.2, 41.2, 81.2, 131.2]
#
# P_2 = [58.5, 37.24 + 58.5, 49 + 37.24 + 58.5, 50 + 49 + 37.24 + 58.5]
# l_2 = [11.5, 41.5, 81.5, 131.5]

# P = [41.16, 76, 106, 147, 164, 182, 206, 225, 241, 268, 294, 305]
# P_l = [41.16, 76, 106, 147, 164, 182]
# Q = [2, 4, 5, 7, 8, 9, 10, 10.8, 11.2, 11.7, 12.2, 12.3]
# Q_l = [2, 4, 5, 7, 8, 9]

P = [205, 235, 278, 317, 352, 368, 391, 411]
Q = [19, 22, 26, 29, 31.5, 32.5, 33.5, 34]

P_l = [205, 235, 278, 317]
Q_l = [19, 22, 26, 29]


coeffs = np.polyfit(Q_l, P_l, 1)
k = coeffs[0]
b = coeffs[1]
line_points = [k * number + b for number in Q_l]
pyplot.plot(Q_l, line_points, color='b')


# coeffs = np.polyfit(l_2, P_2, 1)
# k_2 = coeffs[0]
# b_2 = coeffs[1]
# line_points_2 = [k_2 * number + b_2 for number in l_2]
# pyplot.plot(l_2, line_points_2, color='g')
#
# pyplot.scatter(l_2, P_2, color='r')
pyplot.scatter(Q, P, color='r')

pyplot.grid()
pyplot.xlabel("$Q \cdot 10^2, \\frac{л}{с}$")
pyplot.ylabel("$P, Па$")
pyplot.legend(["$d_3 = (5,30 \pm 0,05)мм$"])
pyplot.title("$График$ $зависимости$ $P$ $oт$ $Q$")

# pyplot.show()
pyplot.savefig("Laba_1_3_3(2)")