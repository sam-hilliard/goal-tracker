# tasklist.py

import tkinter as tk

class TaskList:

    def __init__(self, parent, isGoalSide):
        self.tasks = []

        body = tk.Frame(parent, bg = '#a4b0be')
        if isGoalSide:
            body.pack(side = 'left', fill = 'both', expand = True)
        else:
            body.pack(side = 'right', fill = 'both', expand = True)

        header = tk.Frame(body)
        header.pack(fill = 'x')

        title = tk.Label(header, text = 'List', font = ('Helvetica', 15), width = 10, fg = 'white')
        title.grid(row = 0, column = 0, pady = 5)
        if isGoalSide:
            header.configure(bg = '#55efc4')
            title.configure(text = 'Goals', bg = '#55efc4')
        else:
            header.configure(bg = '#74b9ff')
            title.configure(text = 'Habits', bg = '#74b9ff')

        btn_add = tk.Button(header, text = '+')
        btn_add.grid(row = 0, column = 1, pady = 5)

    def addTask(self):
        print('task added')
        

        