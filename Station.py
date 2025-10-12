from abc import ABC

class Station(ABC):
    def __init__(self, name: str, id: int, pos_x: int, pos_y: int, stop_time: float):
        self._name = name
        self._id = id
        self._pos_x = pos_x
        self._pos_y = pos_y
        self._stop_time = stop_time

    def show_info(self):
        """Show info about station"""
        print(f"Name: {self._name} Id: {self._id} Position: {self._pos_x} {self._pos_y} stop time: {self._stop_time}")

    @property
    def name(self):
        return self._name

    @property
    def id(self):
        return self._id

    @property
    def pos_x(self):
        return self._pos_x

    @property
    def pos_y(self):
        return self._pos_y

    @property
    def stop_time(self):
        return self._stop_time