from TransportCompany.Repositories.ClientRepository import ClientRepository

class ModelUserProfile:

    def UpdatePhone(self, IdClient, Phone):
        ClientRepository().UpdatePhone(IdClient, Phone)

    def UpdateEmail(self, IdClient, Email):
        ClientRepository().UpdateEmail(IdClient, Email)

    def UpdatePassword(self, IdClient, Password):
        ClientRepository().UpdatePassword(IdClient, Password)