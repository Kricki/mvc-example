#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import messagebox as tkmessagebox

import gui

__author__ = 'kricki (https://github.com/kricki)'
__version__ = 0.1


class Model:
    def __init__(self):
        self.data1 = 0
        self.data2 = 0
        self.result = 0
        self.operation = 0  # 0: Sum, 1: Difference, 2: Multiply, 3: Division
        self.title = "MVC Template"


class Controller:
    def __init__(self, master=None):
        self._master = master
        self.model = Model()

        # Initialize the view
        self.main_view = gui.MainView(master, self.model)
        self.main_view.main_widgets.btn_calculate.config(command=self.calculate)
        self.main_view.file_menu.filemenu.entryconfig(0, command=self.show_info)
        self.main_view.file_menu.filemenu.entryconfig(1, command=self.show_config)

        self.set_statusbar("")

    def update_model(self):
        self.model.data1 = self.main_view.main_widgets.v_data1.get()
        self.model.data2 = self.main_view.main_widgets.v_data2.get()
        self.model.operation = self.main_view.main_widgets.v_operation.get()

    def calculate(self):
        self.update_model()

        if self.model.operation == 0:  # sum
            self.model.result = self.model.data1 + self.model.data2
        elif self.model.operation == 1:  # substract
            self.model.result = self.model.data1 - self.model.data2
        elif self.model.operation == 2:  # multiply
            self.model.result = self.model.data1 * self.model.data2
        elif self.model.operation == 3:  # divide
            self.model.result = self.model.data1 / self.model.data2
        else:
            raise ValueError("Invalid operation")

        self.update_view()

    def show_config(self):
        """ Display the settings dialog.

        If the user presses "OK", the new settings are updated.
        """
        settings_dialog = gui.SettingsDialog(self._master)
        settings_dialog.operation = self.model.operation
        settings_dialog.show(self._master)

        if not settings_dialog.canceled:
            self.model.operation = settings_dialog.operation
            self.update_view()

    def show_info(self):
        """ Display the info screen
        """
        tkmessagebox.showinfo("Info", "MVC Example v"+str(__version__))

    def set_statusbar(self, text):
        """ Sets the text displayed in the status bar

        :param string text: The text to be displayed.
        """
        self.main_view.main_widgets.v_statusbar.set(text)

    def update_view(self):
        self.main_view.main_widgets.v_operation.set(self.model.operation)
        if self.model.operation == 0:
            self.set_statusbar("Current operation: Sum")
        elif self.model.operation == 1:  # substract
            self.set_statusbar("Current operation: Difference")
        elif self.model.operation == 2:  # multiply
            self.set_statusbar("Current operation: Multiply")
        elif self.model.operation == 3:  # divide
            self.set_statusbar("Current operation: Division")
        else:
            raise ValueError("Invalid operation")

        self.main_view.main_widgets.v_data1.set(self.model.data1)
        self.main_view.main_widgets.v_data2.set(self.model.data2)
        self.main_view.main_widgets.v_result.set(self.model.result)

if __name__ == '__main__':
    root = tk.Tk()
    root.title('MVC Example')
    root.option_add('*tearOff', False)  # see: http://www.tkdocs.com/tutorial/menus.html (for Menubar)

    app = Controller(root)
    root.mainloop()
