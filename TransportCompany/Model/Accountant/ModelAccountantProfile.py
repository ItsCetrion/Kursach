from TransportCompany.Repositories.AccountantRepository import AccountantRepository


class ModelAccountantProfile:
    def UpdatePhone(self, IdAccountant: int, phone: str):
        AccountantRepository().UpdatePhone(IdAccountant, phone)

    def UpdateEmail(self, IdAccountant: int, email: str):
        AccountantRepository().UpdateEmail(IdAccountant, email)

    def UpdatePassword(self, IdAccountant: int, password: str):
        AccountantRepository().UpdatePassword(IdAccountant, password)