import tkinter as tk
from popup import Popup


class Task:

    def __init__(self, name, streak, isGoal, isComplete, parent):
        self.name = name
        self.name_var = tk.StringVar(value=name)
        self.isGoal = isGoal
        self.streak = streak
        self.isComplete = tk.BooleanVar(value=isComplete)
        self.isRemoved = False
        self.parent = parent

        # setting gui elements to None for now
        self.fr_body = None
        self.cb_done = None
        self.lbl_name = None
        self.btn_edit = None
        self.lbl_streak = None
        self.btn_delete = None

    # adds all of the elements to the gui
    # kept seperate because of the need to save and load data
    def display(self, numr):
        sepx = 10
        sepy = 10
        numc = 0

        if not self.isGoal:
            numc = 1

        # holds all of the widgets of a task
        self.fr_body = tk.Frame(self.parent)
        self.fr_body.grid(row=numr, column=numc, padx=5, pady=(25, 0), ipady=5)

        # recieves user input to decide if task is complete or not
        self.cb_done = tk.Checkbutton(
            self.fr_body, onvalue=True, offvalue=False, variable=self.isComplete, command=self.taskCompleted)
        self.cb_done.grid(row=0, column=0, padx=(0, sepx), pady=(sepy, 0))

        # displays the name of the task
        self.lbl_name = tk.Label(
            self.fr_body, textvariable=self.name_var, font=('Helvetica', 11), width=10)
        self.lbl_name.grid(row=0, column=1, padx=(0, sepx), pady=(sepy, 0))
        name = self.name
        if len(name) > 13:
            name = name[0:10] + '...'
        self.name_var.set(name)

        # displays the task's streak
        self.lbl_streak = tk.Label(self.fr_body, text='s: ' + str(
            self.streak), font=('Helvetica', 11), width=5)
        self.lbl_streak.grid(row=0, column=2, padx=(0, sepx), pady=(sepy, 0))

        # used to edit the name of the task
        self.btn_edit = tk.Button(self.fr_body, text='E', command=self.editName, font=(
            'Helvetica', 11), bd=0, highlightthickness=0, width=3)
        self.btn_edit.grid(row=0, column=3, padx=(0, sepx), pady=(sepy, 0))

        # deletes the task
        self.btn_delete = tk.Button(self.fr_body, text='D', command=self.deleteTask, font=(
            'Helvetica', 11), bd=0, highlightthickness=0, width=3)
        self.btn_delete.grid(row=0, column=4, pady=(sepy, 0), padx=(0, sepx))

        self.configureColors()

    # edits the name of the task
    def editName(self):
        popup = Popup(self.parent, self.isGoal)
        popup.promptUser(False)
        self.parent.wait_window(popup.window)

        if popup.isValid:
            self.name = popup.input.get()
            self.name_var.set(self.name)
            name = self.name
            if len(name) > 13:
                name = name[0:10] + '...'
            self.name_var.set(name)

    # deletes a task from the list
    def deleteTask(self):
        self.fr_body.destroy()
        self.isRemoved = True

    def taskCompleted(self):
        self.configureColors()
        # self.streak += 1
        # add functionality to where streak updates as soon as you click the checkbutton
    
    # used to set the colors of the tasks depending on if they were completed or not
    def configureColors(self):
        widgets = [self.fr_body, self.cb_done,
                   self.lbl_name, self.lbl_name, self.lbl_streak]

        # case the task is completed and the original color scheme is not wanted
        if self.isComplete.get():
            for widget in widgets:
                try:
                    widget.configure(bg='#dcdde1', fg='#718093')
                except:
                       widget.configure(bg='#dcdde1')
        else:
            for widget in widgets:
                if self.isGoal:
                    try:
                        widget.configure(bg='#00b894', fg='white')
                    except:
                        widget.configure(bg='#00b894')
                else:
                    try:
                        widget.configure(bg='#0984e3', fg='white')
                    except:
                        widget.configure(bg='#0984e3')
