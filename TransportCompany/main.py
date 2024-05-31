from Controller.ControllerLogin import ControllerLogin
from Controller.Admin.ControllerWindowApplication import ControllerWindowApplication


def main():
    app = ControllerLogin()
    app.RunViewLogin()
    app.StartProgram()

    # app = ControllerWindowApplication()
    # app.RunViewWindowApplication()


if __name__ == "__main__":
    main()