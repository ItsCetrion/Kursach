from Entities.Client import Client
from Repositories.ClientRepository import ClientRepository
from Repositories.AllRoleRepository import AllRoleRepository


class ModelRegistration:
    def UserRigistation(self, user: Client):
        if not(self.__CheckUserInDB(user)):
            ClientRepository().AddUser(user)
        else:
            raise "Пользователь с таким номером телефона или Email уже есть"

    @staticmethod
    def __CheckUserInDB(user: Client) -> bool:
        return AllRoleRepository().CheckEmail(user.Email)

    @staticmethod
    def CheckPhone(phone):
        return AllRoleRepository().CheckPhone(phone)

    @staticmethod
    def CheckEmail(email):
        return AllRoleRepository().CheckEmail(email)