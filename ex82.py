import ephem

j = ephem.Jupiter()
j.compute("1230/1/1")
dis = j.sun_distance
kilomdis = dis*149600000
print(kilomdis)

