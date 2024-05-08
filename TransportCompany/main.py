from Controller.ControllerLogin import ControllerLogin
from Controller.ControllerRegistration import ControllerRegister


def main():
    app = ControllerLogin()
    app.RunViewLogin()
    app.StartProgram()

    # app = ControllerRegister()
    # app.RunViewRegister()


if __name__ == "__main__":
    main()