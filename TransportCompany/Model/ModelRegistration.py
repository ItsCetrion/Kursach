from TransportCompany.Entities.User import User
from TransportCompany.Repositories.UserRepository import UserRepository
from TransportCompany.Repositories.AllRoleRepository import AllRoleRepository


class ModelRegistration:
    def UserRigistation(self, user: User):
        if not(self.__CheckUserInDB(user)):
            UserRepository.AddUser(user)
        else:
            raise "Пользователь с таким номером телефона или Email уже есть"

    def __CheckUserInDB(self, user: User) -> bool:
        return AllRoleRepository().CheckEmail(user.Email)

    def CheckPhone(self, phone):
        return AllRoleRepository().CheckPhone(phone)

    def CheckEmail(self, email):
        return AllRoleRepository().CheckEmail(email)