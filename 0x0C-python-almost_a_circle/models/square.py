#!/usr/bin/python3
""" Python Almost a Circle Proyect """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Class That inherits from Rectangle """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """ Comments test or checkcer """
        return ("[Square] ({}) {}/{} - {}"
                .format(self.id, self.x, self.y,
                        self.size))

    @property
    def size(self):
        """ Comments test or checkcer """
        return self.width

    @size.setter
    def size(self, value):
        """ Comments test or checkcer """
        self.integer_validator("width", value)
        self.width = value

    def update(self, *args, **kwargs):
        """ Comments test or checkcer """
        if args and len(args) > 0:
            self.id = args[0]
            if len(args) > 1:
                self.integer_validator("width", args[1])
            if len(args) > 2:
                self.coordinate_validator("x", args[2])
            if len(args) > 3:
                self.coordinate_validator("y", args[3])
        else:
            if kwargs is not None:
                for key, value in kwargs.items():
                    if key == 'size':
                        self.integer_validator("width", value)
                    if key == 'x':
                        self.coordinate_validator("x", value)
                    if key == 'y':
                        self.coordinate_validator("y", value)
                    setattr(self, key, value)

    def to_dictionary(self):
        """ Comments test or checkcer """
        return {'id': self.id, 'x': self.x,
                'size': self.size, 'y': self.y}
