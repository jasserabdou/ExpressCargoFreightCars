from station import Station


class FreightCar:
    def __init__(self, ID: int, currentStation: Station, totalWeightCapacity: int,
                 maxNumberOfAllContainers: int, maxNumberOfHeavyContainers: int,
                 maxNumberOfRefrigeratedContainers: int, maxNumberOfLiquidContainers: int,
                 double_fuelConsumptionPerKM: float):
        self.ID = ID
        self.double_fuel = 0
        self.currentStation = currentStation
        self.totalWeightCapacity = totalWeightCapacity
        self.maxNumberOfAllContainers = maxNumberOfAllContainers
        self.maxNumberOfHeavyContainers = maxNumberOfHeavyContainers
        self.maxNumberOfRefrigeratedContainers = maxNumberOfRefrigeratedContainers
        self.maxNumberOfLiquidContainers = maxNumberOfLiquidContainers
        self.double_fuelConsumptionPerKM = double_fuelConsumptionPerKM
        self.fuelConsumption = 0
        self.containers = []

    def __str__(self) -> str:
        return f"FreightCar :\n[ FreightCar ID : {self.ID}\nCurrent Station ID : {self.currentStation.ID}\nFreightCar totalWeightCapacity : {self.totalWeightCapacity}\nMaxNumberOfAllContainers : {self.maxNumberOfAllContainers}\nMaxNumberOfHeavyContainers : {self.maxNumberOfHeavyContainers}\nMaxNumberOfRefrigeratedContainers : {self.maxNumberOfRefrigeratedContainers}\nMaxNumberOfLiquidContainers : {self.maxNumberOfLiquidContainers}\nDoublefuelConsumptionPerK : {self.double_fuelConsumptionPerKM} ]"

    def getCurrentContainers(self):
        return sorted(self.containers, key=lambda container: container.ID)

    def load_container(self, container):
        if container.ID != self.currentStation.ID:
            print(
                f"Container {container.ID} is not in the same station as FreightCar {self.ID}.")
            return False

        if len(self.containers) >= self.maxNumberOfAllContainers:
            print(
                f"FreightCar {self.ID} is already at its maximum capacity for containers.")
            return False

        if container.type == "HeavyContainer" and len([c for c in self.containers if c.type == "HeavyContainer"]) >= self.maxNumberOfHeavyContainers:
            print(f"FreightCar {self.ID} cannot load more HeavyContainers.")
            return False

        if container.type == "RefrigeratedContainer" and len([c for c in self.containers if c.type == "RefrigeratedContainer"]) >= self.maxNumberOfRefrigeratedContainers:
            print(
                f"FreightCar {self.ID} cannot load more RefrigeratedContainers.")
            return False

        if container.type == "LiquidContainer" and len([c for c in self.containers if c.type == "LiquidContainer"]) >= self.maxNumberOfLiquidContainers:
            print(f"FreightCar {self.ID} cannot load more LiquidContainers.")
            return False

        self.containers.append(container)
        self.currentStation.containers.remove(container)
        print(f"Container {container.ID} loaded into FreightCar {self.ID}.")
        return True

    def unload_container(self, container_id: int, current_station: Station):
        container = None
        for c in self.containers:
            if c.ID == container_id:
                container = c
                break

        if container is None:
            print(f"Container {container_id} is not in FreightCar {self.ID}.")
            return

        self.containers.remove(container)
        container.station_id = current_station.ID
        current_station.containers.append(container)

    def calculate_fuel_consumption(self, destination_station):
        total_consumption = sum(container.double_consumption()
                                for container in self.containers)
        fuel_needed = self.currentStation.getDistance(
            destination_station) * self.double_fuelConsumptionPerKM + total_consumption
        return fuel_needed <= self.double_fuel

    def frightcar_to_station(self, station, distance):
        self.currentStation = station
        self.fuelConsumption += self.double_fuelConsumptionPerKM * distance
        return self.currentStation

    def add_fuel(self, fuel_amount):
        if fuel_amount <= 0:
            print(
                f"Fuel amount must be positive. FreightCar {self.ID} fuel not changed.")
            return
        self.double_fuel += fuel_amount
