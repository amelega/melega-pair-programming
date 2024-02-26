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


# Feedback: Function works great. Variables have very clear names. Might want to add comments explaining what each line does

#Test 1:

r = 10
theta = math.pi
polar_to_cartesian(r, theta)
print('Cartesian coordinates are: x =', x, 'and y =', y)

#Test 2:

r = 15
theta = math.pi/6
polar_to_cartesian(r, theta)
print('Cartesian coordinates are: x =', x, 'and y =', y)

