from Repositories.ClientRepository import ClientRepository


class ModelUserProfile:

    @staticmethod
    def UpdatePhone(IdClient, Phone):
        ClientRepository().UpdatePhone(IdClient, Phone)

    @staticmethod
    def UpdateEmail(IdClient, Email):
        ClientRepository().UpdateEmail(IdClient, Email)

    @staticmethod
    def UpdatePassword(IdClient, Password):
        ClientRepository().UpdatePassword(IdClient, Password)