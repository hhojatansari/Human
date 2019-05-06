from anatomy.organs import Organs
from personality import Personality


class Human:

    def __init__(self, first_name="ND_FNAME", last_name="ND_LNAME"):

        self.personality = Personality(first_name, last_name)
        self.organs = Organs()

    def information(self):

        print("\n\nMy name is", self.personality.get_name()[0], self.personality.get_name()[1] + '.',
              "i'm", self.personality.get_nationality() + '.',
              "my eye color is", self.organs.eye.get_color() + '.',
              "and my face shape is", self.organs.head.get_shape() + '.\n')
