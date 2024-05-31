class CostTrip:
    def __init__(self):
        self.diesel = 65
        self.benzine92 = 51
        self.TruckConsumption = 30
        self.GazelleConsumption = 10

    def __CostKm(self, wight: int) -> int:
        if wight <= 1500: return 30
        if wight <= 3000: return 40
        if wight <= 5000: return 50
        if wight <= 10000: return 60
        if wight <= 20000: return 70

    def __GazelleOrTruck(self, distance: float) -> str:
        if distance <= 100: return "Gazell"
        else: return "Truck"

    def Calcilating(self, distance: float, wight: int) -> float:
        transport = self.__GazelleOrTruck(distance)
        if transport == "Gazell":
            RevenueTrip = 20 * distance
            FuelConsumption = distance / 100 * self.GazelleConsumption * self.benzine92
            profit = RevenueTrip - FuelConsumption
            return profit
        elif transport == "Truck":
            CostKm = self.__CostKm(wight)
            RevenueTrip = CostKm * distance
            FuelConsumption = distance / 100 * self.TruckConsumption * self.diesel
            profit = RevenueTrip - FuelConsumption
            return profit
