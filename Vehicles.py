from Transport import Transport

class Train(Transport):
    def __init__(self, id, speed, route, price):
        super().__init__(id, speed, route, price)

class Bus(Transport):
    def __init__(self, id, speed, route, price):
        super().__init__(id, speed, route, price)

class Airplane(Transport):
    def __init__(self, id, speed, route, price):
        super().__init__(id, speed, route, price)
