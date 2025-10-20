from abc import ABC
from time import sleep
import math

class Transport(ABC):
    """
    abstract class for all another transports types
    """
    def __init__(self, id: int, speed: int, route=None, price=None):
        self._id = id
        self._speed = speed
        self._route = list(route) if route else []
        self._time_coeficient = 5 # how many seconds will take 1 hour in program
        self._price = price
        self._current_station = None
        self._is_running = True

    def show_info(self):
        """Show info about transport"""
        if len(self._route) != 0:
            print(f"id: {self._id} speed: {self._speed} start: {self._route[0].name} end: {self._route[-1].name}")
        else:
            print(f"id: {self._id} speed: {self._speed}")

    def add_route(self, stations, price):
        """adding route"""
        self._price = price
        self._route = stations
        self._current_station = self._route[0]

    def move(self):
        """moving transport between stations with speed of that transport"""
        if len(self._route) == 0:
            print(f"[{self.__class__.__name__}-{self._id}] No route for this transport")
            return

        thread_name = f"{self.__class__.__name__}-{self._id}"
        print(f"[{thread_name}] Starting circular route from {self._route[0].name}")

        while self._is_running:
            # Рух вперед
            print(f"[{thread_name}] >>> Going FORWARD")
            self._move_direction(self._route, thread_name)

            # Рух назад (реверс маршруту)
            print(f"[{thread_name}] <<< Going BACKWARD")
            self._move_direction(self._route[::-1], thread_name)

    def _move_direction(self, route, thread_name):
        """Helper method to move in one direction"""
        for i in range(len(route)):
            if i == len(route) - 1:
                print(f"[{thread_name}] Reached end point: {route[i].name}")
                return

            print(f"[{thread_name}] At station: {route[i].name}")

            distance = self.get_distance(route[i], route[i+1])
            time = distance / self._speed

            print(f"[{thread_name}] Moving to {route[i+1].name} ({distance:.2f}km, {time:.2f}h)")
            sleep(time)

            self._current_station = route[i+1]
            stop_time = route[i+1].stop_time * self._time_coeficient

            print(f"[{thread_name}] Stopped at {route[i+1].name} for {stop_time:.2f}h")
            sleep(stop_time)

    def stop(self):
        """Stop the transport"""
        self._is_running = False

    @staticmethod
    def get_distance(station1, station2):
        result = math.sqrt((station1.pos_x - station2.pos_x)**2 + (station1.pos_y - station2.pos_y)**2)
        return result

    @property
    def speed(self):
        return self._speed

    @property
    def id(self):
        return self._id

    @property
    def current_station(self):
        return self._current_station

    @property
    def route(self):
        return self._route

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        self._price = price
