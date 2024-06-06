from Repositories.DeliveredRequestRepositories import DeliveredRequestRepositories


class ModelCostCalculation:
    @staticmethod
    def UpdateRevenue(Idriver, IdOrder, Revenue):
        DeliveredRequestRepositories().UpdateRevenue(Idriver, IdOrder, Revenue)