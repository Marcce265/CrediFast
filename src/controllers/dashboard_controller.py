from src.views.dashboard_view import DashboardView

class DashboardController:
    def __init__(self):
        self.view = DashboardView(self)
        
    def ejecutar(self):
        self.view.mainloop()