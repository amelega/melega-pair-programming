import math

def polar_to_cartesian(r, theta):
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    return x, y

r = 5
theta = math.pi/3

x, y = polar_to_cartesian(r, theta)
x = round(x, 4)
y = round(y, 4)
print('Cartesian coordinates are: x =', x, 'and y =', y)