# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import ttk

import tkadd

__author__ = 'kricki (https://github.com/kricki)'


class MainWidgets(ttk.Frame):
    def __init__(self, master=None, model=None):
        ttk.Frame.__init__(self, master)

        # Entries for the data and a label for the result
        self.v_data1 = tk.DoubleVar()
        self.v_data2 = tk.DoubleVar()
        self.v_result = tk.DoubleVar()
        self.v_data1.set(model.data1)
        self.v_data2.set(model.data2)
        self.v_result.set(model.result)

        self.entry_data1 = ttk.Entry(self, width=10, textvariable=self.v_data1)
        self.entry_data2 = ttk.Entry(self, width=10, textvariable=self.v_data2)
        self.label_result = ttk.Label(self, width=10, textvariable=self.v_result)

        # Place the objects using grid
        self.entry_data1.grid(row=0, column=0)
        self.entry_data2.grid(row=0, column=1)
        self.label_result.grid(row=0, column=2)

        # RadioButtons as selector for the operation
        self.v_operation = tk.IntVar()
        self.v_operation.set(model.operation)
        self.rb_operation = [None]*4
        self.rb_operation[0] = ttk.Radiobutton(self, text='Sum', variable=self.v_operation, value=0)
        self.rb_operation[1] = ttk.Radiobutton(self, text='Difference', variable=self.v_operation, value=1)
        self.rb_operation[2] = ttk.Radiobutton(self, text='Multiply', variable=self.v_operation, value=2)
        self.rb_operation[3] = ttk.Radiobutton(self, text='Division', variable=self.v_operation, value=3)

        self.rb_operation[0].grid(row=3, column=0, sticky='EW')
        self.rb_operation[1].grid(row=4, column=0, sticky='EW')
        self.rb_operation[2].grid(row=5, column=0, sticky='EW')
        self.rb_operation[3].grid(row=6, column=0, sticky='EW')

        # "Calculate" button
        self.btn_calculate = ttk.Button(self, text='Calc!')
        self.btn_calculate.grid(row=7, column=0)

        # Status bar
        ttk.Separator(master, orient=tk.HORIZONTAL).grid(row=15, columnspan=10, sticky='EW')
        self.v_statusbar = tk.StringVar()
        self.label_statusbar = ttk.Label(self, textvariable=self.v_statusbar)
        self.label_statusbar.grid(row=17, column=0, columnspan=2, sticky='W')


class FileMenu(ttk.Frame):
    def __init__(self, master=None):
        ttk.Frame.__init__(self, master)

        self.menubar = tk.Menu(self)

        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Info...")
        self.filemenu.add_command(label="Settings...")
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Quit", command=self.quit)
        self.menubar.add_cascade(label="File", menu=self.filemenu)

        self.master.config(menu=self.menubar)


class MainView(ttk.Frame):
    def __init__(self, master=None, model=None):
        """ Create GUI
        """
        ttk.Frame.__init__(self, master)

        self.file_menu = FileMenu(master)

        self.main_widgets = MainWidgets(master, model)
        self.main_widgets.grid()


class SettingsDialog(tkadd.Dialog):
    """ The settings dialog

    """
    def __init__(self, master):
        self.operation = None
        self.v_operation = tk.IntVar()
        self.rb_operation = [None]*4

        super().__init__(master, "Settings")

    def body(self, master):

        # RadioButtons as selector for the operation
        self.v_operation.set(self.operation)
        self.rb_operation[0] = ttk.Radiobutton(master, text='Sum', variable=self.v_operation, value=0)
        self.rb_operation[1] = ttk.Radiobutton(master, text='Difference', variable=self.v_operation, value=1)
        self.rb_operation[2] = ttk.Radiobutton(master, text='Multiply', variable=self.v_operation, value=2)
        self.rb_operation[3] = ttk.Radiobutton(master, text='Division', variable=self.v_operation, value=3)

        self.rb_operation[0].grid(row=0, column=0, sticky='EW')
        self.rb_operation[1].grid(row=1, column=0, sticky='EW')
        self.rb_operation[2].grid(row=2, column=0, sticky='EW')
        self.rb_operation[3].grid(row=3, column=0, sticky='EW')

        return self.rb_operation[0]  # initial focus

    def apply(self):
        self.operation = self.v_operation.get()
