from Transport import Transport

class Train(Transport):
    def __init__(self, id, speed, route=None, price=None):
        super().__init__(id, speed, route, price)

class Bus(Transport):
    def __init__(self, id, speed, route=None, price=None):
        super().__init__(id, speed, route, price)

class Airplane(Transport):
    def __init__(self, id, speed, route=None, price=None):
        super().__init__(id, speed, route, price)
