from Station import Station

class TrainStation(Station):
    def __init__(self, name, id, pos_x, pos_y, stop_time):
        super().__init__(name, id, pos_x, pos_y, stop_time)

class BusStation(Station):
        def __init__(self, name, id, pos_x, pos_y, stop_time):
             super().__init__(name, id, pos_x, pos_y, stop_time)

class AirplaneStation(Station):
     def __init__(self, name, id, pos_x, pos_y, stop_time):
          super().__init__(name, id, pos_x, pos_y, stop_time)