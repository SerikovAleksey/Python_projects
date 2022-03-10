import numpy as np
from matplotlib import pyplot

t = np.arange(0, 140, 10)
t_97 = np.arange(0, 340, 20)
t_146 = np.arange(0, 510, 30)
t_194 = np.arange(0, 640, 40)
t_247 = np.arange(0, 850, 50)

u_37 = [13.5453, 12.9261, 12.2997, 11.7043, 11.1243, 10.5643, 10.0627, 9.5386, 9.0554, 8.6246, 8.2041, 7.7855, 7.3729, 7.0586]
u_97 = [16.8502, 16.1237, 15.3669, 14.679, 14.0142, 13.3866, 12.8, 12.2219, 11.6713, 11.1939, 10.7046, 10.2306, 9.7932, 9.36, 8.9637, 8.5579, 8.2964]
u_146 = [17.0418, 16.3407, 15.601, 14.8735, 14.2576, 13.6603, 13.0883, 12.5402, 12.0326, 11.5371, 11.063, 10.6065, 10.182, 9.7585, 9.3741, 8.9957, 8.6225]
u_194 = [14.9822, 14.3035, 13.4028, 12.8182, 12.1099, 11.505, 11.1322, 10.5616, 10.3054, 9.6345, 9.1418, 8.9247, 8.4889, 8.0669, 7.7563, 7.4833]
u_247 = [15.7701, 14.6732, 14.0186, 13.2439, 12.6871, 12.1931, 11.6506, 11.1995, 10.7944, 10.336, 9.9822, 9.6474, 9.3088, 8.9788, 8.6611, 8.402, 8.1508]



coeffs = np.polyfit(t, np.log(u_37) - np.log(u_37[0]), 1)
k = coeffs[0]
b = coeffs[1]
line_points = [k * number + b for number in t]
pyplot.plot(t, line_points, color='b')

coeffs_97 = np.polyfit(t_97, np.log(u_97) - np.log(u_97[0]), 1)
k_97 = coeffs_97[0]
b_97 = coeffs_97[1]
line_points_97 = [k_97 * number + b_97 for number in t_97]
pyplot.plot(t_97, line_points_97, color='r')

coeffs_146 = np.polyfit(t_146, np.log(u_146)- np.log(u_146[0]), 1)
k_146 = coeffs_146[0]
b_146 = coeffs_146[1]
line_points_146 = [k_146 * number + b_146 for number in t_146]
pyplot.plot(t_146, line_points_146, color='y')

coeffs_194 = np.polyfit(t_194, np.log(u_194) - np.log(u_194[0]), 1)
k_194 = coeffs_194[0]
b_194 = coeffs_194[1]
line_points_194 = [k_194 * number + b_194 for number in t_194]
pyplot.plot(t_194, line_points_194, color='g')

coeffs_247 = np.polyfit(t_247, np.log(u_247) - np.log(15.3301), 1)
k_247 = coeffs_247[0]
b_247 = coeffs_247[1]
line_points_247 = [k_247 * number + b_247 for number in t_247]
pyplot.plot(t_247, line_points_247, color='c')

pyplot.grid()
pyplot.xlabel("$t, с$")
pyplot.ylabel("$ln\\frac{U}{U_0}$")
pyplot.legend(["40 торр", "92 торр", "144 торр", "196 торр", "250 торр"])
pyplot.title("$График$ $зависимости$ $ln\\frac{U}{U_0}$ $oт$ $t$")

# pyplot.show()
pyplot.savefig("Laba_2_2_1")
print(k, k_247, k_194, k_146, k_97)

# d = [10.392, 4.598, 2.895, 2.361, 1.645, 0.705]
# p = [1/40, 1/97, 1/146, 1/194, 1/247, 1/742]
#
# d_1 = [0.705]
# p_1 = [1/742]
#
# pyplot.scatter(p_1, d_1, color='g')
# pyplot.scatter(p, d, color='r')
# pyplot.scatter(p_1, d_1, color='g')
#
# coeffs = np.polyfit(p, d, 1)
# k = coeffs[0]
# b = coeffs[1]
# line_points = [k * number + b for number in p]
# pyplot.plot(p, line_points, color='b')
#
# pyplot.grid()
# pyplot.xlabel('$\\frac{1}{P}, торр^{-1}$')
# pyplot.ylabel("$D, \\frac{см^{2}}{c}$")
# pyplot.legend(["$D_{aтм} = 0, 705 \\frac{см^{2}}{c}$"])
# pyplot.title("График зависимости $D$ от $\\frac{1}{P}$")
#
# # pyplot.show()
# # print(k)
# pyplot.savefig("Laba_2_2_1_plot_2")