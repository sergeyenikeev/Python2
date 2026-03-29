class Point:
    color = 'red'
    circle = 2

print(Point)

print(Point.color)
Point.color = 'blue'
print(Point.color)
print(Point.__dict__)
a = Point()
b = Point()
print(a.color)
print(b.color)
print(type(a))
print(type(b))
print(type(a) == Point)
print(isinstance(a, Point))
Point.circle = 1
print(Point.circle)
print(a.circle)
print(b.circle)
print(a.__dict__)
a.circle = 3
print(a.__dict__)
print(Point.circle)
print(a.circle)
print(b.circle)
Point.circle = 4
print(Point.circle)
print(a.circle)
print(b.circle)
print(Point.__dict__)
print(a.__dict__)
print(b.__dict__)

Point.type_pt = 'disc'
setattr(Point, 'prop', 1)

print(Point.__dict__)
print(a.__dict__)
print(b.__dict__)
tttt = getattr(Point, 'type_pt_pt', False)
print(tttt)
print(Point.__dict__)
delattr(Point, 'prop')
print(Point.__dict__)
