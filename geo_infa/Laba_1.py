import matplotlib.pyplot as plt
import numpy as np
from pyorbital.orbital import Orbital
from sgp4.api import Satrec, jday
from skyfield.api import load, wgs84
from skyfield.api import EarthSatellite

# Прибавление времени
def minute_plus(time):
    if time[3] < 59:
       time[3] += 1
    elif time[2] < 24:
        time[3] = 0
        time[2] += 1
    else:
        time[1] += 1
        time[2] = 0
        time[3] +=1
# Выбранное время
time = '03.04 18:29'
time_s = [int(time[0:2]), int(time[3:5]), int(time[6:8]), int(time[9:11])]
time = '03.05 18:29'
time_f = [int(time[0:2]), int(time[3:5]), int(time[6:8]), int(time[9:11])]

# TLE
line_1 = '1 33591U 09005A   22073.14995545  .00000144  00000-0  10288-3 0  9992'
line_2 = '2 33591  99.1606 105.2310 0014882  95.8822 264.4045 14.12537324674995'
satellite_1 = Satrec.twoline2rv(line_1, line_2)
satellite = Orbital('NOAA 19')
satellite_2 = EarthSatellite(line_1, line_2)
me = wgs84.latlon(+55.75, -37.62)


# Массивы
ecis = []
eliv = [0]
azim = []
eliv_1 = []

# Координаты спутника в заданном времени
while time_s != time_f:
    jd, fr = jday(2021, 3, time_s[1], time_s[2], time_s[3], 18)
    e, r, v = satellite_1.sgp4(jd, fr)
    ecis.append(r)
    minute_plus(time_s)
print(np.array(ecis))


dif = satellite_2 - me
time = '03.04 18:29'
time_s = [int(time[0:2]), int(time[3:5]), int(time[6:8]), int(time[9:11])]


# Определение эливации и азимута во время виденья спутника
# while time_s != time_f:
#     ts = load.timescale()
#     t = ts.utc(2022, 3, time_s[1], time_s[2], time_s[3], 18)
#     topocentric = dif.at(t)
#     alt, az, dis = topocentric.altaz()
#     if alt.degrees > 0:
#     # if int(str(alt)[0:2]) > 0:
#         time_start_look.append(time_s)
#         eliv.append(int(str(alt)[0:2]))
#         if str(az)[3] == 'd':
#             azim.append(int(str(az)[0:3]))
#         else:
#             azim.append(int(str(az)[0:2]))
#     minute_plus(time_s)
# eliv.remove(0)
# print(len(eliv))
# print(len(azim))

# График орбиты
# a, b = 6378.137, 6356.7523142
#
# ecis = np.array(ecis)
# x, y, z = ecis[:, 0], ecis[:, 1], ecis[:, 2]
#
# fig = plt.figure(figsize=(8, 8))
# ax = fig.add_subplot(111, projection='3d')
#
# ax.plot(x, y, z)
#
# rx, ry, rz = a, a, b
# u = np.linspace(0, 2 * np.pi, 100)
# v = np.linspace(0, np.pi, 100)
# x = rx * np.outer(np.cos(u), np.sin(v))
# y = ry * np.outer(np.sin(u), np.sin(v))
# z = rz * np.outer(np.ones_like(u), np.cos(v))
# #
# ax.plot_wireframe(x, y, z, alpha=0.1)
#
#
# max_radius = max(rx, ry, rz)
# for axis in 'xyz':
#     getattr(ax, 'set_{}lim'.format(axis))((-max_radius, max_radius))
# plt.show()
#
#
# # График во время виденья спутника
# # Очень странный получился
# fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
# ax.plot(np.array(eliv), (np.array(azim) * (-1) + 90))
# ax.set_rmax(90)
# ax.set_rmin(0)
# ax.set_rticks([90,60,30,0], [" "]*4)
# ax.grid(True)
# plt.show()