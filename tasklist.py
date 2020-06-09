# tasklist.py

import tkinter as tk
from task import Task
from popup import Popup


class TaskList:

    def __init__(self, parent, tasks, isGoalSide):
        self.tasks = tasks
        self.isGoalSide = isGoalSide
        self.parent = parent

        # creates the main container frame for the list
        self.fr_body = tk.Frame(parent, bg='#a4b0be')
        if isGoalSide:
            self.fr_body.pack(side='left', fill='both', expand=True)
        else:
            self.fr_body.pack(side='right', fill='both', expand=True)

        # frame to hold the title of the list and a button to add more tasks
        self.fr_header = tk.Frame(self.fr_body)
        self.fr_header.pack(fill='x')

        # label used to identify the type of the list
        title = tk.Label(self.fr_header, text='List', font=(
            'Helvetica', 15), width=10, fg='white')
        title.grid(row=0, column=0, pady=5)
        if self.isGoalSide:
            self.fr_header.configure(bg='#55efc4')
            title.configure(text='Goals', bg='#55efc4')
        else:
            self.fr_header.configure(bg='#74b9ff')
            title.configure(text='Habits', bg='#74b9ff')

        # adds a task to the task list
        self.btn_add = tk.Button(
            self.fr_header, text='+', command=lambda: self.addTask())
        self.btn_add.grid(row=0, column=1, pady=5)

    # displays tasks to the gui with the appropriate parent
    def prepTasks(self):
        for task in self.tasks:
            task.parent = self.fr_body
            task.display()

    # adds a task graphically to a list as well as adds a task object to the tasks
    def addTask(self):
        popup = Popup(self.parent, self.isGoalSide)
        popup.createPrompt()
        self.parent.wait_window(popup.window)

        if popup.isValid:
            name = popup.input.get()
            task = Task(name, 0, self.isGoalSide, False, self.fr_body)
            self.tasks.append(task)
            task.display()
