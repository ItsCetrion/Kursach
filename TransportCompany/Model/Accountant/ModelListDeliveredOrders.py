from TransportCompany.Repositories.DeliveredRequestRepositories import DeliveredRequestRepositories


class ModelListDeliveredOrders:
    def GetAllCompletedOrders(self, sort: str):
        return DeliveredRequestRepositories().GetAllCompletedOrders(sort)

    def GetOrderByIdOrder(self, IdOrder: int):
        return DeliveredRequestRepositories().GetOrderByIdOrder(IdOrder)

    def GetInfoOrderAndDriver(self, IdOrder: int):
        return DeliveredRequestRepositories().GetInfoOrderAndDriver(IdOrder)

