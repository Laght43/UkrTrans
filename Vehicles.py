from Transport import Transport

class Train(Transport):
    def __init__(self, id, speed):
        super().__init__(id, speed)

class Bus(Transport):
    def __init__(self, id, speed):
        super().__init__(id, speed)

class Airplane(Transport):
    def __init__(self, id, speed):
        super().__init__(id, speed)