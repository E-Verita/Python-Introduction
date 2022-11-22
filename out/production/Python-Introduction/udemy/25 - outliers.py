data = [ 4, 5, 104, 105, 110, 120, 130, 130, 150, 160, 170, 183, 185, 187, 188, 191, 350, 360]
print(data)
del data [0:2]
print(data)
del data[14:]
print(data)

#datax = [4, 5, 104, 105, 110, 120, 130, 130, 150, 160, 170, 183, 185, 187, 188, 191, 350, 360]
datax = [1104, 1105, 1110, 1120, 1310, 1130, 1150, 1610, 1710, 11183, 1815, 1871, 1818, 1191]
min_valid = 100
max_valid = 200

# Be careful while changing the size of the object that you are iterating over
"""
will not work, as index positions get changed:

for index, value in enumerate(datax):
    if (value < min_valid) or (value > max_valid):
        del datax[index]
print(datax)
"""

# low values
stop = 0
for index, value in enumerate(datax):
    if value >= min_valid:
        stop = index
        break
print(stop)
del datax[:stop]
print(datax)

# high values
start = 0
for index in range(len(datax) - 1, -1, -1):
    print(datax[index], index)
    if datax[index] <= max_valid:
        # we have the index of the last item to keep
        # set start to the position of the first item to delete (index + 1)
        start = index + 1
        break
print(start)
del datax[start:]
print(datax)



