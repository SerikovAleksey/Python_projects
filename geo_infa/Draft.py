from datetime import datetime, timedelta
from pyorbital.orbital import Orbital
obs_lat, obs_long = 55.75, 37.62


start, end = datetime.now(), datetime.now() + timedelta(days=1)
orb = Orbital("NOAA 19")
step = 60 * 24
ecis = []
for i in range (step):
  ecis.append(orb.get_position(start + i * timedelta(minutes=1), normalize=False)[0])

obs_look = []
begin = []
endd = []
for i in range (step):
  if orb.get_observer_look(start + i * timedelta(minutes=1), obs_long, obs_lat, 192)[1] > 0:
    if orb.get_observer_look(start + (i - 1) * timedelta(minutes=1), obs_long, obs_lat, 192)[1] <= 0:
      begin.append(start + i * timedelta(minutes=1))
    if orb.get_observer_look(start + (i + 1) * timedelta(minutes=1), obs_long, obs_lat, 192)[1] <= 0:
      endd.append(start + i * timedelta(minutes=1))
for j in range (len(begin)):
  print("Диапазон когда спутник виден: c {} до {}".format(begin[j].strftime("%d.%m.%Y %H:%M:%S"), endd[j].strftime("%d.%m.%Y %H:%M:%S")))

