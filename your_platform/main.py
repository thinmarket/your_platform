import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QMenuBar
from utils.theme_manager import ThemeManager

class MainWindow(QMainWindow):
    def __init__(self, theme_manager):
        super().__init__()
        self.theme_manager = theme_manager
        self.setWindowTitle("Your Platform")
        self.setGeometry(100, 100, 800, 600)
        self.setStyleSheet(self.theme_manager.get_current_style())

        # Подключение сигнала смены темы
        self.theme_manager.themeChanged.connect(self.update_theme)

        # Создание меню
        self.create_menu()

    def create_menu(self):
        # Создание меню
        menu_bar = self.menuBar()
        view_menu = menu_bar.addMenu("Вид")

        # Пункт меню для переключения тем
        toggle_theme_action = QAction("Переключить тему", self)
        toggle_theme_action.triggered.connect(self.theme_manager.toggle_theme)
        view_menu.addAction(toggle_theme_action)

    def update_theme(self, theme):
        self.setStyleSheet(self.theme_manager.get_current_style())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    theme_manager = ThemeManager()
    window = MainWindow(theme_manager)
    window.show()
    sys.exit(app.exec_())