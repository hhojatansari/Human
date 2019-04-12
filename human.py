from appearance import Appearance
from personality import Personality
from anatomy.organs import Organs

class Human(Appearance, Personality, Organs):

    def __init__(self, fname, lname):
        self.set_name(fname, lname)

    def information(self):
        print("\n\nMy name is", self.get_name()[0], self.get_name()[1] + '.',
              "i'm", self.get_nationality() + '.',
              "my eye color is", self.eye.get_color() + '.',
              "and my face shape is", self.face.get_shape() + '.\n')
