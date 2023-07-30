class Station:
    def __init__(self, ID: int, X: float, Y: float):
        self.ID = ID
        self.X = X
        self.Y = Y
        self.containers = []
        self.history = []
        self.current = []

    def __str__(self) -> str:
        return f"Station :\n[ ID : {self.ID}\n X : {self.X}\n Y : {self.Y} ]"

    @staticmethod
    def create_station(station_id: int, x: float, y: float):
        station = Station(station_id, x, y)
        return station

    def getDistance(self, other) -> float:
        return ((self.X - other.X) ** 2 + (self.Y - other.Y) ** 2) ** 0.5

    def incoming_freightcar(self, freightcar):
        self.current.append(freightcar)

    def outgoing_freightcar(self, freightcar):
        self.history.append(freightcar)
        self.current.remove(freightcar)
