from TransportCompany.Repositories.AllRoleRepository import AllRoleRepository
from TransportCompany.Repositories.AccountantRepository import AccountantRepository
from TransportCompany.Repositories.DriverRepository import DriverRepository
from TransportCompany.Entities.Driver import Driver
from TransportCompany.Entities.Accountant import Accountant

class ModelRegistrationWorker:

    def CheckPhone(self, phone):
        return AllRoleRepository().CheckPhone(phone)

    def CheckEmail(self, email):
        return AllRoleRepository().CheckEmail(email)

    def RegistrationAccountant(self, accountant: Accountant):
        AccountantRepository().RegistrationAccountant(accountant)

    def RegistrationDriver(self, driver: Driver):
        DriverRepository().RegistrationDriver(driver)