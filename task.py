import tkinter as tk

class Task:

    def __init__(self, name, parent, isGoal):
        self.name = name
        self.isGoal = isGoal
        self.streak = 0
        self.isComplete = tk.BooleanVar(value = False)
        
        # holds all of the widgets of a task
        self.fr_body = tk.Frame(parent)
        self.fr_body.pack(pady = (5, 0))

        # recieves user input to decide if task is complete or not
        self.cb_done = tk.Checkbutton(self.fr_body, onvalue = True, offvalue = False, variable = self.isComplete)
        self.cb_done.grid(row = 0, column = 0)
        
        # displays the name of the task
        self.lbl_name = tk.Label(self.fr_body, textvariable = self.name)
        self.lbl_name.grid(row = 0, column = 1) 

        # used to edit the name of the task
        self.btn_edit = tk.Button(self.fr_body, text = 'E')
        self.btn_edit.grid(row = 0, column = 2)

        # deletes the task
        self.btn_delete = tk.Button(self.fr_body, text = 'D')
        self.btn_delete.grid(row = 0, column = 3) 

