from Repositories.DeliveredRequestRepositories import DeliveredRequestRepositories


class ModelListDeliveredOrders:
    @staticmethod
    def GetAllCompletedOrders(sort: str):
        return DeliveredRequestRepositories().GetAllCompletedOrders(sort)

    @staticmethod
    def GetOrderByIdOrder(IdOrder: int):
        return DeliveredRequestRepositories().GetOrderByIdOrder(IdOrder)

    @staticmethod
    def GetInfoOrderAndDriver(IdOrder: int):
        return DeliveredRequestRepositories().GetInfoOrderAndDriver(IdOrder)

