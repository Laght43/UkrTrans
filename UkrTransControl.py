from StationManager import BusStation, TrainStation, AirplaneStation
from Vehicles import Bus, Train, Airplane
import threading
import json

class UkrTransControl():
    def __init__(self, name):
        self.__name = name
        self.__train_stations = []
        self.__bus_stations = []
        self.__airplane_stations = []
        self.__trains = []
        self.__buses = []
        self.__airplanes = []
        self.__save_file = "save_data.json"

    def save(self):
        """Save all data to json file"""
        data = dict()

        data["name"] = self.__name

        trains = dict()
        for train in self.__trains:
            train_data = {
                "speed": train.speed,
                "route": [station.id for station in train.route],
                "price": train.price
            }
            trains[train.id] = train_data
        data["trains"] = trains

        buses = dict()
        for bus in self.__buses:
            bus_data = {
                "speed": bus.speed,
                "route": [station.id for station in bus.route],
                "price": bus.price
            }
            buses[bus.id] = bus_data
        data["buses"] = buses

        airplanes = dict()
        for airplane in self.__airplanes:
            airplane_data = {
                "speed": airplane.speed,
                "route": [station.id for station in airplane.route],
                "price": airplane.price
            }
            airplanes[airplane.id] = airplane_data
        data["airplanes"] = airplanes

        train_stations = dict()
        for train_station in self.__train_stations:
            train_station_data = {
                "name": train_station.name,
                "pos_x": train_station.pos_x,
                "pos_y": train_station.pos_y,
                "stop_time": train_station.stop_time
            }
            train_stations[train_station.id] = train_station_data
        data["train_stations"] = train_stations

        bus_stations = dict()
        for bus_station in self.__bus_stations:
            bus_station_data = {
                "name": bus_station.name,
                "pos_x": bus_station.pos_x,
                "pos_y": bus_station.pos_y,
                "stop_time": bus_station.stop_time
            }
            bus_stations[bus_station.id] = bus_station_data
        data["bus_stations"] = bus_stations

        airplane_stations = dict()
        for airplane_station in self.__airplane_stations:
            airplane_station_data = {
                "name": airplane_station.name,
                "pos_x": airplane_station.pos_x,
                "pos_y": airplane_station.pos_y,
                "stop_time": airplane_station.stop_time
            }
            airplane_stations[airplane_station.id] = airplane_station_data
        data["airplane_stations"] = airplane_stations

        with open(self.__save_file, "w") as f:
            json.dump(data, f, indent=4)

    def load(self):
        """Load data from json file"""
        with open(self.__save_file, "r") as f:
            data = json.load(f)

            self.__name = data["name"]

            train_stations = data["train_stations"]
            for train_station_data in train_stations.values():
                name = train_station_data["name"]
                id = len(self.__train_stations)
                pos_x = train_station_data["pos_x"]
                pos_y = train_station_data["pos_y"]
                stop_time = train_station_data["stop_time"]
                train_station = TrainStation(name, id, pos_x, pos_y, stop_time)
                self.__train_stations.append(train_station)

            bus_stations = data["bus_stations"]
            for bus_station_data in bus_stations.values():
                name = bus_station_data["name"]
                id = len(self.__bus_stations)
                pos_x = bus_station_data["pos_x"]
                pos_y = bus_station_data["pos_y"]
                stop_time = bus_station_data["stop_time"]
                bus_station = BusStation(name, id, pos_x, pos_y, stop_time)
                self.__bus_stations.append(bus_station)

            airplane_sations = data["airplane_stations"]
            for airplane_staion_data in airplane_sations.values():
                name = airplane_staion_data["name"]
                id = len(self.__airplane_stations)
                pos_x = airplane_staion_data["pos_x"]
                pos_y = airplane_staion_data["pos_y"]
                stop_time = airplane_staion_data["stop_time"]
                airplane_station = AirplaneStation(name, id, pos_x, pos_y, stop_time)
                self.__airplane_stations.append(airplane_station)

            trains = data["trains"]
            for train_data in trains.values():
                id = len(self.__trains)
                speed = train_data["speed"]
                stations = train_data["route"]
                route = self.__load_route_helper(self.__train_stations, stations)
                price = train_data["price"]
                train = Train(id, speed, route, price)
                self.__trains.append(train)

            buses = data["buses"]
            for bus_data in buses.values():
                id = len(self.__buses)
                speed = bus_data["speed"]
                stations = bus_data["route"]
                route = self.__load_route_helper(self.__bus_stations, stations)
                price = bus_data["price"]
                bus = Bus(id, speed, route, price)
                self.__buses.append(bus)

            airplanes = data["airplanes"]
            for airplane_data in airplanes.values():
                id = len(self.__airplanes)
                speed = airplane_data["speed"]
                stations = airplane_data["route"]
                route = self.__load_route_helper(self.__airplanes, stations)
                price = airplane_data["price"]
                airplane = Airplane(id, speed, route, price)
                self.__airplanes.append(airplane)

    def __load_route_helper(self, stations, route_stations):
        """Helper function to create route in load"""
        result = []
        for station in stations:
            for i in route_stations:
                if station.id == i:
                    result.append(station)
        return result
            
    def show_stations(self):
        """"Show information about all stations"""
        print("=====Train stations=====")
        for train_station in self.__train_stations:
            train_station.show_info()
        print("====Bus stations=====")
        for bus_station in self.__bus_stations:
            bus_station.show_info()
        print("=====Airplane stations=====")
        for airplane_station in self.__airplane_stations:
            airplane_station.show_info()

    def show_vehicles(self):
        """"Show information about all vehicles"""
        print("=====Trains=====")
        for train in self.__trains:
            train.show_info()
        print("=====Buses=====")
        for bus in self.__buses:
            bus.show_info()
        print("=====Airplanes=====")
        for airplane in self.__airplanes:
            airplane.show_info()

    def __add_station_helper(self, station_list):
        """"
        Helper function to get station input from user
        Return tuple or None if error
        """
        try:
            name = input("Enter station name: ")
            id = len(station_list)
            pos_x = int(input("Enter station pos x(in kilometers(int)): "))
            pos_y = int(input("Enter station pos y(in kilometers(int)): "))
            stop_time = float(input("Enter stop time(in hours(can be float))"))
            return name, id, pos_x, pos_y, stop_time
        except ValueError:
            print("invalid input")
            return None
        except KeyboardInterrupt:
            print("error")
            return None

    def add_station(self):
        """Create a station of chosen type"""
        type = input("Enter station type(train, bus, airplane): ")
        match type:
            case "train":
                result = self.__add_station_helper(self.__train_stations)
                if result:
                    train_station = TrainStation(*result)
                    self.__train_stations.append(train_station)
            case "bus":
                result = self.__add_station_helper(self.__bus_stations)
                if result:
                    bus_station = BusStation(*result)
                    self.__bus_stations.append(bus_station)
            case "airplane":
                result = self.__add_station_helper(self.__airplane_stations)
                if result:
                    airplane_station = AirplaneStation(*result)
                    self.__airplane_stations.append(airplane_station)
            case _:
                print("invalid station type")
                return

    def __add_vehicle_helper(self, vehicle_list):
        """
        Helper function to get vehicle input from user
        Return tuple or None if error
        """
        try:
            id = len(vehicle_list)
            speed = int(input("Enter train speed(in kilometers per hour(int)): "))
            if speed <= 0:
                raise ValueError
            return id, speed
        except ValueError:
            print("invalid input")
            return None
        except KeyboardInterrupt:
            print("error")
            return None

    def add_vehicle(self):
        """Create vehicle of chosen type"""
        type = input("Enter transport type(train, bus, airplane): ")
        match type:
            case "train":
                result = self.__add_vehicle_helper(self.__trains)
                if result:
                    train = Train(*result)
                    self.__trains.append(train)
            case "bus":
                result = self.__add_vehicle_helper(self.__buses)
                if result:
                    bus = Bus(*result)
                    self.__buses.append(bus)
            case "airplane":
                result = self.__add_vehicle_helper(self.__airplanes)
                if result:
                    airplane = Airplane(*result)
                    self.__airplanes.append(airplane)
            case _:
                print("invalid type input")
                return

    def __add_route_helper(self, vehicle_list, stations_list, vehicle_id):
        """
        Helper function to get rout input from user
        Return tuple or None if error
        """
        if vehicle_id < 0 or vehicle_id >= len(vehicle_list):
            print("invalid input id")
            return None
        stations_count = int(input("Enter how many stations will be in route: "))
        if 2 > stations_count or stations_count > len(stations_list):
            print("incorrect stations count")
            return None

        route = []
        for i in range(stations_count):
            station_id = int(input("Enter station id: "))
            for j, station in enumerate(stations_list):
                if j == station_id and station not in route:
                    route.append(station)

        price = int(input("Enter price for this route: "))
        return route, price


    def add_route(self):
        """Create route for chosen transporn"""
        try:
            type = input("Enter type of vehicle(train, bus, airplane): ")
            vehicle_id = int(input("Enter vehicle id: "))
            match type:
                case "train":
                    if len(self.__train_stations) < 2:
                        raise ValueError("not enough stations to create route")
                    result = self.__add_route_helper(self.__trains, self.__train_stations, vehicle_id)
                    if result:
                        self.__trains[vehicle_id].add_route(*result)
                case "bus":
                    if len(self.__bus_stations) < 2:
                        raise ValueError("not enough stations to create route")
                    result = self.__add_route_helper(self.__buses, self.__bus_stations, vehicle_id)
                    if result:
                        self.__buses[vehicle_id].add_route(*result)
                case "airplane":
                    if len(self.__airplane_stations) < 2:
                        raise ValueError("not enough stations to create route")
                    result = self.__add_route_helper(self.__airplanes, self.__airplane_stations, vehicle_id)
                    if result:
                        self.__airplanes[vehicle_id].add_route(*result)
                case _:
                    print("invalid vehicle input")
                    return
        except ValueError:
            print("invalid input")
        except KeyboardInterrupt:
            print("error")

    def start_transport(self):
        """Starting moving transport"""
        type =  input("Enter transport type to start move(trains, buses, airplanes, all): ")
        threads = []
        match type:
            case "trains":
                for train in self.__trains:
                    thread = threading.Thread(target=train.move, name=f"Train-{train.id}")
                    threads.append(thread)
                    thread.start()
            case "buses":
                for bus in self.__buses:
                    thread = threading.Thread(target=bus.move, name=f"Bus-{bus.id}")
                    threads.append(thread)
                    thread.start()
            case "airplanes":
                for airplane in self.__airplanes:
                    thread = threading.Thread(target=airplane.move, name=f"Airplane-{airplane.id}")
                    threads.append(thread)
                    thread.start()
            case "all":
                all_vehicles = self.__trains + self.__buses + self.__airplanes
                for vehicle in all_vehicles:
                    thread = threading.Thread(target=vehicle.move, name=f"{vehicle.__class__.__name__}-{vehicle.id}")
                    threads.append(thread)
                    thread.start()
            case _:
                print("invalid input")
                return

        for thread in threads:
            thread.join()

    def stop_transport(self):
        """Stop moving transport"""
        type =  input("Enter transport type to start move(trains, buses, airplanes, all): ")
        match type:
            case "trains":
                for train in self.__trains:
                    train.stop()
            case "buses":
                for bus in self.__buses:
                    bus.stop()
            case "airplanes":
                for airplane in self.__airplanes:
                    airplane.stop()
            case "all":
                all_vehicles = self.__trains + self.__buses + self.__airplanes
                for vehicle in all_vehicles:
                    vehicle.stop()
            case _:
                print("invalid input")
                return