from src.views.login_view import LoginView
from src.controllers.dashboard_controller import DashboardController

class LoginController:
    def __init__(self):
        self.view = LoginView(self) # El controlador crea su vista

    def ejecutar(self):
        self.view.mainloop()

    def intentar_login(self):
        usuario = self.view.user_entry.get()
        password = self.view.pass_entry.get()

        # Aquí iría la consulta a la base de datos más adelante
        if usuario == "admin" and password == "1234":
            print("¡Login Exitoso!")
            self.abrir_dashboard()
        else:
            self.view.error_label.configure(text="Credenciales incorrectas")
            
    def abrir_dashboard(self):
        # En lugar de destruir la ventana, la ocultamos primero
        self.view.withdraw() 
        
        # Abrimos el dashboard
        dashboard = DashboardController()
        dashboard.ejecutar()
        
        # Al final, si quieres, destruyes la anterior
        self.view.quit()
 