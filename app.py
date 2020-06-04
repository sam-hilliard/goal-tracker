import tkinter as tk
from tasklist import TaskList

class App:

    def __init__(self):
        window = tk.Tk()
        window.geometry('600x500')
        window.title('Daily Goal and Habit Tracker')

        goals = TaskList(window, True)
        habits = TaskList(window, False)


        tk.mainloop()

    # writes tasks to a json file
    def save(self):
        print('saving...')

    #loads a json file containing saved data
    def load(self):
        print('loading...')