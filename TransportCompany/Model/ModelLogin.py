from TransportCompany.Repositories.AllRoleRepository import AllRoleRepository
from TransportCompany.Repositories.ClientRepository import ClientRepository
from TransportCompany.Repositories.AdministratorRepository import AdministratorRepository
from TransportCompany.Repositories.DriverRepository import DriverRepository
from TransportCompany.Repositories.AccountantRepository import AccountantRepository


class ModelLogin:
    @staticmethod
    def GetEntity(Email: str, password: str) -> list:
        return AllRoleRepository().GetEntity(password, Email)

    @staticmethod
    def GetClient(IdClient: int) -> list:
        return ClientRepository().GetClient(IdClient)

    @staticmethod
    def GetAdmin(IdAdmin: int) -> list:
        return AdministratorRepository().GetAdmin(IdAdmin)

    @staticmethod
    def GetDriver(IdDriver: int) -> list:
        return DriverRepository().GetDriver(IdDriver)

    @staticmethod
    def GetAccountant(IdAccountant: int) -> list:
        return AccountantRepository().GetAccountant(IdAccountant)