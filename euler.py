from decimal import Decimal

def d(i, t, y):
	r = (3-y)*(3-y)*(y+1)
	#print(f'm_{i} &= (3-{y})^2({y}+1) = {r}\\\\')
	return r

def f(i, t_0, y_0, m, t):
	r = y_0 + m * (t-t_0)
	#print(f'y_{i} &= {y_0} + {m} \\times ({t}-{t_0}) = {r}\\\\')
	return y_0 + m * (t-t_0)

y = Decimal('2')
t = Decimal('0')
print((t, y))
m = d(0, t, y)
step = Decimal('1')
for i in range(5):
	#print(f't_{i+1} &= {t} + {step} = {t+step}\\\\')
	y = f(i+1, t, y, m, t+step)
	t += step
	#print(f'&\Rightarrow ({t},{y})\\\\\\\\')
	print((t, y))
	m = d(i+1, t+step, y)
