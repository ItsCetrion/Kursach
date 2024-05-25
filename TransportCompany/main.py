from Controller.ControllerLogin import ControllerLogin
from Controller.Admin.ControllerWindowApplication import ControllerWindowApplication
from Controller.Client.ControllerRequestSubmission import ControllerRequestSubmission
from Controller.Client.ControllerApplicationWindow import ControllerApplicationWindow
from Entities.Client import Client


def main(client):
    # app = ControllerLogin()
    # app.RunViewLogin()
    # app.StartProgram()

    app = ControllerWindowApplication()
    app.RunViewWindowApplication()

    # app = ControllerRequestSubmission(client)
    # app.RunViewRequestSubmission()

    # app = ControllerApplicationWindow(1)
    # app.RunViewApplicationWindow()


if __name__ == "__main__":
    client = Client()
    # client.Id = 1
    # client.FirstName = "Иван"
    # client.LastName = "Иванов"
    # client.Email = "test@mail.ru"
    # client.NumberPhone = "79951622900"
    main(client)
    # a = set([3,4]).intersection([1,3,4])
    # print(a)
