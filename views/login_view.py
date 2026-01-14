import customtkinter as ctk

class LoginView(ctk.CTk):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller  # Guardamos referencia al controlador
        
        self.title("CrediFast - Iniciar Sesión")
        self.geometry("854x480")
        self.configure(fg_color="#D9B2A9")
        self.resizable(False, False)

        # Card de Login
        self.login_card = ctk.CTkFrame(self, width=380, height=400, fg_color="white", corner_radius=30)
        self.login_card.place(relx=0.5, rely=0.5, anchor="center")

        # Título
        ctk.CTkLabel(self.login_card, text="CrediFast", text_color="#1C2621",
                     font=ctk.CTkFont(family="Segoe UI", size=34, weight="bold")).place(relx=0.5, rely=0.15, anchor="center")

        # Inputs
        self.user_entry = ctk.CTkEntry(self.login_card, width=280, height=50, placeholder_text="Usuario",
                                       fg_color="#F4F6F5", border_color="#E2E8E6", corner_radius=12)
        self.user_entry.place(relx=0.5, rely=0.45, anchor="center")

        self.pass_entry = ctk.CTkEntry(self.login_card, width=280, height=50, placeholder_text="Contraseña", 
                                       show="*", fg_color="#F4F6F5", border_color="#E2E8E6", corner_radius=12)
        self.pass_entry.place(relx=0.5, rely=0.6, anchor="center")

        # Botón (llama a una función del controlador)
        self.login_button = ctk.CTkButton(self.login_card, text="INICIAR SESIÓN", width=280, height=55, 
                                          fg_color="#D97652", hover_color="#b35d3d", corner_radius=14,
                                          font=ctk.CTkFont(size=15, weight="bold"),
                                          command=self.controller.intentar_login)
        self.login_button.place(relx=0.5, rely=0.8, anchor="center")

        # Mensaje de error
        self.error_label = ctk.CTkLabel(self.login_card, text="", text_color="#D97652", font=("Segoe UI", 12, "bold"))
        self.error_label.place(relx=0.5, rely=0.7, anchor="center")