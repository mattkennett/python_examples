from Polygon import Triangle, Polygon

my_triangle = Triangle(name='Tri', width=5, height=6)

my_tuple = ('abcd', 3, 14.73, my_triangle)

for item in my_tuple:
    print('My item is of type: %s' % type(item))
    print('My item\'s value is: %s' % item)