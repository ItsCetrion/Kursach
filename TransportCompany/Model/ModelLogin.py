from TransportCompany.Repositories.UserRepository import UserRepository


class ModelLogin:
    @staticmethod
    def GetUserRole(Email, password) -> bool:
        return UserRepository().GetUserRole(password, Email)

    @staticmethod
    def CheckRole(Email, password):
        return UserRepository().CheckRole(Email, password)