cmd = input("What Formula you wanna use?\n")
pi = 3.14

def sphere(r):
	a = (((r ** 3) * pi)*4)/3
	print(a)

def cylinder(r,h):
	a = ((r ** 2) * pi * h)
	print(a)

def cone(r,h):
	a = ((r ** 2) * pi  * h)/3
	print(a)

if cmd == "sphere":
	r = int(input("Enter the radius:\n"))
	sphere(r)
elif cmd == "cylinder":
	r = int(input("Enter the radius:\n"))
	h = int(input("Enter the height:\n"))
	cylinder(r,h)
elif cmd == "cone":
	r = int(input("Enter the radius:\n"))
	h = int(input("Enter the height:\n"))
	cone(r,h)
else:
	print(f"There is no Formula Name {cmd}")