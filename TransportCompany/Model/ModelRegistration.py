from TransportCompany.Entities.Client import Client
from TransportCompany.Repositories.ClientRepository import ClientRepository
from TransportCompany.Repositories.AllRoleRepository import AllRoleRepository


class ModelRegistration:
    def UserRigistation(self, user: Client):
        if not(self.__CheckUserInDB(user)):
            ClientRepository().AddUser(user)
        else:
            raise "Пользователь с таким номером телефона или Email уже есть"

    def __CheckUserInDB(self, user: Client) -> bool:
        return AllRoleRepository().CheckEmail(user.Email)

    def CheckPhone(self, phone):
        return AllRoleRepository().CheckPhone(phone)

    def CheckEmail(self, email):
        return AllRoleRepository().CheckEmail(email)