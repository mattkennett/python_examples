class Polygon:
    def __init__(self, **kwargs):
        self.width = kwargs['width'] if 'width' in kwargs else 0
        self.height = kwargs['height'] if 'height' in kwargs else 0
        self.num_sides = kwargs['num_sides'] if 'num_sides' in kwargs else 0

class  Triangle(Polygon):
    def __init__(self, **kwargs):
        self.name = kwargs['name'] if 'name' in kwargs else 0
        
        kwargs['num_sides'] = 3
        super(Triangle, self).__init__(**kwargs)
    
    def __str__(self):
        return_string =  'My Name is: %s\n' % self.name
        return_string += 'My area is: %f\n' % self.get_area()
        return_string += 'I have %d sides' % self.num_sides
        return return_string
    
    def get_area(self):
        return self.width * self.height / 2.0