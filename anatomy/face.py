class Face:

    def __init__(self):
        self.__shape = "ND_FACE_SHAPE"

    def set_shape(self, shape):
        self.__shape = shape

    def get_shape(self):
        return self.__shape
