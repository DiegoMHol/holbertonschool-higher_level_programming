#!/usr/bin/python3
""" Python Almost a circle Proyect """
from models.base import Base


class Rectangle(Base):
    """ Class Rectangle that inherits from Base """
    def __init__(self, width, height, x=0, y=0, id=None):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
        self.coordinate_validator("x", x)
        self.__x = x
        self.coordinate_validator("y", y)
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.integer_validator("width", value)
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.integer_validator("height", value)
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.coordinate_validator("x", value)
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.coordinate_validator("y", value)
        self.__y = value

    def area(self):
        return self.__width * self.__height

    def display(self):
        for i in range(self.__y):
            print("")
        for j in range(self.__height):
            for k in range(self.__x):
                print(" ", end="")
            for a in range(self.__width):
                print("#", end="")
            print("")

    def __str__(self):
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x,
                                                        self.__y, self.__width,
                                                        self.__height))

    def update(self, *args, **kwargs):
        if args and len(args) > 0:
            self.id = args[0]
            if len(args) > 1:
                self.integer_validator("width", args[1])
                self.__width = args[1]
            if len(args) > 2:
                self.integer_validator("height", args[2])
                self.__height = args[2]
            if len(args) > 3:
                self.coordinate_validator("x", args[3])
                self.__x = args[3]
            if len(args) > 4:
                self.coordinate_validator("y", args[4])
                self.__y = args[4]
        else:
            if kwargs is not None:
                for key, value in kwargs.items():
                    if key == 'width':
                        self.integer_validator("width", value)
                    if key == 'height':
                        self.integer_validator("height", value)
                    if key == 'x':
                        self.coordinate_validator("x", value)
                    if key == 'y':
                        self.coordinate_validator("y", value)
                    setattr(self, key, value)

    def to_dictionary(self):
        return {'x': self.__x, 'y': self.__y,
                'id': self.id, 'height': self.__height, 'width': self.__width}
