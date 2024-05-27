from TransportCompany.Repositories.DriverRepository import DriverRepository
class ModelDriverProfile:
    def UpdatePhone(self, IdDriver, phone):
        DriverRepository().UpdatePhone(IdDriver, phone)

    def UpdateEmail(self, IdDriver, email):
        DriverRepository().UpdateEmail(IdDriver, email)

    def UpdatePassword(self, IdDriver, password):
        DriverRepository().UpdatePassword(IdDriver, password)