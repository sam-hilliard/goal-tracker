import tkinter as tk

class Popup:

    def __init__(self, root, isGoal):
        self.input = tk.StringVar()
        self.isValid = False
        window = tk.Toplevel(root)

        if isGoal:
            window.title('Create a new goal')
        else:
            window.title('Create a new habit')
        
        self.lbl_prompt = tk.Label(window, text = 'Enter a name: ')
        self.lbl_prompt.grid(row = 0, column = 0)

        self.ent_name = tk.Entry(window, textvariable = self.input)
        self.ent_name.grid(row = 1, column = 0)

        self.btn_create = tk.Button(window, text = 'Create', command = lambda: self.quit(window))
        self.btn_create.grid(row = 2, column = 0)

        window.transient(root)
        window.grab_set()
        root.wait_window(window)

    # exits out of the popup if input has been recieved
    def quit(self, window):
        str_input = self.input.get()

        if str_input.isspace() or len(str_input) == 0:
            self.lbl_prompt.configure(text = 'Please enter a name: ')

        elif str_input[0:1].isspace():
            self.lbl_prompt.configure(text = 'Oops, looks like your name has a space before it. Please enter it again: ')

        else:
            # isn't true for some reason...
            self.isValid = True   
            window.destroy()