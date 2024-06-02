from TransportCompany.Repositories.AccountantRepository import AccountantRepository


class ModelAccountantProfile:
    @staticmethod
    def UpdatePhone(IdAccountant: int, phone: str):
        AccountantRepository().UpdatePhone(IdAccountant, phone)

    @staticmethod
    def UpdateEmail(IdAccountant: int, email: str):
        AccountantRepository().UpdateEmail(IdAccountant, email)

    @staticmethod
    def UpdatePassword(IdAccountant: int, password: str):
        AccountantRepository().UpdatePassword(IdAccountant, password)