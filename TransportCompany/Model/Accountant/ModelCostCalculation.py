from TransportCompany.Repositories.DeliveredRequestRepositories import DeliveredRequestRepositories


class ModelCostCalculation:
    def UpdateRevenue(self, Idriver, IdOrder, Revenue):
        DeliveredRequestRepositories().UpdateRevenue(Idriver, IdOrder, Revenue)