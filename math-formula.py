cmd_type = input('''What type of formula you wanna use?
 1 volume
 2 surface area\n''')
cmd = input('''What formula you wanna use? 
 1 cylinder
 2 cone
 3 sphere\n''')
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
    a = ((2 * r * pi)* h)+(2 * pi * (r ** 2))
    print(a)

def cone_sa(r,l):
    a = (pi * r * l)+(pi * (r ** 2))
    print(a)

def sphere_sa(r):
    a = ((r ** 2 ) * pi * 4)
    print(a)

if cmd_type == "volume":
    if cmd == "sphere":
	    r = float(input("Enter the radius:\n"))
	    sphere(r)
    elif cmd == "cylinder":
	    r = float(input("Enter the radius:\n"))
	    h = float(input("Enter the height:\n"))
	    cylinder(r,h)
    elif cmd == "cone":
	    r = float(input("Enter the radius:\n"))
	    h = float(input("Enter the height:\n"))
	    cone(r,h)
elif cmd_type == "surface area":
    if cmd == "cylinder":
        r = float(input("Enter the radius:\n"))
        h = float(input("Enter the height:\n"))
        cylinder_sa(r,h)
    elif cmd == "cone":
        r = float(input("Enter the radius:\n"))
        l = float(input("Enter the slant height:\n"))
        cone_sa(r,l)
    elif cmd == "sphere":
        r = float(input("Enter the radius\n"))
        sphere_sa(r)
else:
	print("An error had occur pls make sure it all lowercase or spell correctly, Thanks - Monke")
