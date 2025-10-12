from StationManager import BusStation, TrainStation, AirplaneStation
from Vehicles import Bus, Train, Airplane
import threading

class UkrTransControl():
    def __init__(self, name):
        self.__name = name
        self.__train_stations = []
        self.__bus_stations = []
        self.__airplane_stations = []
        self.__trains = []
        self.__buses = []
        self.__airplanes = []

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