import tkinter as tk


class Popup:

    def __init__(self, root, isGoal):
        self.root = root
        self.input = tk.StringVar()
        self.isValid = False
        self.isGoal = isGoal

        self.window = tk.Toplevel(self.root)

        # prompts user
        self.lbl_prompt = tk.Label(self.window)
        self.lbl_prompt.grid(row=0, column=0)

        # accepts user input
        self.ent_name = tk.Entry(self.window, textvariable=self.input)
        self.ent_name.grid(row=1, column=0)
        self.ent_name.focus()

        self.btn_confirm = tk.Button(self.window, command=self.quit)
        self.btn_confirm.grid(row=2, column=0)

        # allows the popup to take priority over the main window
        self.window.transient(self.root)
        self.window.grab_set()

    # popup window configured to ask user to add a new task
    def createPrompt(self):
        if self.isGoal:
            self.window.title('Create a new goal')
        else:
            self.window.title('Create a new habit')

        self.lbl_prompt.configure(text='Enter a name: ')
        self.btn_confirm.configure(text='Create')

    # popup window configured to ask user to edit existing task
    def editPrompt(self):

        if self.isGoal:
            self.window.title('New goal name')
        else:
            self.window.title('New habit name')

        self.lbl_prompt.configure(text='Enter a new name: ')

        self.btn_confirm.configure(text='Change')

    # exits out of the popup if input has been recieved
    def quit(self):
        str_input = self.input.get()

        if str_input.isspace() or len(str_input) == 0:
            self.lbl_prompt.configure(text='Please enter a name: ')

        elif str_input[0:1].isspace():
            self.lbl_prompt.configure(
                text='Oops, looks like your name has a space before it.\nPlease enter it again: ')

        else:
            self.isValid = True
            self.window.destroy()
