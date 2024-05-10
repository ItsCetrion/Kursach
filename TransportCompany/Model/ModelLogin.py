from TransportCompany.Repositories.UserRepository import UserRepository


class ModelLogin:
    @staticmethod
    def GetRole(Email, password) -> bool:
        return UserRepository().GetRole(password, Email)

    # @staticmethod
    #
    # def CheckRole(Email, password):
    #     return UserRepository().CheckRole(Email, password)