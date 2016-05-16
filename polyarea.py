import math
def area(n,s):
	x=math.pi/n
	area=n*(s**2)/(4*math.tan(x))
	return area