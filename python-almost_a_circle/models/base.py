class Base:    
    __nb_objects = 0  # private class attribute

    def __init__(self id=None):

        if id is not None:  # if id is given assign it to the instance attribute id
            self.id = id
        else:  # if id is not given increment __nb_objects and assign it to the instance attribute id
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
