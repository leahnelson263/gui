import tkinter
import tkinter.messagebox


class MyGUI:
    def __init__(self):
        #create the main window widget and assign it to the variable 'main window'.
        self.main_window = tkinter.Tk()

        #configure the main window
        self.main_window.geometry('500x200')
        self.main_window.title('Label Demo')

        #create two frames, one for the top of the
        #window, and one for the bottom
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # create three IntVar objects to use with
        # the Checkbuttons.

        self.cb_var1 = tkinter.IntVar()
        self.cb_var2 = tkinter.IntVar()
        self.cb_var3 = tkinter.IntVar()


        self.cb_var1.set(1)       # checked = 1 and unchecked = 0
                                  # if you want all of them to be checked you just do that for each one (cb_var2 and cb_var3)

        self.cb1 = tkinter.Checkbutton(self.top_frame,
                                       text='Option 1',
                                       variable=self.cb_var1)
        

        self.cb2 = tkinter.Checkbutton(self.top_frame,
                                       text='Option 2',
                                       variable=self.cb_var2)
        

        self.cb3 = tkinter.Checkbutton(self.top_frame,
                                       text='Option 3',
                                       variable=self.cb_var3)
        

        self.cb1.pack()
        self.cb2.pack()
        self.cb3.pack()




        self.ok_button = tkinter.Button(self.bottom_frame, text='OK', command=self.show_choice)
        self.quit_button = tkinter.Button(self.bottom_frame, text='Quit', command=self.main_window.destroy)

        self.top_frame.pack()
        self.bottom_frame.pack()

        self.ok_button.pack(side='left')
        self.quit_button.pack(side='right')


        tkinter.mainloop()

    
    def show_choice(self):
        message = 'You have selected: \n'

        if self.cb_var1.get() == 1:
            message += '1\n'

        if self.cb_var2.get() == 1:
            message += '2\n'

        if self.cb_var3.get() == 1:
            message += '3\n'  

        
        tkinter.messagebox.showinfo('Selection', message)

#create an instance of the MyGUI class (otherwise it wont run)
my_gui = MyGUI()

print('moving on...')       #this print once the user closes the window