# habitlist.py

import tkinter as tk
from tkinter import ttk
from habit import Habit
from popup import Popup


class HabitList:

    def __init__(self, window, habits):
        self.habits = habits
        self.window = window

        # frame to hold the title of the list and a button to add more habits
        self.fr_header = tk.Frame(self.window, bg='#74b9ff')
        self.fr_header.grid(row=0, column=0, sticky='nsew')
        
        # used to contain the canvas and the scrollbar
        self.fr_body = tk.Frame(self.window, bg='#a4b0be')
        self.fr_body.grid(row=1, column=0, sticky='nsew')

        # scrollable canvas to hold the list
        self.scroll_canvas = tk.Canvas(self.fr_body, width=353, height= 415, bg='#a4b0be', highlightthickness=0)
        self.scroll_canvas.grid(row=0, column=0, sticky='nsew', padx=25, pady=(25,0))
        
        # scrollbar to control the view of the canvas
        self.scrollbar = ttk.Scrollbar(self.fr_body, orient='vertical', command=self.scroll_canvas.yview)
        self.scrollbar.grid(row=0, column=1, sticky='nsew')

        # creates the main container frame for the list
        self.fr_list = tk.Frame(self.scroll_canvas, bg='#a4b0be')
        self.fr_list.bind(
            '<Configure>',
            lambda e: self.scroll_canvas.configure(
                scrollregion=self.scroll_canvas.bbox('all')
            )
        )
        self.scroll_canvas.create_window((0,0), window=self.fr_list, anchor='nw')
        self.scroll_canvas.configure(yscrollcommand=self.scrollbar.set)

        # label used to identify the type of the list
        title = tk.Label(self.fr_header, text='Habits', font=(
            'Helvetica', 15), width=25, fg='white', bg='#74b9ff')
        title.grid(row=0, column=0, pady=15, padx=(30, 0))

        # adds a habit to the habit list
        self.btn_add = tk.Button(
            self.fr_header, text='+', command=lambda: self.addHabit(), font=(
                'Helvetica', 11), bd=0, highlightthickness=0, width=5)
        self.btn_add.grid(row=0, column=1, pady=15, padx=(0, 60))

    # displays habits to the gui with the appropriate window
    def prephabits(self):
        for habit in self.habits:
            habit.parent = self.fr_list
            habit.display()

    # adds a habit graphically to a list as well as adds a habit object to the habits
    def addHabit(self):
        popup = Popup(self.window)
        popup.promptUser(True)
        self.window.wait_window(popup.window)

        if popup.isValid:
            name = popup.input.get()
            habit = Habit(name, 0, False, self.fr_list)
            self.habits.append(habit)
            habit.display()
