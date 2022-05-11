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

def cylinder_sa(r,h):
    a = (2 * h * r *pi)+(pi * (r ** 2))
    print(a)

def cone_sa(r,l):
    a = (pi * r * l)+(pi * (r ** 2))
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
elif cmd == "cylinder_sa":
    r = int(input("Enter the radius:\n"))
    h = int(input("Enter the height:\n"))
    cylinder(r,h)
elif cmd == "cone_sa":
    r = int(input("Enter the radius:\n"))
    l = int(input("Enter the slant height:\n"))
    cone_sa(r,l)
else:
	print(f"There is no Formula Name {cmd}")
