from Controller.ControllerLogin import ControllerLogin


def main():
    app = ControllerLogin()
    app.RunViewLogin()
    app.StartProgram()


if __name__ == "__main__":
    main()