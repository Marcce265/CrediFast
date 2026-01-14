import customtkinter as ctk

class DashboardView(ctk.CTk):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        
        self.title("CrediFast - Sistema de Préstamos")
        self.geometry("960x540")
        self.configure(fg_color="#F2F2F2") # Fondo gris muy claro para el centro

        # --- BARRA LATERAL (SIDEBAR) ---
        self.sidebar = ctk.CTkFrame(self, width=220, corner_radius=0, fg_color="#D97652")
        self.sidebar.pack(side="left", fill="y")

        # Título en Sidebar
        self.logo = ctk.CTkLabel(self.sidebar, text="CrediFast 💸", 
                                 font=ctk.CTkFont(size=24, weight="bold"), text_color="white")
        self.logo.pack(pady=40, padx=20)

        # Botones del Menú
        self.btn_inicio = self.crear_boton_menu("🏠  Inicio")
        self.btn_clientes = self.crear_boton_menu("👥  Clientes")
        self.btn_prestamos = self.crear_boton_menu("💰  Préstamos")
        
        # Espaciador para empujar el botón de cerrar sesión abajo
        self.spacer = ctk.CTkLabel(self.sidebar, text="")
        self.spacer.pack(expand=True, fill="both")

        self.btn_logout = self.crear_boton_menu("🚪  Cerrar Sesión")
        self.btn_logout.configure(hover_color="#b35d3d")

    def crear_boton_menu(self, texto):
        btn = ctk.CTkButton(self.sidebar, text=texto, corner_radius=0, height=45,
                            fg_color="transparent", anchor="w", 
                            font=ctk.CTkFont(size=14), text_color="white",
                            hover_color="rgba(255, 255, 255, 0.1)")
        btn.pack(fill="x", padx=10, pady=5)
        return btn

        # --- CONTENIDO CENTRAL ---
        self.container = ctk.CTkFrame(self, fg_color="transparent")
        self.container.pack(side="right", expand=True, fill="both", padx=40, pady=40)

        self.title_label = ctk.CTkLabel(self.container, text="Panel de Control", 
                                        font=ctk.CTkFont(size=32, weight="bold"), text_color="#1C2621")
        self.title_label.pack(anchor="w")

        self.sub_label = ctk.CTkLabel(self.container, text="Bienvenido al sistema de CrediFast admin.", 
                                      font=ctk.CTkFont(size=16), text_color="#7F8C8D")
        self.sub_label.pack(anchor="w", pady=(5, 20))