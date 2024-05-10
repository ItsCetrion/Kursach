from TransportCompany.Repositories.AllRoleRepository import AllRoleRepository


class ModelLogin:
    @staticmethod
    def GetRole(Email, password) -> bool:
        return AllRoleRepository().GetRole(password, Email)

    # @staticmethod
    #
    # def CheckRole(Email, password):
    #     return UserRepository().CheckRole(Email, password)