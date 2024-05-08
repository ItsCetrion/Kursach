from TransportCompany.UserRepository.UserRepository import UserRepository


class ModelLogin:
    @staticmethod
    def CheckUserInDB(Email, password) -> bool:
        return UserRepository().CheckPasswordAndEmail(password, Email)