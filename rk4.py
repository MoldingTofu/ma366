# https://en.wikipedia.org/wiki/Runge%E2%80%93Kutta_methods#The_Runge%E2%80%93Kutta_metho}}d

from decimal import Decimal

def f(t, y):
	r = (3-y)*(3-y)*(y+1)
	return Decimal(r)

y = Decimal('2')
t = Decimal('0')
print((t, y))
step = Decimal('1')
for i in range(5):
	k1 = f(t, y)
	k2 = f(t + (step / Decimal('2')), y + (step * k1) / Decimal('2'))
	k3 = f(t + (step / Decimal('2')), y + (step * k2) / Decimal('2'))
	k4 = f(t + step, y + step * k3)

	y += Decimal('1')/Decimal('6') * step * (k1 + 2*k2 + 2*k3 + k4)
	t += step
	print((t, y))
