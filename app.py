import tkinter as tk
from habitlist import HabitList
from habit import Habit
import pickle
from datetime import datetime
from datetime import date


class App:

    def __init__(self):
        self.habit_list = []

        self.main_window = tk.Tk()
        posx = int(self.main_window.winfo_screenwidth() / 2 - 307)
        posy = int(self.main_window.winfo_screenheight() / 2 - 250)
        self.main_window.geometry('420x500+{}+{}'.format(posx, posy))
        self.main_window.title('Daily Habit Tracker')
        self.main_window.configure(bg='#a4b0be')
        self.main_window.resizable(False, False)

        self.openTime = datetime.date(datetime.now())
        self.lastClosed = ''

    def run(self):

        # creating the habits list
        habits = HabitList(self.main_window, self.habit_list)
        habits.prephabits()

        tk.mainloop()

        self.habit_list = habits.habits

    # writes habits to a json file and makes note of time
    def save(self):
        data_lists = []

        # discards all habits that were previously deleted
        for habit in self.habit_list:
            if not habit.isRemoved:
                data = {
                    'name': str(habit.name),
                    'streak': int(habit.streak),
                    'isComplete': bool(habit.isComplete.get())
                }
                data_lists.append(data)
            # check to see if the date changed while app was running
            if self.openTime != datetime.date(datetime.now()):
                if habit.isComplete.get():
                        habit.streak += 1
                else:
                    habit.streak = 0
                habit.isComplete.set(False)

        pickle.dump(data_lists, open('user_data.p', 'wb'))

        # record the time that the app closed
        closed_date = datetime.date(datetime.now())
        save_file = open('timelog.txt', 'w')
        save_file.truncate(0)
        save_file.write(closed_date)

    # loads saved habit data and last operation data
    def load(self):
        # update las closed date
        try:
            time_file = open('timelog.txt', 'r')
            self.lastClosed = time_file.readline()
        except FileNotFoundError:
            self.lastClosed = datetime.date(datetime.now())
        # get the saved habits
        try:
            data_lists = pickle.load(open('user_data.p', 'rb'))
            for data in data_lists:
                habit = Habit(data['name'], data['streak'],
                                data['isComplete'], self.main_window)
                # if date has changed to some point in the future, revert the habit to incomplete state
                if self.lastClosed != self.openTime:
                    if habit.isComplete.get():
                        habit.streak += 1
                    else:
                        habit.streak = 0
                    habit.isComplete.set(False)
                        
                self.habit_list.append(habit)
        except FileNotFoundError:
            self.habit_list = []
