import tkinter as tk


class Popup:

    def __init__(self, root, isGoal):
        self.root = root
        self.input = tk.StringVar()
        self.isValid = False
        self.isGoal = isGoal
        self.window = tk.Toplevel(self.root)

        # set the position of the popup to the middle of the window
        self.root.update_idletasks()
        rootx = self.root.winfo_rootx()
        rooty = self.root.winfo_rooty()
        posx = int(rootx + self.root.winfo_width() / 2 - 125)
        posy = int(rooty + self.root.winfo_height() / 2 - 200)
        self.window.geometry('225x125+{}+{}'.format(posx, posy))
        self.window.resizable(False, False)

        sepx = 50
        sepy = 10
        # prompts user
        self.lbl_prompt = tk.Label(self.window)
        self.lbl_prompt.grid(row=0, column=0, padx=sepx, pady=sepy)

        # accepts user input
        self.ent_name = tk.Entry(self.window, textvariable=self.input, width = 20)
        self.ent_name.grid(row=1, column=0, padx=sepx, pady=sepy)
        self.ent_name.focus()

        self.btn_confirm = tk.Button(self.window, command=self.quit, font=(
            'Helvetica', 11), bd=0, highlightthickness=0)
        self.btn_confirm.grid(row=2, column=0, padx=sepx, pady=sepy)

        # allows the popup to take priority over the main window
        self.window.transient(self.root)
        self.window.grab_set()

    # popup window configured to ask the user for task input
    def promptUser(self, isCreate):

        # configure text
        if isCreate:
            self.lbl_prompt.configure(text='Enter a name: ')
            self.btn_confirm.configure(text='Create')
        else:
            self.lbl_prompt.configure(text='Enter a new name: ')
            self.btn_confirm.configure(text='Change')

        # configure the color scheme and prompts
        if self.isGoal:
            if isCreate:
                self.window.title('Create a new goal')
            else:
                self.window.title('New goal name')
            self.window.configure(bg='#00b894')
            self.lbl_prompt.configure(bg='#00b894')
        else:
            if isCreate:
                self.window.title('Create a new goal')
            else:
                self.window.title('New habit name')
            self.window.configure(bg='#0984e3')
            self.lbl_prompt.configure(bg='#0984e3')

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
