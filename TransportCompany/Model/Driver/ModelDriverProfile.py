from TransportCompany.Repositories.DriverRepository import DriverRepository


class ModelDriverProfile:
    @staticmethod
    def UpdatePhone(IdDriver, phone):
        DriverRepository().UpdatePhone(IdDriver, phone)

    @staticmethod
    def UpdateEmail(IdDriver, email):
        DriverRepository().UpdateEmail(IdDriver, email)

    @staticmethod
    def UpdatePassword(IdDriver, password):
        DriverRepository().UpdatePassword(IdDriver, password)