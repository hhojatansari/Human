from anatomy.head import Head
from anatomy.mouth import Mouth
from anatomy.eye import Eye


class Organs:

    def __init__(self):
        self.head = Head()
        self.mouth = Mouth()
        self.eye = Eye()
