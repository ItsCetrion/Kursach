from Repositories.AllRoleRepository import AllRoleRepository
from Repositories.AccountantRepository import AccountantRepository
from Repositories.DriverRepository import DriverRepository
from Entities.Driver import Driver
from Entities.Accountant import Accountant


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