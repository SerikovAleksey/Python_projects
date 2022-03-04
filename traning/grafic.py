import matplotlib
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from scipy.optimize import minimize

plt.errorbar(spectrum['T'], spectrum['A'], xerr=10, yerr=0, fmt='.', linewidth=1)
x = np.linspace(1850, 2650, num=100)
plt.plot(x, np.polyval(poly, x), linewidth=1)

plt.grid(linestyle='--')
plt.xlabel('$\\theta, ^\circ$')
plt.ylabel('$\lambda, \mathring{A}$')

plt.savefig('data/spectrum.pgf')
plt.show()

# Эти 2 строки сохраняют пустой график с названием 1.pgf.
# Хз зачем это, если у вас будет работать без этого, можно смело удалять.
plt.savefig('data/1.pgf')
plt.show()


# matplotlib.use("pgf")
# matplotlib.rcParams.update({
#     "pgf.texsystem": "pdflatex",
#     'font.family': 'serif',
#     'text.usetex': True,
#     'pgf.rcfonts': False,
# })

# Размер графика
fig = plt.figure(figsize=(7, 4))

#задаем отрезок, на котором рисуем кривую
x = np.linspace(0, 50, num=100)
#рисуем кривую
plt.plot(x, sigmoid(par, x), 'k', linewidth=1, label='N approximation')

# Надо еще погрешности посчитать
delta_N = geig['N'] / geig['t']**2

#рисуем точки
plt.errorbar(geig['l'], geig['N1'], fmt='k.', yerr=delta_N, xerr=0, linewidth=1, label='measurments')

#вариант без погрешностей
#plt.plot(geig['l'], geig['N1'], 'k.', linewidth=1, label='measurments')

#Оформление
plt.grid(linestyle='--')
plt.xlabel('$l, mm$', fontsize=15)
plt.ylabel('$N$', fontsize=15)
# fig.legend()

#Сохраняем результат
plt.savefig('data/geig.pgf')
plt.show()