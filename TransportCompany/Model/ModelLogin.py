from TransportCompany.Repositories.AllRoleRepository import AllRoleRepository
from TransportCompany.Repositories.ClientRepository import ClientRepository
from TransportCompany.Repositories.AdministratorRepository import AdministratorRepository
from TransportCompany.Repositories.DriverRepository import DriverRepository
from TransportCompany.Repositories.AccountantRepository import AccountantRepository


class ModelLogin:
    @staticmethod
    def GetEntity(Email, password) -> list:
        return AllRoleRepository().GetEntity(password, Email)

    def GetClient(self, IdClient):
        return ClientRepository().GetClient(IdClient)

    def GetAdmin(self, IdAdmin):
        return AdministratorRepository().GetAdmin(IdAdmin)

    def GetDriver(self, IdDriver):
        return DriverRepository().GetDriver(IdDriver)

    def GetAccountant(self, IdAccountant):
        return AccountantRepository().GetAccountant(IdAccountant)

    # @staticmethod
    #
    # def CheckRole(Email, password):
    #     return UserRepository().CheckRole(Email, password)