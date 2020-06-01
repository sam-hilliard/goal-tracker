#task.py

class Task:

    def __init__(self, name, isGoal):
        self.name = name
        self.isGoal = isGoal
        self.streak = 0
        self.isComplete = False