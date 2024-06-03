from TransportCompany.Repositories.AllRoleRepository import AllRoleRepository
from TransportCompany.Repositories.AccountantRepository import AccountantRepository
from TransportCompany.Repositories.DriverRepository import DriverRepository
from TransportCompany.Entities.Driver import Driver
from TransportCompany.Entities.Accountant import Accountant


class ModelRegistrationWorker:
    @staticmethod
    def CheckPhone(phone):
        return AllRoleRepository().CheckPhone(phone)

    @staticmethod
    def CheckEmail(email):
        return AllRoleRepository().CheckEmail(email)

    @staticmethod
    def RegistrationAccountant(accountant: Accountant):
        AccountantRepository().RegistrationAccountant(accountant)

    @staticmethod
    def RegistrationDriver(driver: Driver):
        DriverRepository().RegistrationDriver(driver)