# -*- coding: utf-8 -*-
# author: alex markov - agb2019@list.ru
# license: GNU General Public License
################################################
# -- BETA Version --
###################################################
import sys

from PyQt5 import QtWidgets, QtGui, QtCore

import run_control as run

WIDTH = 640  # Ширина
HEIGHT = 480  # Высота


class MainWindow(QtWidgets.QMainWindow):
    """Класс главного меню
    """

    def __init__(self):
        """Функция конструктор (инициализатор) класса основного меню"""
        super().__init__()
        self.setWindowTitle("АлгоритмиК")
        self.resize(WIDTH, HEIGHT)
        self.ico = QtGui.QIcon('images/title_icon.png')
        self.mainMenu()
        self.tab = TabWindow()
        self.setCentralWidget(self.tab)
        self.show()

    def mainMenu(self):
        """Функция главного меню бара приложения"""
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu("Алгоритмы")
        helpMenu = mainMenu.addMenu("Справка")

        binaryAction = QtWidgets.QAction(QtGui.QIcon("images/binary_icon.png"), 'Двоичный поиск', self)
        binaryAction.setShortcut("Alt+1")  # горячие клавиши
        fileMenu.addAction(binaryAction)

        ellipsisAction = QtWidgets.QAction(QtGui.QIcon("images/free_icon.png"), '...', self)
        ellipsisAction.setShortcut("Alt+2")  # горячие клавиши
        fileMenu.addAction(ellipsisAction)
        fileMenu.addSeparator()  # сепаратор в главном меню

        exitAction = QtWidgets.QAction(QtGui.QIcon("images/exit_icon.png"), 'Выход', self)
        exitAction.setShortcut("Alt+F4")  # горячие клавиши
        exitAction.triggered.connect(self.exitWindow)
        fileMenu.addAction(exitAction)

        aboutprogrammAction = QtWidgets.QAction('О программе', self)
        helpMenu.addAction(aboutprogrammAction)
        aboutprogrammAction.triggered.connect(self.aboutProgramm)

        aboutqtAction = QtWidgets.QAction('О библиотеке Qt...', self)
        helpMenu.addAction(aboutqtAction)
        aboutqtAction.triggered.connect(self.aboutQt)

    def aboutProgramm(self):
        QtWidgets.QMessageBox.about(self, "О программе",
                                    "<center>\"АлгоритмиК\" v0.0.1(Beta version)<br><br>"
                                    "Программа для изучения основ применения алгоритмов при программировании на языке Python. "
                                    "Примеры программ и сам программный продукт выполнен с использованием Python 3.6.4 и Qt 5.13.0.<br> "
                                    "<center>Информация о лицензии: GNU General Public License<br><br>"
                                    "(c) Alex Markov 2020 agb2019@list.ru")

    def aboutQt(self):
        """"Функция окна информации о версии программного продукта Qt
        """
        QtWidgets.QMessageBox.aboutQt(window, title="О библиотеке Qt")

    def exitWindow(self):
        """Функция экземпляра класса close() - закрытие окна программы --?
        """
        self.close()


class TabWindow(QtWidgets.QWidget):
    """"Класс окна с вкладками
    """

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        vbox = QtWidgets.QVBoxLayout()
        tab = QtWidgets.QTabWidget()
        tab.addTab(TabBinary(), "&1 Бинарный поиск")

        # для добавления новых возможностей используется класс TabEllipsis()
        tab.addTab(QtWidgets.QLabel("<center>Здесь могут быть другие алгоритмы</center><center>\n"
                                    "Alex Markov</center><center>\nagb2019@list.ru</center>"), "&2 ...")

        vbox.addWidget(tab)
        self.setLayout(vbox)


class TabBinary(QtWidgets.QWidget):
    """Класс окна вкладки "Бинарный поиск"
    """
    valueChanged = QtCore.pyqtSignal(object) # создание нового сигнала для передачи значения дисплея

    def __init__(self):
        super().__init__()

        # Экран числа
        vbox = QtWidgets.QVBoxLayout()  # создаем контейнер
        self.lcdNumber = QtWidgets.QLCDNumber(self)  # создаем электронный индикатор
        self.lcdNumber.setToolTip("Выбранное число")  # всплывающая подсказка
        vbox.addWidget(self.lcdNumber)  # добавляем в вертикальный контейнер
        # Выбор числа
        self.selectNumber = QtWidgets.QSlider(self)  # создаем шкалу с ползунком
        self.selectNumber.setOrientation(QtCore.Qt.Horizontal)  # горизонтальное раcположение шкалы
        self.selectNumber.setToolTip("Выберите число")  # всплывающая подсказка
        self.selectNumber.setTickInterval(1)
        self.selectNumber.setMinimum(0)
        self.selectNumber.setMaximum(99999)
        self.selectNumber.valueChanged.connect(self.lcdNumber.display)  # вызов метода вывода значения на экран
        vbox.addWidget(self.selectNumber)  # добавляем в вертикальный контейнер
        # Кнопка "ВЫПОЛНИТЬ"
        self.pushButton = QtWidgets.QPushButton("&ВЫПОЛНИТЬ")  # создаем кнопку
        self.pushButton.setIcon(QtGui.QIcon("images/binary_icon.png"))  # добавляем иконку
        self.pushButton.setToolTip("Запуск алгоритма")  # всплывающая подсказка
        self.valueChanged.connect(run.RunButton.clickRun) # объект сигнала в модуле run_control (инкапсуляция PyQt5)
        self.pushButton.clicked.connect(self.signal_emited) # вызов функции генерации сигнала
        vbox.addWidget(self.pushButton)  # добавляем в вертикальный контейнер
        # Кнопка "УЗНАТЬ БОЛЬШЕ"
        self.pushButton = QtWidgets.QPushButton("&УЗНАТЬ БОЛЬШЕ")  # создаем кнопку
        self.pushButton.setIcon(QtGui.QIcon("images/questions_icon.png"))  # добавляем иконку
        self.pushButton.setToolTip("Подробнее")  # всплывающая подсказка
        self.pushButton.clicked.connect(run.RunButton.clickMore)
        vbox.addWidget(self.pushButton)  # добавляем в вертикальный контейнер
        # Вывод на экран
        self.setLayout(vbox)  # передача ссылки родителю

    def signal_emited(self):
        """"Функция генерации сигнала
        """
        self.valueChanged.emit(self) # генерация сигнала


# Класс для добавления новых возможностей
class TabEllipsis(QtWidgets.QWidget):
    """Класс окна вкладки "..."
    """

    def __init__(self):
        super().__init__()


# Тестирование:
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.move(window.width() * -2, 0)  # расположение точно по центру экрана
    window.setWindowIcon(window.ico)  # значок для окна
    # window.show()
    desktop = QtWidgets.QApplication.desktop()  # расположение точно по центру экрана
    x = (desktop.width() - window.frameSize().width()) // 2  # расположение точно по центру экрана
    y = (desktop.height() - window.frameSize().height()) // 2  # расположение точно по центру экрана
    window.move(x, y)  # расположение точно по центру экрана
    sys.exit(app.exec())
