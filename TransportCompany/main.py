from Controller.ControllerLogin import ControllerLogin
from Controller.Admin.ControllerWindowApplication import ControllerWindowApplication
from Controller.Client.ControllerRequestSubmission import ControllerRequestSubmission
from Entities.Request import Request


def main():
    # app = ControllerLogin()
    # app.RunViewLogin()
    # app.StartProgram()

    app = ControllerWindowApplication()
    app.RunViewWindowApplication()

    # app = ControllerRequestSubmission()
    # app.RunViewRequestSubmission()


if __name__ == "__main__":
    main()
    # t = False
    # print(t is False)
