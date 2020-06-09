import tkinter as tk
from tasklist import TaskList
from task import Task
import pickle
from datetime import datetime
from datetime import date


class App:

    def __init__(self):
        self.task_lists = [[], []]
        self.main_window = tk.Tk()
        self.main_window.geometry('600x500')
        self.main_window.title('Daily Goal and Habit Tracker')
        self.lastClosed = ''
        self.openTime = datetime.now().strftime('%H:%M:%S')

    def run(self):

        # creating the goals list
        goals = TaskList(self.main_window, self.task_lists[0], True)
        goals.prepTasks()

        # creating the habits list
        habits = TaskList(self.main_window, self.task_lists[1], False)
        habits.prepTasks()

        tk.mainloop()

        self.task_lists = [goals.tasks, habits.tasks]

    # writes tasks to a json file and makes note of time
    def save(self):
        data_lists = [[], []]

        # discards all tasks that were previously deleted
        for i in range(len(self.task_lists)):
            for task in self.task_lists[i]:
                if not task.isRemoved:
                    data = {
                        'name': str(task.name.get()),
                        'streak': int(task.streak),
                        'isGoal': bool(task.isGoal),
                        'isComplete': bool(task.isComplete.get())
                    }
                    data_lists[i].append(data)

        pickle.dump(data_lists, open('user_data.p', 'wb'))

        # record the time that the app closed
        closed_date = date.today().strftime('%d/%m/%Y')
        save_file = open('timelog.txt', 'w')
        save_file.truncate(0)
        save_file.write(closed_date)
    
    # loads saved task data and last operation data
    def load(self):
        # update las closed date
        time_file = open('timelog.txt', 'r')
        self.lastClosed = time_file.readline()
        # get the saved tasks
        try:
            data_lists = pickle.load(open('user_data.p', 'rb'))
            for i in range(len(data_lists)):
                for data in data_lists[i]:
                    task = Task(data['name'], data['streak'],
                                data['isGoal'], data['isComplete'], self.main_window)

                    # if date has changed to some point in the future, revert the task to incomplete state
                    if self.lastClosed != datetime.date.today().strftime('%d/%m/%Y'):
                        task.configureColors(True)
                        task.isComplete.set(False)
                    self.task_lists[i].append(task)
        except FileNotFoundError:
            self.task_lists = [[], []]
