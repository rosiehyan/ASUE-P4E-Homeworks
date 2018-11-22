iterations = int (input ('How many iterations? '))
x_min = 0

def f(x):
    return 0.05*x**4 + 0.1*x**3 + 0.5*x**2 + 10*x +5
f(x_min)

def f_d1(x):
    return 0.2*x**3 + 0.3*x**2 + 1*x + 10

def f_d2(x):
    return 0.6*x**2 +0.6*x + 1

x_min = int(input('Enter a minimum value.'))

for i in range(1, iterations + 1):
    estimated_x_min = x_min - f_d1(x_min)/f_d2(x_min)

    print('Initial x_min value is', x_min )

    print('Estimated value of x_min after iteration:', i, estimated_x_min )
    x_min= estimated_x_min

