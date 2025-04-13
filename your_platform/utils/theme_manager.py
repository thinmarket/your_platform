# trading_platform/utils/theme_manager.py
from PyQt5.QtCore import QObject, pyqtSignal
from enum import Enum
import os

class Theme(Enum):
    LIGHT = "light"
    DARK = "dark"

class ThemeManager(QObject):
    themeChanged = pyqtSignal(Theme)  # Сигнал для оповещения о смене темы

    def __init__(self):
        super().__init__()
        self.current_theme = Theme.LIGHT
        self._load_styles()

    def _load_styles(self):
        """Загрузка файлов стилей"""
        base_path = os.path.join(os.path.dirname(__file__), '../resources/styles')
        self.styles = {
            Theme.LIGHT: self._read_style_file(os.path.join(base_path, "light/main.qss")),
            Theme.DARK: self._read_style_file(os.path.join(base_path, "dark/main.qss"))
        }

    def _read_style_file(self, path):
        """Чтение файла стилей"""
        with open(path, "r") as file:
            return file.read()

    def toggle_theme(self):
        """Переключение между темами"""
        self.current_theme = Theme.DARK if self.current_theme == Theme.LIGHT else Theme.LIGHT
        self.themeChanged.emit(self.current_theme)

    def get_current_style(self):
        """Получение текущего стиля"""
        return self.styles[self.current_theme]