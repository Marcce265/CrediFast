from controllers.login_controller import LoginController

def main():
    # Iniciamos el controlador del login
    app = LoginController()
    app.ejecutar()

if __name__ == "__main__":
    main()